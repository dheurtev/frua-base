"""
TAR file manipulation (tar/untar)

Provided with a CLI, this module can be used to manipulate tar files.

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- tarfile: https://docs.python.org/3/library/tarfile.html
- argparse: https://docs.python.org/3/library/argparse.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import tarfile
import argparse

class Tar:
    """
    TAR file manipulation (tar/untar)
    """

    def __init__(self, *args, **kwargs) -> None:
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
    
    
    def tar(self, dir:str, tar_file:str, fmt:str=None) -> bool:
        """
        tar a directory

        Args:
        dir (str): path to directory
        tar_file (str): path to tar file
        fmt (str): compression format (gz, bz2, xz, None)

        Returns:
            bool: True if tarping was successful
        """
        if hasattr(self, '_logger'):
            self._logger.debug("Starting to tar dir: %s", dir)
        try:
            #create the folder if it does not exist
            if not os.path.exists(dir):
                os.makedirs(dir)
                if hasattr(self, '_logger'):
                    self._logger.debug("Created dir: %s", dir)
            #open the tar file
            if fmt:
                tar_ref = tarfile.open(tar_file, 'w:%s'%fmt)
            else:
                tar_ref = tarfile.open(tar_file, 'w')
            #add the directory  to the tar file
            tar_ref.add(dir)
            #close the tar file
            tar_ref.close()
            #Done, log
            if hasattr(self, '_logger'):
                self._logger.info("Done taring dir: %s", dir)
            return True
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error("Failed to tar dir: %s", dir)
                self._logger.error(e)
            return False
    
    def untar(self, tar_file:str, dir:str, fmt:str=None) -> bool:
        """
        untar a directory

        Args:
        dir (str): path to directory
        tar_file (str): path to tar file
        fmt (str): compression format (gz, bz2, xz, None)

        Returns:
            bool: True if untaring was successful
        """
        if hasattr(self, '_logger'):
            self._logger.debug("Starting to untar dir: %s", dir)
        #start untar
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
                if hasattr(self, '_logger'):
                    self._logger.debug("Created dir: %s", dir)
            #open the tar file
            if fmt:
                tar_ref = tarfile.open(tar_file, 'r:%s'%fmt)
            else:
                tar_ref = tarfile.open(tar_file, 'r')
            #extract the directory
            tar_ref.extractall(dir)
            #close the tar file
            tar_ref.close()
            #Done, log
            if hasattr(self, '_logger'):
                self._logger.info("Done untaring dir: %s", dir)
            return True
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error("Failed to untar dir: %s", dir)
                self._logger.error(e)
            return False

if __name__ == '__main__':
    #create the command line parser
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
                    prog = 'TAR/UNTAR Utility',
                    description = 'TAR/UNTAR a folder to/from a TAR file.\
                    By default, it does not use compression.',
                    epilog = 'MIT Licensed',)
    parser.add_argument('command', help='tar or untar', choices=['tar', 'untar'])
    parser.add_argument('dir', help='path to untar to or from')
    parser.add_argument('tar_file', help='path to tar file')
    parser.add_argument('-c', '--compression', choices=['gz', 'bz2', 'xz'], default=None)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    #parse the command line arguments
    args = parser.parse_args()
    #logic
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    tar = Tar()
    if args.command.lower() == 'tar':
        if not args.verbose:
            print("Starting to tar dir: %s to file %s"%(args.dir, args.tar_file))
        status = tar.tar(args.dir, args.tar_file, args.compression)
        if status:
            if not args.verbose:
                print("Done doing tar with dir: %s to file %s"%(args.dir, args.tar_file))
        else:
            if not args.verbose:
                print("Failed to tar dir: %s to file %s"%(args.dir, args.tar_file))
    elif args.command.lower() == 'untar':
        if not args.verbose:
            print("Starting to untar file: %s to dir %s"%(args.tar_file, args.dir))
        status = tar.untar(args.tar_file, args.dir, args.compression)
        if status:
            if not args.verbose:
                print("Done doing untar with file: %s to dir %s"%(args.tar_file, args.dir))
        else:
            if not args.verbose:
                print("Failed to unzip file: %s to dir %s"%(args.tar_file, args.dir))
    else:
        print("Command not recognized. Must be tar or untar")


