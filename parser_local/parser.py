import abc


class Parser(abc.ABC):

    @abc.abstractmethod
    def parse(self, file_path):
        pass
