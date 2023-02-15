"""
Users shortcuts

Uses:
- pwd: https://docs.python.org/3/library/pwd.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pwd

class Users(object):
    """
    Users Utility class
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
  
    def uid(self, user:str) -> int:
        """
        Return the user name associated to the uid

        Args:
            user (str): user name

        Returns:
            int: uid
        """
        return pwd.getpwnam(user).pw_uid

    def user(self, uid:int) -> str:
        """
        Return the user name associated to the uid

        Args:
            uid (int): uid

        Returns:
            str: user name
        """
        return pwd.getpwuid(uid).pw_name
