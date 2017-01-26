from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from lib.exceptions import Execution_Error, Invalid_Argument
import os


def execute_cmd(sshclient, cmd, log):
    logger.console('\nExecuting "%s"' % cmd)
    log.info('Executing "%s"' % cmd)
    return_code, stdout, stderr = sshclient.command_exec(cmd)
    if return_code != 0:
        log.error(stdout)
        raise Execution_Error(stdout)
    logger.console("%s " % stdout)
    try:
        stdout = stdout.replace("", "")
    except:
        pass
    log.info(stdout)
    return stdout


def form_cmd(args, kwargs, cmd):
    for key in kwargs.keys():
        if key in args:
            cmd += "-{} {} ".format(key, kwargs[key])
        else:
            raise Invalid_Argument("Invalid argument '%s'\n" % key)

    return cmd
