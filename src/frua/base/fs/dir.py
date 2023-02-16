"""
Directory manipulation with logger

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging

class Dir(object):
    """"
    Directory manipulation 
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

    def subfolders(self, dir:str=None) -> list:
        """
        List all subfolders of the directory

        Args:
            dir: Directory to be listed
        Returns:
            list: list of subfolders
        """
        subdirs = [os.path.join(dir, o) for o in os.listdir(dir) if os.path.isdir(os.path.join(dir,o))]
        print(subdirs)
        return subdirs

    def wipe(self, dir:str=None, wipesys:bool=False) -> None:
        """
        Wipes a directory (equivalent rm -rf dir)

        By default, it refuses to wipe system folders :
        / /boot /proc /dev /lib /mnt /run /sbin /srv /sys /lost+found
        
        To wipe system directories, set wipesys=True

        Args:
            dir: Directory to be nuked
            wipesys: wipe the directory (default: False)        
        """
        #set the path
        if self.path == None and dir == None:
            if hasattr(self, '_logger'):
                self._logger.error("No path to wipe")
            else:
                print("No path to wipe")
            return
        if dir == None:
            dir = self._path
        else:
            self._path = dir
        #set the logger
        if hasattr(self, '_logger'):
            self._logger.debug("Starting to wipe dir: %s", dir)
        #refuses to nuke system folders
        if not wipesys:
            if str(dir).strip() in ['/','/boot','/proc','/dev','/lib','/mnt','/run','/sbin','/srv','/sys','/lost+found']:
                if hasattr(self, '_logger'):
                    self._logger.debug("Refusing to wipe system dir: %s", dir)
                else:
                    print("Refusing to wipe system dir: %s", dir)
                return
        #nuking
        try:
            if os.path.isdir(dir):
                if dir[-1] == os.sep: dir = dir[:-1]
                files = os.listdir(dir)
                for file in files:
                    if file == '.' or file == '..': continue
                    path = dir + os.sep + file
                    if os.path.isdir(path):
                        #wipe sub-directory
                        self.wipe(path, wipesys=wipesys)
                        if hasattr(self, '_logger'):
                            self._logger.debug("wiped dir: %s", path)
                    else:
                        try:
                            #remove the file
                            os.unlink(path)
                            if hasattr(self, '_logger'):
                                self._logger.debug("wiped file: %s", path)
                        except Exception as e:
                            if hasattr(self, '_logger'):
                                self._logger.error("Failed to wipe file: %s", path)
                                self._logger.error(e)
                try:
                    #remove the directory
                    os.rmdir(dir)
                except Exception as e:
                    if hasattr(self, '_logger'):
                        self._logger.error("Failed to wipe dir: %s", dir)
                        self._logger.error(e)
                if hasattr(self, '_logger'):
                    self._logger.debug("removed dir: %s", dir)
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error("Failed to wipe dir: %s", dir)
                self._logger.error(e)
        if hasattr(self, '_logger'):
            self._logger.info("Done wiping dir: %s", dir)

