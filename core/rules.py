import abc
import sys
from core.actions import *
from commons.git import GitCommons
from commons.logger import Logger
from commons.phoenix import PhoenixCommons
from commons.python import PythonCommons
from exception.custom_exceptions import ExecutionException


class Rules(abc.ABC):

    @staticmethod
    def fire_rules(execution):

        if (not GitCommons.has_unstaged_files()):
            if (not GitCommons.is_ahead()):
                actions = {}
                i = 0

                for action_execution in execution.action["execution"]:
                    action_from_template = action_execution["do"]["action"]

                    Logger.info(cls=Rules, msg=(("Validating method " +
                                                 PythonCommons.LIGHT_GREEN +
                                                 "{}" +
                                                 PythonCommons.NC +
                                                 "...").format(action_from_template)))

                    action_to_run = Rules._translate(method_name=action_from_template)
                    action_class = eval(action_to_run.replace("_", " ").title().replace(" ", ""))
                    action = action_class(execution, action_execution)

                    if (action.is_implemented):
                        if (not action.confirm_execution()):
                            Logger.warn(cls=Checkout, msg="Execution stopped by user")
                            sys.exit()

                        actions[i] = action
                        i += 1

                all_actions = [action.action_execution["do"]["action"] for action in actions.values()]

                for action in actions.values():
                    Logger.info(cls=Rules, msg=(("Executing method " +
                                                 PythonCommons.LIGHT_GREEN +
                                                 "{}" +
                                                 PythonCommons.NC +
                                                 "...").format(action.action_execution["do"]["action"])))
                    try:
                        all_actions.pop(0)
                        action.execute()
                    except ExecutionException:
                        if (len(all_actions) > 0):
                            Logger.error(cls=Rules, msg=("An error has ocurred while processing! " +
                                                         "The following action(s) couldn't be executed:" +
                                                         PythonCommons.LIGHT_CYAN +
                                                         " {}" +
                                                         PythonCommons.NC +
                                                         "!").format(", ".join(all_actions)))
            else:
                Logger.error(cls=Rules, msg="You are ahead of remote branch! Please push your changes before proceeding.")
        else:
            Logger.error(cls=Rules, msg="You have unstaged files! Please commit them before proceeding.")

    @staticmethod
    def _translate(method_name):
        if (method_name == "create_branch"):
            return "checkout"

        return method_name
