"""
tests frua.base.fs.file.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging
import os

from frua.base.fs.file import File

@pytest.fixture
def fobj():
    obj = File()
    return obj

def test_init(fobj):
    assert isinstance(fobj, File)

def test_get_set_path(fobj):
    assert fobj.path is None
    fobj.path = 'test'
    assert fobj.path == 'test'

def test_copy(fobj):
    #setup
    src = '/tmp/test_copy.txt'
    dst = '/tmp/test_copy2.txt'
    ##create an empty src file
    with open(src, 'w') as file: 
        pass
    #copy
    fobj.path = src
    outcome = fobj.copy(dst)
    #test dst
    assert outcome
    assert os.path.exists(src)
    assert os.path.exists(dst)
    assert os.path.isfile(src)
    assert os.path.isfile(dst)
    #teardown
    if os.path.exists(src):
        os.unlink(src)
    if os.path.exists(dst):
        os.unlink(dst)

def test_move(fobj):
    #setup
    src = '/tmp/test_copy.txt'
    dst = '/tmp/test_copy2.txt'
    ##create an empty src file
    with open(src, 'w') as file: 
        pass
    #copy
    fobj.path = src
    outcome = fobj.move(dst)
    #test dst
    assert outcome
    assert os.path.exists(dst)
    assert not os.path.exists(src)
    assert os.path.isfile(dst)
    #teardown
    if os.path.exists(src):
        os.unlink(src)
    if os.path.exists(dst):
        os.unlink(dst)

