""""
pyinfra_plugins: file downloader
"""
__author__ = "David HEURTEVENT"
__copyright__ = "David HEURTEVENT"
__license__ = "MIT"

#Setup logger
import logging
import os
import requests
import subprocess
  
    def download_github_zip(self, userandrepo, branch="master", file_name=None, file_dir='.', overwrite=False):
        """
        Download a zip file from github

        Args:
            url (str): the url to download
            file_name (str): the name of the file to save
            file_dir (str): the directory to save the file to
            overwrite (bool): whether to overwrite an existing file

        Returns:
            bool: True if successful, False otherwise
        """
        self._logger.info("Downloading from %s" % userandrepo)
        #pick the file name
        if not file_name:
            file_name = "%s.zip"%(branch)
        # pick and create the directory
        if not file_dir:
            file_dir = os.path.dirname(file_name)
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
                self._logger.info("Created directory %s" % file_dir)
                self._logger.info("Created file %s" % file_name)
            else:
                self._logger.info("Directory %s already exists" % file_dir)
                self._logger.info("File %s already exists" % file_name)
        # compute the file path
        file_path = os.path.join(file_dir, file_name)
        # generate the url
        url = "https://github.com/%s/archive/%s.zip"%(userandrepo, branch)
        # download the file
        if not os.path.exists(file_path) or overwrite:
            self._logger.info("Downloading url %s. Will be saved to %s" % (url, file_path))
            r = requests.get(url, stream=True)
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                    else:
                        break
                    self._logger.info("Downloaded %s and saved to %s" % (url, file_path))
                return True
        else:
            self._logger.info("File %s already exists in %s" % (file_name, file_dir))
            return False

    def git_clone(self, repourl, directory=None, branch=None, overwrite=True):
        """
        Clone a git repository

        Args:
            reporurl (str): the repourl to download 
            directory (str): the directory to save the file to (optional)
            branch (str): the branch to clone (optional)
            overwrite (bool): whether to overwrite an existing file
        Returns:
            bool: True if successful, False otherwise
        """
        self._logger.info("Cloning from %s" % repourl)
        #Create the list of arguments
        args = list(['git'])
        args.append("clone")
        if branch:
            args.append("--branch")
            args.append(branch)
        args.append(repourl)
        if directory:
            args.append(directory)
            if not os.path.exists(directory):
                os.makedirs(directory)
                self._logger.info("Created directory %s" % directory)
            else:
                self._logger.info("Directory %s already exists" % directory)

        # Clone the repository
        pipe = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        pipe.wait()
        if pipe.returncode == 0:
            self._logger.info("Cloned from %s" % repourl)
            return True
        else:
            self._logger.error("Failed to clone from %s" % repourl)
            return False
        
if __name__ == "__main__":
    u = "https://google.com"
    f = FileDownloader()
    #f.download_web(url=u)
    #f.download_web(url=u, file_name="test.txt")
    #f.download_web(url=u, file_name="test.txt", file_dir="/tmp")
    #f.download_web(url=u, file_name="test.txt", overwrite=True)
    #f.download_github_zip(userandrepo="JadedTuna/gitrepo", branch="master", file_dir="/tmp")
    f.git_clone(repourl="https://github.com/libgit2/libgit2")

