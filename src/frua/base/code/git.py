"""
Git Helper

Tool to clone and deploy git repositories with or without git installed on your machine (clones repos, branches or releases)

Uses:
- os: https://docs.python.org/3/library/os.html
- logging: https://docs.python.org/3/library/logging.html
- subprocess: https://docs.python.org/3/library/subprocess.html
- shutil: https://docs.python.org/3/library/shutil.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import os
import logging
import subprocess
import shutil

from frua.base.http.getdownloader import GetDownloader
from frua.base.archive.zip import Zip

GITHUB_URL="https://github.com"

class Git(object):
    """
    Git helper

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
        super(Git, self).__init__(*args, **kwargs)
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)    

    def clone_https(self, repourl:str, outputdir:str=None, branch:str=None, overwrite:bool=True) -> None:
        """
        Clone a git repository using https

        Uses subprocess to clone the git repository indicated in the repourl.
        Git must be installed on your system for it to work.

        Args:
            reporurl (str): the repourl to download 
            outputdir (str): the directory to save the file to (optional)
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
        if outputdir:
            args.append(outputdir)
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
                self._logger.info("Created directory %s" % outputdir)
            else:
                self._logger.info("Directory %s already exists" % outputdir)

        # Clone the repository
        pipe = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        pipe.wait()
        if pipe.returncode == 0:
            self._logger.info("Cloned from %s" % repourl)
            return True
        else:
            self._logger.error("Failed to clone from %s" % repourl)
            return False

class GitHub(Git):
    """
    GitHub Helper
    """
    def __init__(self, user:str=None, repo:str=None, branch:str='main', release:str=None, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            user (str): the github user name
            repo (str): the repository name
            branch (str, optional): the branch name. Defaults to 'main'.
            release (str, optional): the release name. Defaults to None.
            logger (logging.Logger): the logger to use (optional)
            args: positional arguments
            kwargs: keyword arguments
        """
        super(GitHub, self).__init__(*args, **kwargs)
        #handle other args
        if user is not None:
            self._user = user
        if repo is not None:
            self._repo = repo
        if branch is not None:
            self._branch = branch
        if release is not None:
            self._release = release
    
    @property
    def user(self) -> str:
        """
        Returns the user name
        """
        return self._user
    
    @user.setter
    def user(self, user:str) -> None:
        """
        Sets the user name

        Args:
            user (str): the github user name
        """
        self._user = user

    @property
    def repo(self) -> str:
        """
        Returns the repository name
        """
        return self._repo

    @repo.setter
    def repo(self, repo:str) -> None:
        """
        Sets the repository name

        Args:
            repo (str): the repository name
        """
        self._repo = repo
    
    @property
    def branch(self) -> str:
        """
        Returns the branch name
        """
        return self._branch

    @branch.setter
    def branch(self, branch:str) -> None:
        """
        Sets the branch name

        Args:
            branch (str): the branch name
        """
        self._branch = branch

    @property
    def release(self) -> str:
        """
        Returns the release name
        """
        return self._release

    @release.setter
    def release(self, release:str) -> None:
        """
        Sets the release name (e.g. 0.0.1)

        Args:
            release (str): the release name
        """
        self._release = release

    @property
    def repo_url(self) -> str:
        """
        Returns the repo url on github for username and repo name

        Returns:
            str: the link on github for the given user name and repo name
        """
        return "%s/%s/%s.git"%(GITHUB_URL, self._user, self._repo)

    @property
    def repo_branch_zip_url(self) -> str:
        """
        Returns the url to the zip file of a repo on github for username, repo name and branch name
        Returns:
            str: the link on github to the zip file for the given user name and repo name and branch name (optional)
        """
        return "%s/%s/%s/archive/%s.zip"%(GITHUB_URL, self._user, self._repo, self._branch)

    @property
    def release_zip_url(self) -> str:
        """
        Returns the url to the zip file for a specific release of a repo on github for a given username, repo name, and release name
        """
        return "%s/%s/%s/archive/refs/tags/v%s.zip"%(GITHUB_URL, self._user, self._repo, self._release)

    def clone_https_gh(self, outputdir:str=None, overwrite:bool=True) -> bool:
        """
        Clone a github repository using https

        git must be installed in your system

        Args:
            outputdir (str): the directory to save the file to (optional)
            overwrite (bool): whether to overwrite an existing file
        Returns:
            bool: True if successful, False otherwise
        """
        if self.user is None or self.repo is None:
            self._logger.error("User and repo must be set")
            return False
        #compute the url
        url = self.repo_url
        #clone
        return self.clone_https(url, outputdir=outputdir, branch=self._branch, overwrite=overwrite)
    
    def clone_from_zip(self, outputdir:str=None, overwrite:bool=True) -> bool:
        """
        Clone a github repository by using https and the branch zip file and unziping it to the output directory

        Does not require git to be installed on your system

        Args:
            outputdir (str): the directory to save the file to (optional)
            overwrite (bool): whether to overwrite an existing file
        Returns:
            bool: True if successful, False otherwise
        """
        if self.user is None or self.repo is None:
            self._logger.error("User and repo must be set")
            return False
        if self.release is None:
            self._logger.error("Release must be set")
            return False
        #compute the url
        url = self.repo_branch_zip_url
        userandrepo = '%s/%s'%(self.user, self.repo)
        repobranch = '%s-%s'%(self.repo, self.branch)
        file_name = '%s.zip'%(repobranch)
        #download the zip archive to the temporary folder
        self._logger.info("Downloading from %s" % userandrepo)
        tempdir = '/tmp'
        try:
            g = GetDownloader(url=url, file_name=file_name, file_dir=tempdir)
            g.download(overwrite=overwrite)
        except Exception as e:
            self._logger.error("Failed to download from %s" % url)
            self._logger.error(e)
            return False
        #unzip the archive to the output directory
        self._logger.info("Unziping from %s to %s" % (file_name, outputdir))
        try:
            z = Zip()
            z.unzip(os.path.join(tempdir, file_name), tempdir)
        except Exception as e:
            self._logger.error("Failed to unzip %s to %s" % (file_name, tempdir))
            self._logger.error(e)
            return False
        #move the content to the output destination
        src = os.path.join(tempdir, repobranch)
        dst = os.path.join(outputdir)
        self._logger.info("Moving %s to %s" % (src, dst))
        try:
            shutil.move(src, dst)
        except Exception as e:
            self._logger.error("Failed to move %s to %s" % src, dst)
            self._logger.error(e)
            return False
        #delete the zip from the temporary folder
        if os.path.exists(os.path.join(tempdir, file_name)):
            os.remove(os.path.join(tempdir, file_name))
        return True        

    def clone_release_from_zip(self, outputdir:str=None, overwrite:bool=True) -> bool:
        """
        Clone a github repository by using https and the release zip file and unziping it to the output directory

        Does not require git to be installed on your system

        Args:
            outputdir (str): the directory to save the file to (optional)
            overwrite (bool): whether to overwrite an existing file
        Returns:
            bool: True if successful, False otherwise
        """
        if self.user is None or self.repo is None:
            self._logger.error("User and repo must be set")
            return False
        if self.branch is None:
            self._logger.error("Branch must be set")
            return False
        #compute the url
        url = self.release_zip_url
        userandrepo = '%s/%s'%(self.user, self.repo)
        reporelease = '%s-%s'%(self.repo, self.release)
        file_name = 'v%s.zip'%(self.release)
        #download the zip archive to the temporary folder
        self._logger.info("Downloading release %s from %s" % (self.release, userandrepo))
        tempdir = '/tmp'
        try:
            g = GetDownloader(url=url, file_name=file_name, file_dir=tempdir)
            g.download(overwrite=overwrite)
        except Exception as e:
            self._logger.error("Failed to download from %s" % url)
            self._logger.error(e)
            return False
        #unzip the archive to the output directory
        self._logger.info("Unziping from %s to %s" % (file_name, outputdir))
        try:
            z = Zip()
            z.unzip(os.path.join(tempdir, file_name), tempdir)
        except Exception as e:
            self._logger.error("Failed to unzip %s to %s" % (file_name, tempdir))
            self._logger.error(e)
            return False
        #move the content to the output destination
        src = os.path.join(tempdir, reporelease)
        dst = os.path.join(outputdir)
        self._logger.info("Moving %s to %s" % (src, dst))
        try:
            shutil.move(src, dst)
        except Exception as e:
            self._logger.error("Failed to move %s to %s" % src, dst)
            self._logger.error(e)
            return False
        #delete the zip from the temporary folder
        if os.path.exists(os.path.join(tempdir, file_name)):
            os.remove(os.path.join(tempdir, file_name))
        return True        



