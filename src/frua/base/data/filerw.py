"""
Basic file read/write with a dry run mode

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging

class FileRW(object):
    """
    File Read Write handler
    
    Basic file read/write with a dry run mode
    """
    def __init__(self, path, content=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            path (str): the file path
            content (list):The content to write in the file as a list of lines
            args: positional arguments
            kwargs: keyword arguments
        """
        super().__init__()
        #handle other attributes
        self.path = path
        self.content = content
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)

    def write(self, content:list=None, mode:str='w+', dry:bool=False) -> int:
        """
        Write the content to a file, except in dry run mode

        Args:
            content (list):The content to write in the file as a list of lines
            mode (str):The file writing mode
            dry (bool): flag indicating a dry run

        Returns:
           :int:Status: 0 is OK, 1 is dry run, 2 is error

        """
        #set content
        if content:
            self.content = content
        #dry run
        if dry:
            if hasattr(self, '_logger'):
                self._logger.debug('DRY RUN - Content %s should have been written to %s'%(self.content, self.path))
            return 1
        #normal read
        try:
            with open(self.path, mode) as file:
                file.writelines(self.content)
                file.close()
            if hasattr(self, '_logger'):
                self._logger.debug('Content %s written to %s'%(self.content, self.path))
            return 0
        except Error as e:
            if hasattr(self, '_logger'):
                self._logger.error('Could not write to the file %s'%(self.path))
                self._logger.error(e)
            return 2

    def read(self, mode:str='r+', dry:bool=False) -> int:
        """
        Read the content from a file, except in dry run mode

        Args:
            mode (str):The file reading mode
            dry (bool): flag indicating a dry run

        Returns:
           :int:Status: 0 is OK, 1 is dry run, 2 is error

        """
        #dry run
        if dry:
            if hasattr(self, '_logger'):
                self._logger.debug('DRY RUN - Content should have been read from %s'%(self.path))
            return 1
        #normal write
        try:

            with open(self.path, mode) as file:
                content = file.readlines()
                file.close()
            if hasattr(self, '_logger'):
                self._logger.debug('File content %s read from %s'%(content, self.path))
            self.content = content
            return 0
        except Error as e:
            if hasattr(self, '_logger'):
                self._logger.error('Could not read the file %s'%(self.path))
                self._logger.error(e)
            return 1