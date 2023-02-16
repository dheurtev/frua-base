"""
tests frua.base.code.git.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os

from frua.base.code.git import *
from frua.base.fs.dir import Dir

@pytest.fixture
def gitobj():
    gitobj = Git()
    return gitobj

@pytest.fixture
def ghobj():
    ghobj = GitHub()
    return ghobj

# test Git

def test_init(gitobj):
    assert isinstance(gitobj, Git)

def test_git_clone_https(gitobj):
    url = 'https://github.com/dheurtev/testrepo.git'
    outputdir = '/tmp/testrepo'
    #setup
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)
    #create
    branch = 'test'
    gitobj.clone_https(url, outputdir, branch, overwrite=True) 
    #test
    assert os.path.exists(outputdir)
    #teadown
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)

# Test Github

def test_init_gh(ghobj):
    assert isinstance(ghobj, GitHub)

def test_github_repo_name(ghobj):
    name = 'dheurtev'
    ghobj.user = name
    assert ghobj._user == name

def test_github_repo(ghobj):
    repo = 'testrepo'
    ghobj.repo = repo
    assert ghobj._repo == repo

def test_github_branch(ghobj):
    branch = 'test'
    ghobj.branch = branch
    assert ghobj._branch == branch

def test_github_release(ghobj):
    version = '1.0.0'
    ghobj.release = version
    assert ghobj._release == version

def test_github_repo_url(ghobj):
    name = 'dheurtev'
    ghobj.user = name
    repo = 'testrepo'
    ghobj.repo = repo 
    url = ghobj.repo_url
    assert url == 'https://github.com/dheurtev/testrepo.git'

def test_github_repo_branch_zip_url(ghobj):
    name = 'dheurtev'
    ghobj.user = name
    repo = 'testrepo'
    ghobj.repo = repo 
    branch = 'test'
    ghobj.branch = branch
    url = ghobj.repo_branch_zip_url
    assert url == 'https://github.com/dheurtev/testrepo/archive/test.zip'

def test_github_clone_https(ghobj):
    outputdir = '/tmp/testrepo'
    #setup
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)
    #create
    name = 'dheurtev'
    ghobj.user = name
    repo = 'testrepo'
    ghobj.repo = repo 
    branch = 'test'
    ghobj.branch = branch
    ghobj.clone_https_gh(outputdir=outputdir, overwrite=True) 
    #test
    assert os.path.exists(outputdir)
    #teadown
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)

def test_github_clone_from_zip(ghobj):
    outputdir = '/tmp/testrepo'
    #setup
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)
    #create
    name = 'dheurtev'
    ghobj.user = name
    repo = 'testrepo'
    ghobj.repo = repo 
    branch = 'test'
    ghobj.branch = branch
    ghobj.clone_from_zip(outputdir=outputdir, overwrite=True) 
    #test
    assert os.path.exists(outputdir)
    #teadown
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)

def test_github_clone_release_from_zip(ghobj):
    outputdir = '/tmp/testrepo'
    #setup
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)
    #create
    name = 'dheurtev'
    ghobj.user = name
    repo = 'cryptopyutils'
    ghobj.repo = repo 
    release = '0.1.0'
    ghobj.release = release
    ghobj.clone_release_from_zip(outputdir=outputdir, overwrite=True) 
    #test
    assert os.path.exists(outputdir)
    #teadown
    if os.path.exists(outputdir):
        Dir().wipe(outputdir)
