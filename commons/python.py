import abc
import os.path
import sys


class PythonCommons(abc.ABC):

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN_ORANGE = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    NC = "\033[0m"  # No Color

    @staticmethod
    def path(file_name):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    @staticmethod
    def read_input(cls, msg):
        from .logger import Logger
        user_input = None

        while not user_input:
            try:
                Logger.input(cls=cls, msg=msg)
                user_input = input()
            except EOFError:
                Logger.warn(cls=PythonCommons, msg="Please, " + msg)
            except KeyboardInterrupt:
                Logger.error(cls=PythonCommons, msg="Stopping execution")

        return user_input

    @staticmethod
    def define_pattern(pattern, should_start, should_end):
        if (isinstance(pattern, list)):
            for i in range(len(pattern)):
                pattern[i] = pattern[i].replace("^", "").replace("$", "").replace("/", "\/")
    
            pattern = "".join(pattern)

        if (should_start):
            pattern = "^" + pattern
        if(should_end):
            pattern = pattern + "$"

        return pattern

    @staticmethod
    def beautify_exception():
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return "Error type: " + str(exc_type) + " | Module: " + str(fname) + " | Line number: " + str(exc_tb.tb_lineno)