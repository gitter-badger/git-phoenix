import abc
import git
import os
import re
import sys
from git import Repo
from git.exc import GitCommandError
from .logger import Logger
from .python import PythonCommons


class GitCommons(abc.ABC):

    @staticmethod
    def checkout(branch):
        git = Repo().git
        Logger.info(cls=GitCommons, msg=("Checking out branch" +
                                         PythonCommons.LIGHT_CYAN +
                                         " {}" +
                                         PythonCommons.NC +
                                         "...").format(branch))

        git.checkout(branch)

    @staticmethod
    def checkout_new_branch(origin, branch):
        git = Repo().git
        GitCommons.checkout(origin)
        GitCommons.pull(origin)
        Logger.info(cls=GitCommons, msg=("Creating branch" +
                                         PythonCommons.LIGHT_CYAN +
                                         " {} " +
                                         PythonCommons.NC +
                                         "based on" +
                                         PythonCommons.LIGHT_CYAN +
                                         " {} " +
                                         PythonCommons.NC +
                                         "...").format(branch, origin))
        try:
            git.checkout(origin, b=branch)
        except GitCommandError:
            Logger.error(cls=GitCommons, msg=("Branch" +
                                              PythonCommons.LIGHT_CYAN +
                                              " {} " +
                                              PythonCommons.NC +
                                              "already exists!").format(branch))

    @staticmethod
    def merge(branch, destination):
        git = Repo().git

        if (not GitCommons._already_merged(destination, branch)):
            GitCommons.checkout(destination)
            GitCommons.pull(destination)
            Logger.info(cls=GitCommons, msg=("Merging branch" +
                                             PythonCommons.LIGHT_CYAN +
                                             " {} " +
                                             PythonCommons.NC +
                                             "into" +
                                             PythonCommons.LIGHT_CYAN +
                                             " {}" +
                                             PythonCommons.NC +
                                             "...").format(branch, destination))

            try:
                git.merge(branch, "--no-ff")
            except:
                Logger.error(cls=GitCommons, msg="You have conflicts on your working tree! Resolve them before commiting!")
        else:
            Logger.warn(cls=GitCommons, msg=("Branch" +
                                             PythonCommons.LIGHT_CYAN +
                                             " {} " +
                                             PythonCommons.NC +
                                             "already merged into" +
                                             PythonCommons.LIGHT_CYAN +
                                             " {}" +
                                             PythonCommons.NC +
                                             "!").format(branch, destination))

    @staticmethod
    def pull(branch):
        git = Repo().git
        Logger.info(cls=GitCommons, msg=("Updating branch " +
                                         PythonCommons.LIGHT_CYAN +
                                         "{}" +
                                         PythonCommons.NC +
                                         "...").format(branch))
        try:
            git.pull()
        except GitCommandError:
            pass

    @staticmethod
    def has_unstaged_files():
        git = Repo().git
        unstaged_files = git.status("--porcelain")

        if (not unstaged_files):
            return False

        return True

    @staticmethod
    def config(key, value):
        pass

    @staticmethod
    def retrieve_config(key):
        try:
            git = Repo().git
            return git.config(key)
        except GitCommandError:
            return None

    @staticmethod
    def _has_config(key, value):
        pass

    @staticmethod
    def require_git_repo(msg):
        is_git_repo_ = GitCommons.is_git_repo()

        if (not is_git_repo_):
            Logger.critical(cls=GitCommons, msg=msg)

    @staticmethod
    def is_git_repo():
        try:
            git.Repo(os.getcwd()).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    @staticmethod
    def retrieve_current_branch():
        repo = Repo()
        return repo.active_branch.name

    @staticmethod
    def log(parameters):
        git = Repo().git

        if (parameters):
            return git.log(parameters)

        return git.log()

    @staticmethod
    def current():
        return GitCommons.retrieve_current_branch()

    @staticmethod
    def raw_current():
        branch_name = GitCommons.current()
        splitted_branch_name = branch_name.split("/")

        return splitted_branch_name[-1]

    @staticmethod
    def last_merged(args):
        branch = args[0]

        merge_branch = GitCommons.log(["--oneline", "--merges", "--grep=into", branch, "-1"])
        translated_merge_message = GitCommons._translate_merge_message(msg=merge_branch)
        origin = translated_merge_message["origin"]
        destination = translated_merge_message["destination"]

        if ([] != args[1:]):
            origin = re.search(PythonCommons.define_pattern(args[1]), origin).group(0)

        return origin

    @staticmethod
    def _already_merged(destination, branch):
        merged_branches = GitCommons.log(["--oneline", "--merges", "--grep=into", destination]).splitlines()

        for merged_branch in merged_branches:
            translated_merge_message = GitCommons._translate_merge_message(msg=merged_branch)

            if (translated_merge_message["origin"] == branch):
                return True

        return False

    @staticmethod
    def _translate_merge_message(msg):
        translated_merge_message = {}

        origin = msg.split("branch ")

        if ([] != origin[1:]):
            origin = origin[1]
        else:
            origin = origin[0]

        origin = origin[:origin.index(" ")]

        translated_merge_message["origin"] = origin.replace("'", "")
        translated_merge_message["destination"] = msg.split("into ")[-1].replace("'", "")

        return translated_merge_message

    @staticmethod
    def is_ahead():
        repo = Repo()
        branch = GitCommons.retrieve_current_branch()

        commits_ahead = repo.iter_commits("origin/" + branch + ".." + branch)
        number_of_commits = sum(1 for c in commits_ahead)

        return number_of_commits > 0
