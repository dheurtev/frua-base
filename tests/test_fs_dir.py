"""
tests frua.base.fs.dir.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging
import os

from frua.base.fs.dir import Dir

#Test Wipe

@pytest.fixture
def dirobj():
    obj = Dir()
    return obj

def test_subfolders(dirobj):
    path = '/tmp'
    subs = dirobj.subfolders(path)
    assert len(subs) > 0

def test_files(dirobj):
    path = '/etc'
    files = dirobj.files(path)
    assert len(files) > 0

def test_wipe_with_empty_dir(dirobj):
    #setup
    ##create the test directory
    path = '/tmp/test_wipe'
    if not os.path.exists(path):
        os.makedirs(path)
    #wipe
    dirobj.wipe(path)
    #test
    assert not os.path.exists(dirobj.path)
    assert not os.path.isdir(dirobj.path)    

def test_wipe_with_file(dirobj):
    #setup
    ##create the test directory
    path = '/tmp/test_wipe'
    if not os.path.exists(path):
        os.makedirs(path)
    ##put a test file in the test directory
    with open(os.path.join(path, 'tmp.txt'), 'w') as file: 
        pass    
    #wipe
    dirobj.wipe(path)
    #test
    assert not os.path.exists(dirobj.path)
    assert not os.path.isdir(dirobj.path)

def test_wipe_with_subfolder(dirobj):
    #setup
    ##create the test directory
    path = '/tmp/test_wipe'
    if not os.path.exists(path):
        os.makedirs(path)
    ##put a test file in the test directory
    with open(os.path.join(path, 'tmp.txt'), 'w') as file: 
        pass
    ##put a subfolder in the test directory
    os.makedirs(os.path.join(path, 'tmp2'))
    ##put a test file in the subfolder
    with open(os.path.join(path, 'tmp2', 'tmp.txt'), 'w') as file: 
        pass
    #wipe
    dirobj.wipe(path)
    #test
    assert not os.path.exists(dirobj.path)
    assert not os.path.isdir(dirobj.path)    

def test_wipe_non_existing_dir(dirobj):
    #setup
    path = '/tmp/test_wipe'
    #test non exist
    assert not os.path.exists(path)
    assert not os.path.isdir(path)    
    #wipe
    dirobj.wipe(path)
    #test
    assert not os.path.exists(path)
    assert not os.path.isdir(path)    

