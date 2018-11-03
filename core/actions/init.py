from .executable import Executable
from commons.logger import Logger


class Init(Executable):

    def __init__(self, execution):
        super().__init__(execution)

    def execute(self):
        Logger.warn(cls=Init, msg="Not implemented yet!")

    def _parse(self):
        pass
