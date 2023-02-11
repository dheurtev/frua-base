"""
ZIP file manipulation (zip/unzip)

Provided with a CLI, this module can be used to manipulate zip files.

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- zipfile: https://docs.python.org/3/library/zipfile.html
- argparse: https://docs.python.org/3/library/argparse.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import zipfile
import argparse

class Zip(object):
    """"
    ZIP file manipulation (zip/unzip)
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
        if not hasattr(self, '_logger'):
            self._logger = logging.getLogger(__name__)


    def _zipdir(self, path:str, ziph:zipfile.ZipFile) -> None:
        """
        ziph is zipfile handle. It supports compression.
        
        Args:
            path (str): path to the directory to zip
            ziph (zipfile.ZipFile): zipfile handle

        Inspiration source: https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
        """
        #zip the directory
        for root, dirs, files in os.walk(path):
            for file in files:                
                ziph.write(os.path.join(root, file), 
                        os.path.relpath(os.path.join(root, file), 
                                        os.path.join(path, '..')))
                if hasattr(self, '_logger'):
                   self._logger.debug("Done adding file %s", os.path.join(root, file))
            if hasattr(self, '_logger'):
                self._logger.debug("Done adding directory %s", os.path.join(root))
            
    def zip(self, dir:str, zip_file:str, compression_algorithm:int=zipfile.ZIP_DEFLATED) -> bool:
        """
        zips a directory

        Args:
            dir (str): path to the directory to zip
            zip_file (str): path to zip file
            compression_algorithm (int): compression algorithm to use

        Returns:
            bool: True if zipping was successful, False otherwise
        """
        if hasattr(self, '_logger'):
            self._logger.info("Starting to zip dir: %s", dir)
        #start to zip
        try:
            #create the folder if it does not exist
            if not os.path.exists(dir):
                os.makedirs(dir, exist_ok=True)
                if hasattr(self, '_logger'):
                    self._logger.debug("Created dir: %s", dir)
            #zip the directory
            with zipfile.ZipFile(zip_file, 'w', compression_algorithm, strict_timestamps=False) as zipf:
                self._zipdir(dir, zipf)
            zipf.close()
            #Done, log
            if hasattr(self, '_logger'):
                self._logger.info("Done zipping dir: %s", dir)
            return True      
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error("Failed to zip dir: %s", dir)
                self._logger.error(e)
            return False

    def unzip(self, zip_file:str, dir:str) -> bool:
        """
        unzips a zip file

        Args:
        zip_file (str): path to zip file
        dir (str): directory path to unzip to

        Returns:
            bool: True if unzipping was successful
        """
        if hasattr(self, '_logger'):
            self._logger.info("Starting to unzip file: %s", zip_file)
        #start to unzip
        try:
            #create the folder if it does not exist
            if not os.path.exists(dir):
                os.makedirs(dir, exist_ok=True)
                if hasattr(self, '_logger'):
                    self._logger.debug("Created dir: %s", dir)
            #unzip
            zip_ref = zipfile.ZipFile(zip_file, 'r')
            zip_ref.extractall(dir)
            zip_ref.close()
            #Done, log
            if hasattr(self, '_logger'):
                self._logger.info("Done unzipping file: %s", zip_file)
            return True
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error("Failed to unzip file: %s", zip_file)
                self._logger.error(e)
            return False

if __name__ == '__main__':
    #create the command line parser
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
                    prog = 'ZIP/UNZIP Utility',
                    description = 'ZIP/UNZIP a folder to/from a ZIP file',
                    epilog = 'MIT Licensed',)
    parser.add_argument('command', help='zip or unzip', choices=['zip', 'unzip'])
    parser.add_argument('dir', help='path to unzip to or from')
    parser.add_argument('zip_file', help='path to zip file')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    #parse the command line arguments
    args = parser.parse_args()
    #logic
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    zip = Zip()
    if args.command.lower() == 'zip':
        if not args.verbose:
            print("Starting to zip dir: %s to file %s"%(args.dir, args.zip_file))
        status = zip.zip(args.dir, args.zip_file)
        if status:
            if not args.verbose:
                print("Done zipping dir: %s to file %s"%(args.dir, args.zip_file))
        else:
            if not args.verbose:
                print("Failed to zip dir: %s to file %s"%(args.dir, args.zip_file))
    elif args.command.lower() == 'unzip':
        if not args.verbose:
            print("Starting to unzip file: %s to dir %s"%(args.zip_file, args.dir))
        status = zip.unzip(args.zip_file, args.dir)
        if status:
            if not args.verbose:
                print("Done unzipping file: %s to dir %s"%(args.zip_file, args.dir))
        else:
            if not args.verbose:
                print("Failed to unzip file: %s to dir %s"%(args.zip_file, args.dir))
    else:
        print("Command not recognized. Must be zip or unzip")

