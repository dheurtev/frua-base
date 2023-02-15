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

    @property
    def path(self) -> str:
        """
        Returns path

        Returns:
            str: path (file or directory)
        """
        return os.path.normpath(self._path)

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
        return os.getgid(self._path)
    
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

    def owner(self) -> str:
        """
        Returns the owner name of the Path

        Returns:
            str: owner of the file
        """
        return pwd.getpwuid(self.uid()).pw_name

    def group(self) -> str:
        """
        Returns the group name of the Path
        Returns:
            str: group of the file
        """
        return grp.getgrgid(self.gid()).gr_name

    def others(self, rep='str') -> str:
        """
        Return the others permission number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: others permission number
        """
        mode =str(self.perms('oct'))
        res = mode[-1]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def group(self, rep='str') -> str:
        """
        Return the group permission number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: group permission number
        """
        mode =str(self.perms('oct'))
        res = mode[-2]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def user(self, rep='str') -> str:
        """
        Return the user permission number

        Args:
            rep (str, optional): representation of the permissions. Defaults to'str'. can be 'oct' or 'str'.

        Returns:
            str: user permission number
        """
        mode =str(self.perms('oct'))
        res = mode[-3]
        perms = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'} 
        if rep == 'str':
            return perms[res]
        else:
            return res

    def isreadable(self)-> bool:
        """
        Is the file readable

        Returns:
            bool: True if the file is readable, False otherwise
        
        """
        return os.access(self.filepath, os.R_OK)
    
    def iswritable(self)-> bool:
        """
        Is the file writable

        Returns:
            bool: True if the file is read write, False otherwise
        """
        return os.access(self.filepath, os.W_OK)

    def isexecutable(self)-> bool:
        """
        Is the file executable

        Returns:
            bool: True if the file is executable, False otherwise
        """
        return os.access(self.filepath, os.X_OK)
    
    def isreadonly(self)-> bool:
        """
        Is the file readable only

        Returns:
            bool: True if the file is readable only, False otherwise
        """
        readable = self.isreadable()
        writeable = self.iswritable()
        executable = self.isexecutable()
        if readable and not writeable and not executable:
            return True
        else:
            return False

    def isreadwrite(self)-> bool:
        """
        Is the file readable and writeable

        Returns:
            bool: True if the file is readble and writeable only, False otherwise
        """
        readable = self.isreadable()
        writeable = self.iswritable()
        executable = self.isexecutable()
        if (readable and writeable) and not executable:
            return True
        else:
            return False

    def isreadexec(self)-> bool:
        """
        Is the file readable and executable

        Returns:
            bool: True if the file is readable and executable only, False otherwise
        """
        readable = self.isreadable()
        writeable = self.iswritable()
        executable = self.isexecutable()
        if (readable and executable) and not writeable:
            return True
        else:
            return False

    def isreadwriteexec(self)-> bool:
        """
        Is the file readable and writeable and executable

        Returns:
            bool: True if the file is readable and writeable and executable only, False otherwise
        """
        readable = self.isreadable()
        writeable = self.iswritable()
        executable = self.isexecutable()
        if readable and writeable and executable:
            return True
        else:
            return False

if __name__ == '__main__':
    f = PathPerms('/tmp/testfile.txt')
    print(f.perms())
    print(f.user())
    print(f.group())
    print(f.others())
    f = PathPerms('/tmp')
    print(f.perms())
    print(f.user())
    print(f.group())
    print(f.others())
    print(f.gid)
    print(f.uid)

