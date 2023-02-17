"""
Files manipulation with logger

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- shutil: https://docs.python.org/3/library/shutil.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import shutil

class File(object):
    """
    File class
    """

    def __init__(self, path=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args: positional arguments
            kwargs: keyword arguments
        """
        super().__init__()
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)
        #handle path
        if path != None:
            self._path = path
        else:
            self._path = None

    @property
    def path(self) -> str:
        """
        Returns the path

        Returns:
            str: path
        """
        return self._path

    @path.setter
    def path(self, path:str) -> None:
        """
        Set the path

        Args:
            path: path
        """
        self._path = path

    def copy(self, dst:str) -> bool:
        """
        Copy a file to a destination

        Args:
            dst (str): destination

        Returns:
            bool: success
        """
        if self.path is None:
            self._logger.error("No path to copy")
            return False
        src = self.path
        self._logger.debug("Starting to copy file: %s", src)
        try:
            par = os.path.dirname(dst)
            if not os.path.exists(par):
                os.makedirs(par)
                self._logger.debug("Created dir: %s", par)
            self._logger.debug("Starting to copy file: %s", src)
            #copy
            shutil.copy(src, dst)
            self._logger.debug("Done copying file: %s", src)
            self._logger.info("Done copying file: %s", src)
            return True
        except Exception as e:
            self._logger.error("Failed to copy file: %s", src)
            self._logger.error(e)
            return False
    
    def move(self, dst:str) -> bool:
        """
        Move a file to a destination

        Args:
            dst (str): destination

        Returns:
            bool: success
        """
        if self.path is None:
            self._logger.error("No path to copy")
            return False
        src = self.path
        self._logger.debug("Starting to move file: %s", src)
        try:
            par = os.path.dirname(dst)
            if not os.path.exists(par):
                os.makedirs(par)
                self._logger.debug("Created dir: %s", par)
            self._logger.debug("Starting to move file: %s", src)
            #move the file
            shutil.move(src, dst)
            self._logger.debug("Done moving file: %s", src)
            self._logger.info("Done moving file: %s", src)
            return True
        except Exception as e:
            self._logger.error("Failed to move file: %s", src)
            self._logger.error(e)
            return False