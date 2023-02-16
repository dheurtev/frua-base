"""
HTTP get downloader

Download web pages or files from the internet with a get download method and save the files to disk (similar to wget) 


Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- requests: https://requests.readthedocs.io/en/latest/

"""
__author__ = "David HEURTEVENT"
__copyright__ = "David HEURTEVENT"
__license__ = "MIT"

import logging
import os
from urllib.parse import urlparse

#external dependencies
import requests


class GetDownloader(object):

    def __init__(self, url:str=None, file_name:str=None, file_dir:str=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            url (str): the url to download
            file_name (str): the filename to save
            file_dir (str): the directory to save the file to
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
        #handle url
        if url != None:
            self._url = url
        else:
            self._url = None
        #handle file_name
        if file_name != None:
            self._file_name = file_name
        else:
            self._file_name = None
        #handle file_dir
        if file_dir != None:
            self._file_dir = file_dir
        else:
            self._file_dir = None

    @property
    def url(self) -> str:
        """
        Returns the url to download

        Returns:
            str: the url to download
        """
        return self._url
    
    @url.setter
    def url(self, url:str) -> None:
        """
        Sets the url to download

        Args:
            url (str): the url to download
        """
        self._url = url

    @property
    def file_name(self) -> str:
        """
        Returns the filename to save

        Returns:
            str: the filename to save
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self, file_name:str) -> None:
        """
        Set the filename

        Args:
            file_name (str): the filename to save
        """
        self._file_name = file_name
    
    @property
    def file_dir(self) -> str:
        """
        Returns the directory to save the file to

        Returns:
            str: the directory to save the file to
        """
        return self._file_dir

    @file_dir.setter
    def file_dir(self, file_dir:str) -> None:
        """
        Set the directory to save the file to

        Args:
            file_dir (str): the directory to save the file to
        """
        self._file_dir = file_dir

    def download(self, overwrite=False):
        """
        Download a file from the internet.

        Saved by default to the current directory.

        Args:
            overwrite (bool): whether to overwrite an existing file

        Returns:
            bool: True if successful, False otherwise

        """
        # Check url is set
        if self.url == None:
            self._logger.error("You must set the url")
            return False
        # Set the filename if not set
        if self.file_name is None:
            file_name = self.url.split('/')[-1]
            file_name = file_name.split('?')[0]
            file_name = file_name.split('#')[0]
            file_name = file_name.split('&')[0]
            file_name = file_name.split('=')[0]
            self.file_name = file_name
            #case empty file name
            if self.file_name == '' or self.file_name is None:         
                domain = urlparse(self._url).netloc
                self.file_name = domain
        # Set the file_dir
        if self.file_dir is None:
            self.file_dir = os.path.dirname(os.getcwd())
            if not os.path.exists(self.file_dir):
                os.makedirs(self.file_dir)
                self._logger.info("Created directory %s" % self.file_dir)
        # Compute the output file path
        file_path = os.path.normpath(os.path.join(self.file_dir, self.file_name))
        #Check if file already exists if not allowed to overwrite
        if not overwrite and os.path.exists(file_path):
            self._logger.error("File %s already exists" % file_path)
            return False
        # start downloading the file
        if not os.path.exists(file_path) or overwrite:
            self._logger.info("Downloading url %s."% self.url)
            self._logger.info("Url will be saved to %s" % file_path)
            #download the file
            r = requests.get(self.url, stream=True)
            r.raise_for_status()
            #write the output
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                    else:
                        break
                    self._logger.info("Downloaded %s and saved to %s" % (self.url, file_path))
                return True
        else:
            self._logger.info("File %s already exists in %s" % (self.file_name, self.file_dir))
            return False