"""
TAR file manipulation (tar/untar)

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- tarfile: https://docs.python.org/3/library/tarfile.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import tarfile

class Tar:
    """
    TAR file manipulation (tar/untar)
    """

    def __init__(self, *args, **kwargs):
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
        if not hasattr(self, '_logger'):
            self._logger = logging.getLogger(__name__)

    def tar(self, dir, tar_file, fmt=None):
        """
        tar a directory

        Args:
        dir (str): path to directory
        tar_file (str): path to tar file
        fmt (str): compression format (gz, bz2, xz, None)

        Returns:
            bool: True if tarping was successful
        """
        self._logger.debug("Starting to tar dir: %s", dir)
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
                self._logger.debug("Created dir: %s", dir)
                self._logger.debug("Starting to tar dir: %s", dir)
                if fmt:
                    tar_ref = tarfile.open(tar_file, 'w:%s'%fmt)
                else:
                    tar_ref = tarfile.open(tar_file, 'w')
                tar_ref.add(dir)
                tar_ref.close()
                self._logger.debug("Done tarping dir: %s", dir)
                self._logger.info("Done tarping dir: %s", dir)
                return True
        except Exception as e:
            self._logger.error("Failed to tar dir: %s", dir)
            self._logger.error(e)
            return False
    
    def untar(self, dir, tar_file, fmt=None):
        """
        untar a directory

        Args:
        dir (str): path to directory
        tar_file (str): path to tar file
        fmt (str): compression format (gz, bz2, xz, None)

        Returns:
            bool: True if untaring was successful
        """
        self._logger.debug("Starting to untar dir: %s", dir)
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
                self._logger.debug("Created dir: %s", dir)
                self._logger.debug("Starting to untar dir: %s", dir)
                if fmt:
                    tar_ref = tarfile.open(tar_file, 'r:%s'%fmt)
                else:
                    tar_ref = tarfile.open(tar_file, 'r')
                tar_ref.extractall(dir)
                tar_ref.close()
                self._logger.debug("Done untaring dir: %s", dir)
                self._logger.info("Done untaring dir: %s", dir)
                return True
        except Exception as e:
            self._logger.error("Failed to untar dir: %s", dir)
            self._logger.error(e)
            return False