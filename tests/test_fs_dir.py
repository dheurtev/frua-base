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

def test_copy(dirobj):
    #setup
    src = '/tmp/test_copy'
    dst = '/tmp/test_copy2'
    #wipe
    dirobj.wipe(src)
    dirobj.wipe(dst)
    #create the dirs
    if not os.path.exists(src):
        os.makedirs(src)
    ##put a test file in the test directory
    with open(os.path.join(src, 'tmp.txt'), 'w') as file: 
        pass
    ##put a subfolder in the test directory
    os.makedirs(os.path.join(src, 'tmp2'))
    ##put a test file in the subfolder
    with open(os.path.join(src, 'tmp2', 'tmp.txt'), 'w') as file: 
        pass
    #copy
    dirobj.path = src
    outcome = dirobj.copy(dst)
    #test dst
    assert outcome
    assert os.path.exists(dst)
    assert os.path.isdir(dst)
    assert os.path.exists(os.path.join(dst, 'tmp2'))
    assert os.path.isdir(os.path.join(dst, 'tmp2'))
    assert os.path.exists(os.path.join(dst, 'tmp.txt'))
    assert os.path.isfile(os.path.join(dst, 'tmp.txt'))
    assert os.path.exists(os.path.join(dst, 'tmp2', 'tmp.txt'))
    assert os.path.isfile(os.path.join(dst, 'tmp2', 'tmp.txt'))
    #test src still exist
    assert os.path.exists(src)
    #teardown
    dirobj.wipe(src)
    dirobj.wipe(dst)

def test_move(dirobj):
    #setup
    src = '/tmp/test_copy'
    dst = '/tmp/test_copy2'
    #wipe
    dirobj.wipe(src)
    dirobj.wipe(dst)
    #create the dirs
    if not os.path.exists(src):
        os.makedirs(src)
    ##put a test file in the test directory
    with open(os.path.join(src, 'tmp.txt'), 'w') as file: 
        pass
    ##put a subfolder in the test directory
    os.makedirs(os.path.join(src, 'tmp2'))
    ##put a test file in the subfolder
    with open(os.path.join(src, 'tmp2', 'tmp.txt'), 'w') as file: 
        pass
    #move
    dirobj.path = src
    outcome = dirobj.move(dst)
    #test dst
    assert outcome
    assert os.path.exists(dst)
    assert os.path.isdir(dst)
    assert os.path.exists(os.path.join(dst, 'tmp2'))
    assert os.path.isdir(os.path.join(dst, 'tmp2'))
    assert os.path.exists(os.path.join(dst, 'tmp.txt'))
    assert os.path.isfile(os.path.join(dst, 'tmp.txt'))
    assert os.path.exists(os.path.join(dst, 'tmp2', 'tmp.txt'))
    assert os.path.isfile(os.path.join(dst, 'tmp2', 'tmp.txt'))
    #test src no longer exist
    assert not os.path.exists(src)
    #teardown
    dirobj.wipe(src)
    dirobj.wipe(dst)
