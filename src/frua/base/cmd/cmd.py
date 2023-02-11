"""
To execute terminal command and run bash scripts

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- sys: https://docs.python.org/3/library/sys.html
- subprocess: https://docs.python.org/3/library/subprocess.html
- shlex: https://docs.python.org/3/library/shlex.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging

class CMD(object):
    """
    Command Object
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args: positional arguments
            kwargs: keyword arguments
        """
        pass
        super().__init__()
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)
  
    def run(self, cmdargs:list, shell:bool=True) -> None:
        """
        Run a command as a list of arguments

        Args:
            cmdargs (list): list of command arguments
            shell (bool, optional): run command in shell. Defaults to True.
        """
        if hasattr(self, 'logger'):
            logging.info(f'Running command: {args}')
        try:
            output = subprocess.run(self._args, capture_output=True)
            if hasattr(self, 'logger'):
                logging.info(f'Command executed successfully')
                if output:
                    logging.info(f'Output: {output}')
            else:
                if output:
                    print(output)
        except Exception as e:
            logging.error(f'Command failed: {e}')
            raise e

    def run_os_system(self, cmd: str) -> None:
        """
        Run a command in string format with os.system

        !! Vulnerable to shell injection - prefer other methods!!

        Args:
            cmd(str): command to run
        """
        if hasattr(self, 'logger'):
            logging.info(f'Running command: {cmd}')
        try:
            output = os.system(cmd)
            if hasattr(self, 'logger'):
                logging.info(f'Command executed successfully')
                if output:
                    logging.info(f'Output: {output}')
            else:
                if output:
                    print(output)
        except Exception as e:
            logging.error(f'Command failed: {e}')
            raise e
    
