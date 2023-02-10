"""
tests frua.base.archive.tar.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os
from pathlib import Path

from frua.base.archive.tar import Tar
from frua.base.fs.dirs import Dirs

@pytest.fixture
def tarobj():
    tarobj = Tar()
    return tarobj

def test_init(tarobj):
    assert isinstance(tarobj, Tar)
    assert hasattr(tarobj, '_logger')

def test_tar_untar_cycle(tarobj):
    #create a temporary directory
    path1 = '/tmp/testtar'
    if not os.path.exists(path1):
        os.mkdir(path1)
    #create a file in the temporary directory
    file1 = '/tmp/testtar/test1.txt'
    Path(file1).touch()
    #create a subdirectory in the temporary directory
    path2 = '/tmp/testtar/test2'
    if not os.path.exists(path2):
        os.mkdir(path2)
    #create a file in the subdirectory
    file2 = '/tmp/testtar/test2/test3.txt'
    Path(file2).touch()
    #set source
    srctotar = '/tmp/testtar'
    #set tarfile
    tarfilepath = '/tmp/test.tar'
    #perform the tar
    tarobj.tar(srctotar, tarfilepath)
    #decide where to untar
    dst = '/tmp/test1'
    #untar
    tarobj.untar(tarfilepath, dst)
    #perform the tests
    print(dst)
    assert os.path.exists(os.path.join(dst, 'tmp', 'testtar', 'test1.txt'))
    assert os.path.exists(os.path.join(dst, 'tmp', 'testtar', 'test2'))
    assert os.path.exists(os.path.join(dst, 'tmp','testtar', 'test2', 'test3.txt'))
    #Create a dirs object
    d = Dirs()
    #remove the output directory
    if os.path.exists(dst):
        d.wipedir(dst)
    #remove the temporary directory
    if os.path.exists(path1):
        d.wipedir(path1)
    #remove the tarfile
    if os.path.exists(tarfilepath):
        os.remove(tarfilepath)

def test_tar_untar_cycle_gz(tarobj):
    #create a temporary directory
    path1 = '/tmp/testtar'
    if not os.path.exists(path1):
        os.mkdir(path1)
    #create a file in the temporary directory
    file1 = '/tmp/testtar/test1.txt'
    Path(file1).touch()
    #create a subdirectory in the temporary directory
    path2 = '/tmp/testtar/test2'
    if not os.path.exists(path2):
        os.mkdir(path2)
    #create a file in the subdirectory
    file2 = '/tmp/testtar/test2/test3.txt'
    Path(file2).touch()
    #set source
    srctotar = '/tmp/testtar'
    #set tarfile
    tarfilepath = '/tmp/test.tar.gz'
    #perform the tar
    tarobj.tar(srctotar, tarfilepath, fmt='gz')
    #decide where to untar
    dst = '/tmp/test1'
    #untar
    tarobj.untar(tarfilepath, dst, fmt='gz')
    #perform the tests
    print(dst)
    assert os.path.exists(os.path.join(dst, 'tmp', 'testtar', 'test1.txt'))
    assert os.path.exists(os.path.join(dst, 'tmp', 'testtar', 'test2'))
    assert os.path.exists(os.path.join(dst, 'tmp','testtar', 'test2', 'test3.txt'))
    #Create a dirs object
    d = Dirs()
    #remove the output directory
    if os.path.exists(dst):
        d.wipedir(dst)
    #remove the temporary directory
    if os.path.exists(path1):
        d.wipedir(path1)
    #remove the tarfile
    if os.path.exists(tarfilepath):
        os.remove(tarfilepath)

