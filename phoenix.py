#!/usr/bin/env python

import abc
import os
import sys
from commons.git import GitCommons
from commons.phoenix import PhoenixCommons
from commons.python import PythonCommons
from commons.logger import Logger
from core.execution import Execution
from core.rules import Rules
from parser_local import *


class Phoenix(abc.ABC):

    @staticmethod
    def execute(args):
        PhoenixCommons.draw_phoenix()

        GitCommons.require_git_repo(msg="git phoenix cannot be used without a git repository!")
        template_path = PhoenixCommons.require_template()
        file_extension = os.path.splitext(template_path)[1][1:]
        parser_class = eval(file_extension.title() + "Parser")
        parser = parser_class()
        template = parser.parse(file_path=template_path)

        if ([] != args[1:]):
            # Create execution object to carry template and arguments through execution
            execution = Execution(args, template)

            Logger.info(cls=Phoenix, msg="Firing rules...")
            Rules.fire_rules(execution=execution)
        else:
            Logger.error(cls=Phoenix, msg="Please inform arguments to Phoenix! ")

if (__name__ == "__main__"):
    args = sys.argv[1:]
    Phoenix.execute(args)
