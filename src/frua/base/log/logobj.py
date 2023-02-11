"""
Log Object module

Uses:
- logging: https://docs.python.org/3/library/logging.html
- sys: https://docs.python.org/3/library/sys.html

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import logging
import logging.config
import sys

class LogObj(logging.Logger):
    """"
    An object extending logging.Logger
    """

    def __init__(self, logger:str=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            logger (str): The name of the logger
            *args: Any positional arguments
            **kwargs: Any keyword arguments
        """
        if logger is None:
            logger = ''
        super().__init__(logger, *args, **kwargs)
        #setup logger
        self.logger = self.load_logger(logger)
    
    def add_console_logger(self, level:int=logging.DEBUG, \
        fmt:str='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt:str='%Y-%m-%d %H:%M:%S') -> None:
        """
        Add a console logger

        Args:
            level (int): The level of the logger
            fmt (str): The format of the logger
            datefmt (str): The date format of the logger
        """
        self._logger.setLevel(level)
        ch = logging.StreamHandler(stream = sys.stdout)
        ch.setLevel(level)
        # create formatter
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self._logger.addHandler(ch)

    def add_basic_console_logger(self, level:int=logging.INFO) -> None:
        """
        Add a basic console logger

        Args:
            level (int): The level of the logger
        """
        self.add_console_logger(level=level, fmt='%(message)s')

    def add_file_logger(self, filename:str='example.log', level:int=logging.DEBUG, \
        fmt:str='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt:str='%Y-%m-%d %H:%M:%S', \
            encoding:str='utf-8', mode:str='w') -> None:
        """
        Add a file logger

        Args:
            filename (str): The name of the file
            level (int): The level of the logger
            fmt (str): The format of the logger
            datefmt (str): The date format of the logger
            encoding (str): The encoding of the file
            mode (str): The mode of the file
        """
        self._logger.setLevel(level)
        fh = logging.FileHandler(filename=filename, encoding=encoding, mode=mode)
        fh.setLevel(level)
        # create formatter
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        # add formatter to ch
        fh.setFormatter(formatter)
        # add ch to logger
        self._logger.addHandler(fh)

    def load_logger(self, logger:str=None) -> logging.Logger:
        """
        Load a logger by name

        Args:
            logger (str): The name of the logger

        Returns:
            logging.Logger: The logger
        """
        if logger:
            self._logger = logging.getLogger(logger)
        else:
            self._logger = logging.getLogger(__name__)
        return self._logger
    
    def load_logger_from_dict(self, logger_dict:dict) -> logging.Logger:
        """
        Load a logger from a dictionary

        Args:
            logger_dict (dict): The dictionary containing the logger configuration

        Returns:
            logging.Logger: The logger
        """
        logging.config.dictConfig(logger_dict)
        return self._logger

    def disable(self, level:int=logging.INFO) -> None:
        """
        Disable the logger

        Args:
            level (int): The level of the logger
        """
        self._logger.disabled = True
        self._logger.setLevel(level)

    def enable(self, level=logging.INFO) -> None:
        """
        Enable the logger

        Args:
            level (int): The level of the logger
        """
        self._logger.disabled = False
        self._logger.setLevel(level)
    
    def is_disabled(self) -> bool:
        """
        Check if the logger is disabled

        Returns:
            bool: True if the logger is disabled, False otherwise
        """
        return self._logger.disabled
    
    def is_enabled(self) -> bool:
        """
        Check if the logger is enabled

        Returns:
            bool: True if the logger is enabled, False otherwise
        """
        return not self._logger.disabled