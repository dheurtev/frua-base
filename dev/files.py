""""
pyinfra_plugins: Files module
"""
__author__ = "David HEURTEVENT"
__copyright__ = "David HEURTEVENT"
__license__ = "MIT"

import os
import logging

class Files(object):
    """
    Files class
    """

    def __init__(self, logger=None):
        """
        Constructor

        logger (logging.Logger): the logger to use (optional)
        """
        #setup logger
        if logger:
            self._logger = logger
        else:
            self._logger = logging.getLogger(__name__)

    def copy(self, src, dst):
        """
        Copy a file
        """
        self._logger.debug("Starting to copy file: %s", src)
        try:
            if not os.path.exists(dst):
                os.makedirs(dst)
                self._logger.debug("Created dir: %s", dst)
                self._logger.debug("Starting to copy file: %s", src)
                shutil.copy(src, dst)
                self._logger.debug("Done copying file: %s", src)
                self._logger.info("Done copying file: %s", src)
                return True
        except Exception as e:
            self._logger.error("Failed to copy file: %s", src)
            self._logger.error(e)
            return False
    
    def move(self, src, dst):
        """
        Move a file
        """
        self._logger.debug("Starting to move file: %s", src)
        try:
            if not os.path.exists(dst):
                os.makedirs(dst)
                self._logger.debug("Created dir: %s", dst)
                self._logger.debug("Starting to move file: %s", src)
                shutil.move(src, dst)
                self._logger.debug("Done moving file: %s", src)
                self._logger.info("Done moving file: %s", src)
                return True
        except Exception as e:
            self._logger.error("Failed to move file: %s", src)
            self._logger.error(e)
            return False
    
    def copydir(self, src, dst):
        """
        Copy a directory
        """
        self._logger.debug("Starting to copy dir: %s", src)
        try:
            if not os.path.exists(dst):
                os.makedirs(dst)
                self._logger.debug("Created dir: %s", dst)
                self._logger.debug("Starting to copy dir: %s", src)
                shutil.copytree(src, dst)
                self._logger.debug("Done copying dir: %s", src)
                self._logger.info("Done copying dir: %s", src)
                return True
        except Exception as e:
            self._logger.error("Failed to copy dir: %s", src)
            self._logger.error(e)
            return False
    
    def movedir(self, src, dst):
        """
        Move a directory
        """
        self._logger.debug("Starting to move dir: %s", src)
        try:
            if not os.path.exists(dst):
                os.makedirs(dst)
                self._logger.debug("Created dir: %s", dst)
                self._logger.debug("Starting to move dir: %s", src)
                shutil.movetree(src, dst)
                self._logger.debug("Done moving dir: %s", src)
                self._logger.info("Done moving dir: %s", src)
                return True
        except Exception as e:
            self._logger.error("Failed to move dir: %s", src)
            self._logger.error(e)
            return False