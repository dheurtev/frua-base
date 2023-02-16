"""
File utility : read, write, head, tail, append to bottom, append to top, merge

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging

class File(object):
    """
    File utility class
    
    File utility : head, tail, append to bottom, append to top, merge
    """
    def __init__(self, path:str, content:list=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            path (str): the file path
            content (list, optional): The content to append to the file as a list of lines
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
           int:Status: 0 is OK, 1 is dry run, 2 is error
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
        except IOError as e:
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
           int:Status: 0 is OK, 1 is dry run, 2 is error
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
        except IOError as e:
            if hasattr(self, '_logger'):
                self._logger.error('Could not read the file %s'%(self.path))
                self._logger.error(e)
            return 1

    def head(self, n:int=1) -> list:
        """
        Return the first n lines of the file

        Args:
            n (int, optional): the number of lines to return

        Returns:
            list: the first n lines of the file
        """
        try:
            with open(self.path, 'r') as f:
                return f.readlines()[0:n]
            self._logger.debug('File content %s read from %s'%(self.content, self.path))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(self.path))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(self.path))
            return
        except Exception as e:
            self._logger.error("Could not read file: {}".format(self.path))
            self._logger.error(e)
            return
    
    def tail(self, n:int=1) -> list:
        """
        Return the last n lines of the file

        Args:
            n (int, optional): the number of lines to return

        Returns:
            list: the last n lines of the file
        """
        try:
            with open(self.path, 'r') as f:
                return f.readlines()[-n:]
            self._logger.debug('File content %s read from %s'%(self.content, self.path))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(self.path))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(self.path))
            return
        except Exception as e:
            self._logger.error("Could not read file: {}".format(self.path))
            self._logger.error(e)
            return
    
    def append_bottom(self, content:list=None) -> None:
        """
        Append content to the bottom of the file

        Args:
            content (list, optional): the content to append
        """
        #use self.content if not specified
        if content is None:
            content = self.content
        #append to the file
        try:
            with open(self.path, 'a') as f:
                f.writelines(content)
            self._logger.debug('File content %s appended at the bottom of %s'%(self.content, self.path))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(self.path))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(self.path))
            return
        except Exception as e:
            self._logger.error("Could not append to file: {}".format(self.path))
            self._logger.error(e)
            return
    
    def append_top(self, content:list=None) -> None:
        """
        Append content to the top of the file

        Args:
            content (list, optional): the content to append
        """
        #use self.content if not specified
        if content is None:
            content = self.content
        #append to the file
        try:
            #append the content
            data = content
            #read the file existing content
            with open(self.path, 'r') as f:
                data += f.readlines()
            #write the new file
            with open(self.path, 'w') as f:
                f.writelines(data)
            self._logger.debug('File content %s appended at the bottom of %s'%(self.content, self.path))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(self.path))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(self.path))
            return
        except Exception as e:
            self._logger.error("Could not append to file: {}".format(self.path))
            self._logger.error(e)
            return
    
    def merge(self, secondfilepath:str, dst:str, remove_src:bool=False) -> None:
        """
        Merge the file with another file and copy it in the destination path

        Args:
            secondfile (str): the path to the second file
            dst (str): the path to the destination file
            remove_src (bool, optional): if True, remove the source files
        """
        # Reading data from src1
        try:
            with open(self.path) as fp:
                data = fp.read()
            self._logger.debug('File content %s read from %s'%(data, self.path))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(self.path))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(self.path))
            return
        except Exception as e:
            self._logger.error("Could not read file: {}".format(self.path))
            self._logger.error(e)
            return
        # Reading data from src2
        try:
            with open(secondfilepath) as fp:
                data2 = fp.read()
            self._logger.debug('File content %s read from %s'%(data2, secondfilepath))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(secondfilepath))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(secondfilepath))
            return
        except Exception as e:
            self._logger.error("Could not read file: {}".format(secondfilepath))
            self._logger.error(e)
            return
        #Merge the two file
        # from next line
        data += data2
        #Write the output data to the destination file
        try:
            with open (dst, 'w') as fp:
                fp.write(data)
            self._logger.debug('File content %s written to %s'%(data, dst))
        except FileNotFoundError:
            self._logger.error("File not found: {}".format(dst))
            return
        except PermissionError:
            self._logger.error("Permission denied: {}".format(dst))
            return
        except Exception as e:
            self._logger.error("Could not write output to destination file: {}".format(dst))
            self._logger.error(e)
            return
        #remove the source files if specified
        if remove_src:
            try:
                os.remove(self.path)
                self._logger.debug('Removed file %s'%(self.path))
            except FileNotFoundError:
                self._logger.error("File not found: {}".format(self.path))
                return
            except PermissionError:
                self._logger.error("Permission denied: {}".format(self.path))
                return
            except Exception as e:
                self._logger.error("Could not remove source file: {}".format(self.path))
                self._logger.error(e)
                return
            try:
                os.remove(secondfilepath)
                self._logger.debug('Removed file %s'%(secondfilepath))
            except FileNotFoundError:
                self._logger.error("File not found: {}".format(secondfilepath))
                return
            except PermissionError:
                self._logger.error("Permission denied: {}".format(secondfilepath))
                return
            except Exception as e:
                self._logger.error("Could not remove source file: {}".format(secondfilepath))
                self._logger.error(e)
                return

