"""
To clone and deploy repositories

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import sys
import subprocess
import shlex

class Git(object):
    """
    Git object

    Methodes to clone and deploy repositories.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            logger (logging.Logger): the logger to use (optional)
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
    
