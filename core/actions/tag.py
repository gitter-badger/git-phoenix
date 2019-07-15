from .executable import Executable
from commons.logger import Logger


class Tag(Executable):

    def __init__(self, execution, action_execution):
        super().__init__(execution, action_execution)
        self.is_implemented = False

    def execute(self):
        Logger.warn(cls=Tag, msg="Not implemented yet!")

    def _parse(self):
        pass
