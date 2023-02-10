"""
tests frua.base.archive.zip.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os
from pathlib import Path

from frua.base.archive.zip import Zip
from frua.base.fs.dirs import Dirs

@pytest.fixture
def zipobj():
    zipobj = Zip()
    return zipobj

def test_init(zipobj):
    assert isinstance(zipobj, Zip)
    assert hasattr(zipobj, '_logger')

def test_zip_unzip_cycle(zipobj):
    #create a temporary directory
    path1 = '/tmp/testzip'
    if not os.path.exists(path1):
        os.mkdir(path1)
    #create a file in the temporary directory
    file1 = '/tmp/testzip/test1.txt'
    Path(file1).touch()
    #create a subdirectory in the temporary directory
    path2 = '/tmp/testzip/test2'
    if not os.path.exists(path2):
        os.mkdir(path2)
    #create a file in the subdirectory
    file2 = '/tmp/testzip/test2/test3.txt'
    Path(file2).touch()
    #set source
    srctozip = '/tmp/testzip'
    #set zipfile
    zipfilepath = '/tmp/test.zip'
    #perform the zip
    zipobj.zip(srctozip, zipfilepath)
    #decide where to unzip
    dst = '/tmp/test1'
    #unzip
    zipobj.unzip(zipfilepath, dst)
    #perform the tests
    assert os.path.exists(os.path.join(dst, 'testzip', 'test1.txt'))
    assert os.path.exists(os.path.join(dst, 'testzip', 'test2'))
    assert os.path.exists(os.path.join(dst, 'testzip', 'test2', 'test3.txt'))
    #Create a dirs object
    d = Dirs()
    #remove the output directory
    if os.path.exists(dst):
        d.wipedir(dst)
    #remove the temporary directory
    if os.path.exists(path1):
        d.wipedir(path1)
    #remove the zipfile
    if os.path.exists(zipfilepath):
        os.remove(zipfilepath)

