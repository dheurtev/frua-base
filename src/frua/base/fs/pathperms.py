"""
POSIX Path permissions helpers (for files and directories)

Does not require pathlib

Uses:
- os: https://docs.python.org/3/library/os.html
- pwd: https://docs.python.org/3/library/pwd.html
- grp: https://docs.python.org/3/library/grp.html
- stat: https://docs.python.org/3/library/stat.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import pwd
import grp
from stat import (S_IRUSR, S_IWUSR, S_IXUSR, S_IRGRP, S_IWGRP,
                  S_IXGRP, S_IROTH, S_IWOTH, S_IXOTH)

class PathPerms(object):
    """
    Path permissions helpers (for files and directories)
    """
    def __init__(self, path=None) -> None:
        """
        Constructor

        Args:
            path (str, optional): path (file or directory)
        """
        
        if path != None:
            self._path = path
        else:
            self._path = None

    @property
    def path(self) -> str:
        """
        Returns path

        Returns:
            str: path (file or directory) else None
        """
        if self._path!= None:
           return os.path.normpath(self._path)
        else:
            return None

    @path.setter
    def path(self, value:str) -> None:
        """
        Set the path of the file

        Args:
           value (str): path of the file       
        """
        self._path = os.path.normpath(str(value))

    @property
    def uid(self) -> str:
        """
        Returns the uid of the file

        Returns:
            str: uid of the owner of the file
        """
        return os.stat(self._path).st_uid
    
    @property
    def gid(self) -> str:
        """
        Returns the gid of the file

        Returns:
            str: group gid of the file
        """
        return os.stat(self._path).st_gid
    
    @property
    def stats(self) -> dict:
        """
        Returns the file statistics

        Returns:
            dict: file statistics
        """
        return os.stat(self._path)

    def perms(self, rep='str') -> int:
        """
        Returns the permissions of the file

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            int: permissions of the file in octets
        """
        oct_rep = oct(os.stat(self._path).st_mode)
        if rep == 'str':
            res = ''
            #file or directory
            dir_rep = str(oct_rep)[-4]
            if dir_rep == '0':
                res += '-'
            else:
                res += 'd'
            #user, group, other
            tmp_rep = str(oct_rep)[-3:]
            for char in tmp_rep:
                perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
                res += perms[char]	    
            return res
        else:
            return oct_rep

    @property
    def owner_name(self) -> str:
        """
        Returns the owner name of the Path

        Returns:
            str: owner of the file
        """
        return str(pwd.getpwuid(self.uid).pw_name)

    @property
    def group_name(self) -> str:
        """
        Returns the group name of the Path
        Returns:
            str: group of the file
        """
        return str(grp.getgrgid(self.gid).gr_name)

    def others_perms(self, rep='str') -> str:
        """
        Return the others permissions as a string or as an octet number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: others permissions
        """
        mode =str(self.perms('oct'))
        res = mode[-1]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def group_perms(self, rep='str') -> str:
        """
        Return the group permission as a string or as an octet number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: group permissions
        """
        mode =str(self.perms('oct'))
        res = mode[-2]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def owner_perms(self, rep='str') -> str:
        """
        Return the owner permission as a string or as an octet number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: owner permissions
        """
        mode =str(self.perms('oct'))
        res = mode[-3]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def is_readable(self)-> bool:
        """
        Is the file readable

        Returns:
            bool: True if the file is readable, False otherwise
        
        """
        return os.access(self.path, os.R_OK)
    
    def is_writable(self)-> bool:
        """
        Is the file writable

        Returns:
            bool: True if the file is read write, False otherwise
        """
        return os.access(self.path, os.W_OK)

    def is_executable(self)-> bool:
        """
        Is the file executable

        Returns:
            bool: True if the file is executable, False otherwise
        """
        return os.access(self.path, os.X_OK)
    
    def is_read_only(self)-> bool:
        """
        Is the file readable only

        Returns:
            bool: True if the file is readable only, False otherwise
        """
        readable = self.is_readable()
        writeable = self.is_writable()
        executable = self.is_executable()
        if readable and not writeable and not executable:
            return True
        else:
            return False

    def is_read_writable(self)-> bool:
        """
        Is the file readable and writeable

        Returns:
            bool: True if the file is readble and writeable only, False otherwise
        """
        readable = self.is_readable()
        writeable = self.is_writable()
        executable = self.is_executable()
        if (readable and writeable) and not executable:
            return True
        else:
            return False

    def is_read_executable(self)-> bool:
        """
        Is the file readable and executable

        Returns:
            bool: True if the file is readable and executable only, False otherwise
        """
        readable = self.is_readable()
        writeable = self.is_writable()
        executable = self.is_executable()
        if (readable and executable) and not writeable:
            return True
        else:
            return False

    def is_full_access(self)-> bool:
        """
        Is the file readable and writeable and executable

        Returns:
            bool: True if the file is readable and writeable and executable only, False otherwise
        """
        readable = self.is_readable()
        writeable = self.is_writable()
        executable = self.is_executable()
        if readable and writeable and executable:
            return True
        else:
            return False
