import os
import platform
import subprocess


def install():
    origin_folder = os.getcwd()
    origin_file = origin_folder + "/phoenix.py"
    system = platform.system()

    dependencies_folder = "./dependencies/"

    colorama_file = dependencies_folder + "colorama-0.4.1-py2.py3-none-any.whl"
    colorlog_file = dependencies_folder + "colorlog-3.1.4-py2.py3-none-any.whl"
    gitpython_file = dependencies_folder + "GitPython-2.1.11-py2.py3-none-any.whl"
    regex_file_linux = dependencies_folder + "regex-2018.11.22.tar.gz"
    regex_file_windows = dependencies_folder + "regex-2018.11.22-cp37-none-win32.whl"

    colorama_install = ["pip", "install", colorama_file]
    colorlog_install = ["pip", "install", colorlog_file]
    gitpython_install = ["pip", "install", gitpython_file]
    regex_install = ["pip", "install"]

    if ("Linux" == system):
        import stat

        folder = subprocess.run(["which", "git"], stdout=subprocess.PIPE)
        folder = folder.stdout.decode('utf-8').replace("\n", "")
        folder = folder.replace("git", "")

        symbolic_link_array = ["sudo", "ln", "-s", origin_file, ""]

        scripts = [folder + "git-phoenix", folder + "git-px"]

        for script in scripts:
            symbolic_link_array[-1] = script

            subprocess.run(symbolic_link_array)
            st = os.stat(script)
            os.chmod(script, st.st_mode | stat.S_IEXEC)

        colorama_install.insert(0, "sudo")
        colorlog_install.insert(0, "sudo")
        gitpython_install.insert(0, "sudo")
        regex_install.insert(0, "sudo")
        regex_install.append(regex_file_linux)
    elif ("Windows" == system):
        folder = subprocess.run(["where", "git"], stdout=subprocess.PIPE)
        folder = folder.stdout.decode('utf-8').replace("\n", "")
        folder = folder.replace("cmd\\git.exe", "")
        folder = folder + "usr\\bin\\"

        origin_file = origin_file.replace("/", "\\")
        origin_commons = origin_folder + "\\commons"
        origin_core = origin_folder + "\\core"
        origin_exception = origin_folder + "\\exception"
        origin_parser_local = origin_folder + "\\parser_local"

        scripts = [folder + "git-phoenix", folder + "git-px"]
        folders = [folder + "commons", folder + "core", folder + "exception", folder + "parser_local"]
        dest_folders = [origin_commons, origin_core, origin_exception, origin_parser_local]
        symbolic_link_script_array = ["cmd", "/c", "mklink", "", origin_file]
        symbolic_link_folder_array = ["cmd", "/c", "mklink", "/J", "", ""]

        for script in scripts:
            symbolic_link_script_array[-2] = script
            subprocess.run(symbolic_link_script_array)

        for i in range(0, len(folders)):
            symbolic_link_folder_array[-2] = folders[i]
            symbolic_link_folder_array[-1] = dest_folders[i]
            subprocess.run(symbolic_link_folder_array)

        regex_install.append(regex_file_windows)

    subprocess.run(colorama_install)
    subprocess.run(colorlog_install)
    subprocess.run(gitpython_install)
    subprocess.run(regex_install)


if (__name__ == "__main__"):
    install()
