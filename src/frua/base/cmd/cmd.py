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
import sys
import subprocess
import shlex

class CmdLine(object):
    """
    Command line object

    Performs command line transformations between string and list using shlex.
    """
    def __init__(self, line:str=None) -> None:
        """
        Constructor

        Args:
            line(str, optional): the command line
        """
        if line:
            self._args = shlex.split(line)

    @property  
    def line(self) -> str:
        """
        Returns the command line
        """
        return str(shlex.join(self._args))
    
    @line.setter
    def line(self, value:str) -> None:
        """
        Set the command line
        """
        self._args = shlex.split(value)
    
    @property
    def args(self) -> list:
        """
        Returns the command line arguments
        """
        return self._args
    
    @args.setter
    def args(self, value:list) -> None:
        """
        Set the command line arguments
        """
        self._args = value
    
    def __str__(self) -> str:
        """
        Returns the command line string
        """
        return self.line

    def __repr__(self) -> str:
        """
        Returns the command line string
        """
        return self.line
    
    def quote(self) -> str:
        """
        Returns the command line string with quotes
        """
        line = self.line
        qline = shlex.quote(line)
        return qline

class Cmd(object):
    """
    Command Object
    """
    def __init__(self, cmdline:object=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            cmdline(object, optional): the command line object. can be a string or a list of arguments (list of strings)
            args: positional arguments
            kwargs: keyword arguments
        """
        super().__init__()
        #line
        self.cmdlineargs = None
        if cmdline != None:
            self._clean_cmdline(cmdline)
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)
    
    def _clean_cmdline(self, cmdline:object) -> None:
        """
        Split the command line with shlex to clean it as a list of arguments to reduce risks of shell injection

        if string: shlex.split
        if list: shlex.split if only one argument in list, else list of strings

        Args:
            cmdline(object): the command line object. can be a string or a list of arguments (list of strings)
        """
        if isinstance(cmdline, str):
            self.cmdlineargs = CmdLine(cmdline).args
        elif isinstance(cmdline, list):
            if len(cmdline) == 1:
                self.cmdlineargs = CmdLine(cmdline[0]).args
            else:
                self.cmdlineargs = cmdline
        else:
            raise TypeError('cmdline must be a string or a list of arguments')

    def raw(self, cmdline:list=None, shell:bool=False, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a command

        Args:
            cmdline(list, optional): the command line object. can be a string or a list of arguments (list of strings)
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        if cmdline == None:
            cmdline = self.cmdlineargs
        if hasattr(self, '_logger'):
            logging.info(f'Running command: {cmdline}')
        if 'verbose' in kwargs:
            print(f'Running command: {cmdline}')
        #executing command
        result = subprocess.run(cmdline, capture_output=True, shell=shell, check=check, stdout=stdout, stderr=stderr)
        #handle stdout
        if result.stdout:
            if hasattr(self, '_logger'):
                logging.info('stdout: %s'%(result.stdout.decode()))
            if 'verbose' in kwargs:
                print(f"stdout:", result.stdout)
        #handle stderr
        if result.stderr:
            if hasattr(self, '_logger'):
                logging.error('stderr: %s'%(result.stderr.decode()))
            if 'verbose' in kwargs:
                print(f"stderr:", result.stderr)
        #handle return code
        if result.returncode:
            if hasattr(self, '_logger'):
                logging.info('return code: {result.returncode}')
            if 'verbose' in kwargs:
                print(f"return code: {result.returncode}")
        return result 

    def cmd(self, cmdline:object=None, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a command not using the shell

        Args:
            cmdline(object, optional): the command line object. can be a string or a list of arguments (list of strings)
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        if (cmdline != None):
            #handle sudo
            if isinstance(cmdline, list):
                if 'sudo' in kwargs:
                    args = ['sudo']
                    args.extend(cmdline)
                else:
                    args = cmdline
            elif isinstance(cmdline, str):
                if 'sudo' in kwargs:
                    args = 'sudo ' + cmdline
                else:
                    args = cmdline
            else:
                raise TypeError('cmdline must be a string or a list of arguments')            
        #clean input a bit first        
            self._clean_cmdline(args)
        #run as raw command once cleaned
        return self.raw(self.cmdlineargs, shell=False, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def shell(self, cmdline:object=None, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a command using the shell

        Args:
            cmdline(object, optional): the command line object. can be a string or a list of arguments (list of strings)
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        if (cmdline != None):
            #handle sudo
            if isinstance(cmdline, list):
                if 'sudo' in kwargs:
                    args = ['sudo']
                    args.extend(cmdline)
                else:
                    args = cmdline
            elif isinstance(cmdline, str):
                if 'sudo' in kwargs:
                    args = 'sudo ' + cmdline
                else:
                    args = cmdline
            else:
                raise TypeError('cmdline must be a string or a list of arguments')            
            #clean input a bit first
            self._clean_cmdline(args)
        #run as raw command once cleaned
        return self.raw(self.cmdlineargs, shell=True, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def bash_script(self, script:str, scriptargs:list=None, shell:bool=False, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a bash script

        Args:
            script(str): the path to the bash script
            scriptargs(list, optional): the arguments to the bash script
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        args = list()
        #sudo
        if 'sudo' in kwargs:
            args.append('sudo')
        #bash
        args.append('bash')
        #script
        args.append(script)
        #script args
        if scriptargs!= None:
            args.extend(scriptargs)
        #execute command
        return self.raw(args, shell=shell, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def bash(self, command:str, shell:bool=False, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a bash command

        Args:
            command(str): the bash command to execute
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        args = list()
        #sudo
        if 'sudo' in kwargs:
            args.append('sudo')
        #bash
        args.append('bash')
        #bash command
        args.append('-c')
        #command to execute
        args.append(command)
        #execute command
        return self.raw(args, shell=shell, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def python_script(self, script:str, scriptargs:list=None, shell:bool=False, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a python script

        Args:
            script(str): the path to the python script
            scriptargs(list, optional): the arguments to the python script
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        args = list()
        #sudo
        if 'sudo' in kwargs:
            args.append('sudo')
        #bash
        args.append(sys.executable)
        #script
        args.append(script)
        #script args
        if scriptargs!= None:
            args.extend(scriptargs)
        #execute command
        return self.raw(args, shell=shell, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def python(self, command:str, shell:bool=False, check:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a python command

        Args:
            command(str): the python command to execute
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            check (bool, optional): check for errors. Defaults to False. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)
        
        Returns:
            result: The result object from subprocess.run
        """
        args = list()
        #sudo
        if 'sudo' in kwargs:
            args.append('sudo')
        #bash
        args.append(sys.executable)
        #command
        args.append('-c')
        #python command to execute
        args.append(command)
        #execute command
        return self.raw(args, shell=shell, check=check, stdout=stdout, stderr=stderr, **kwargs)

    def raw_line(self, cmd:str, shell:bool=False, stdout:int=None, stderr:int=None, **kwargs):
        """
        Run a command in string format

        Args:
            cmd(str): command to run
            shell (bool, optional): run command in a separate shell. Defaults to True. See subprocess documentation.
            stdout (int, optional): stdout. Defaults to subprocess.PIPE. See subprocess documentation.
            stderr (int, optional): stderr. Defaults to subprocess.PIPE. See subprocess documentation.
            kwargs: keyword arguments (passed to subprocess.run)

        !! Vulnerable to shell injection - prefer other methods!!

        Returns:
            result: The result object from subprocess.run
        """        
        if'sudo' in kwargs:
            cmd1 ='sudo'+ cmd
        else:
            cmd1 = cmd
        if hasattr(self, '_logger') or'verbose' in kwargs:
            logging.info(f'Running command: {cmd1}')
        try:
            result = subprocess.Popen([cmd1], shell=shell, stdout=stdout, stderr=stderr)
            result.wait(timeout=5)
            #handle stdout
            if result.stdout:
                if hasattr(self, '_logger'):
                    logging.info('stdout: %s'%(result.stdout.decode()))
                if 'verbose' in kwargs:
                    print(f"stdout:", result.stdout)
            #handle stderr
            if result.stderr:
                if hasattr(self, '_logger'):
                    logging.error('stderr: %s'%(result.stderr.decode()))
                if 'verbose' in kwargs:
                    print(f"stderr:", result.stderr)
            #handle return code
            if result.returncode:
                if hasattr(self, '_logger'):
                    logging.info('return code: {result.returncode}')
                if 'verbose' in kwargs:
                    print(f"return code: {result.returncode}")
            return result        
        except Exception as e:
            if hasattr(self, '_logger') or'verbose' in kwargs:
                logging.error(f'Command failed: {e}') 
            return e

    def raw_os(self, cmd: str, **kwargs) -> int:
        """
        Run a command in string format with os.system

        !! Vulnerable to shell injection - prefer other methods!!

        Args:
            cmd(str): command to run
            sudo(bool, optional): run as sudo

        Returns:
            int: the return code of the command
        """
        if 'sudo' in kwargs:
            cmd1 = 'sudo ' + cmd
        else:
            cmd1 = cmd
        if hasattr(self, '_logger') or 'verbose' in kwargs:
            logging.info(f'Running command: {cmd1}')
        try:
            output = os.system(cmd1)
            if output:
                if hasattr(self, '_logger') or 'verbose' in kwargs:
                    logging.info(f'Output: {output}')
            return output
        except Exception as e:
            if hasattr(self, '_logger') or 'verbose' in kwargs:
                logging.error(f'Command failed: {e}')
            raise e
