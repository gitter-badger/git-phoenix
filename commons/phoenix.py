import sys
from .git import GitCommons
from .logger import Logger
from .python import PythonCommons


class PhoenixCommons:

    phoenix_key_prefix = "phoenix."

    @staticmethod
    def config_phoenix_key(key, value):
        GitCommons.config(key=key, value=value)

    @staticmethod
    def retrieve_phoenix_key(key):
        return GitCommons.retrieve_config(key=PhoenixCommons.phoenix_key_prefix + key)

    @staticmethod
    def retrieve_template():
        return PhoenixCommons.retrieve_phoenix_key("template.path")

    @staticmethod
    def require_template():
        template = PhoenixCommons.retrieve_template()

        if (None is template):
            Logger.error(cls=PhoenixCommons, msg=("You must specify a template to use " +
                                                  "git phoenix! Run " +
                                                  PythonCommons.GREEN +
                                                  "git phoenix config template " +
                                                  PythonCommons.LIGHT_PURPLE +
                                                  "path_to_template " +
                                                  PythonCommons.NC +
                                                  "to configure it..."))
        else:
            return template

    @staticmethod
    def retrieve_commands(template):
        commands = []

        for command in template["commands"]:
            commands.append(command["name"])

        return commands

    @staticmethod
    def retrieve_command(commands, command_name):
        Logger.info(cls=PhoenixCommons, msg="Validating command...")

        for command in commands:
            if (command["name"] == command_name):
                return command

        Logger.error(cls=PhoenixCommons, msg=("Invalid command (" +
                                              PythonCommons.LIGHT_PURPLE +
                                              "{}" +
                                              PythonCommons.NC +
                                              ")!").format(command_name))

    @staticmethod
    def retrieve_action(actions, action_name):
        Logger.info(cls=PhoenixCommons, msg="Validating action...")

        for action in actions:
            if (action["name"] == action_name):
                return action

        Logger.error(cls=PhoenixCommons, msg=("Invalid action (" +
                                              PythonCommons.LIGHT_PURPLE +
                                              "{}" +
                                              PythonCommons.NC +
                                              ")!").format(action_name))

    @staticmethod
    def ask_for_input(args):
        if ([] == sys.argv[int(args[0]):]):
            value = PythonCommons.read_input(cls=PhoenixCommons, msg=args[1])
        else:
            value = sys.argv[int(args[0])]

        return value

    @staticmethod
    def determine_pattern(pattern):
        if (isinstance(pattern, list)):
            for i in range(len(pattern)):
                pattern[i] = pattern[i].replace("^", "").replace("$", "").replace("/", "\/")

        pattern = "".join(pattern)
        pattern = "^" + pattern + "$"

        return pattern

    @staticmethod
    def determine_prefix(prefix):
        return "".join(prefix)

    @staticmethod
    def use_passed_arg(args):
        if ([] == sys.argv[int(args[0]):]):
            value = args[1]
        else:
            value = sys.argv[int(args[0])]

        return value

    @staticmethod
    def draw_phoenix():
        print(PythonCommons.YELLOW + "______ _                     " + PythonCommons.RED + " _")
        print(PythonCommons.YELLOW + "| ___ \ |                    " + PythonCommons.RED + "(_)")
        print(PythonCommons.YELLOW + "| |_/ / |" + PythonCommons.BROWN_ORANGE + "__   ___  " + PythonCommons.LIGHT_RED + " ___ _ __ "  + PythonCommons.RED + " ___  __")
        print(PythonCommons.YELLOW + "|  __/| '" + PythonCommons.BROWN_ORANGE + "_ \ / _ \ " + PythonCommons.LIGHT_RED + "/ _ \ '_ \\" + PythonCommons.RED + "| \ \/ /")
        print(PythonCommons.YELLOW + "| |   | |" + PythonCommons.BROWN_ORANGE + " | | (_) |" + PythonCommons.LIGHT_RED + "  __/ | | "  + PythonCommons.RED + "| |>  <")
        print(PythonCommons.YELLOW + "\_|   |_|" + PythonCommons.BROWN_ORANGE + " |_|\___/ " + PythonCommons.LIGHT_RED + "\___|_| |_"  + PythonCommons.RED + "|_/_/\_\\" + PythonCommons.NC)
        print(PythonCommons.LIGHT_BLUE + "                               v0.0.1" + PythonCommons.NC)
        print()
