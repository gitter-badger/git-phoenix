from commons.phoenix import PhoenixCommons


class Execution:

    def __init__(self, args, template):
        self.args = args[2:]
        self.template = template
        self.init = self.template["init"]
        self.commons = self.template["commons"]
        self.command = PhoenixCommons.retrieve_command(commands=self.template["commands"], command_name=args[0])
        self.action = PhoenixCommons.retrieve_action(actions=self.command["actions"], action_name=args[1])

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, args):
        self._args = args

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        self._template = template

    @property
    def init(self):
        return self._init

    @init.setter
    def init(self, init):
        self._init = init

    @property
    def commons(self):
        return self._commons

    @commons.setter
    def commons(self, commons):
        self._commons = commons

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action
