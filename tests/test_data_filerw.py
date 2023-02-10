"""
tests frua.base.data.filerw.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os

from frua.base.data.filerw import FileRW

@pytest.fixture
def filerw():
    path = '/tmp/filerw.txt'
    content = 'test'
    f = FileRW(path, content)
    return f

def test_write_read(filerw):
    if os.path.exists(filerw.path):
        os.remove(filerw.path)
    filerw.write()
    assert os.path.exists(filerw.path)
    f1 = FileRW(filerw.path)
    f1.read()
    assert f1.content[0] == 'test'
    if os.path.exists(filerw.path):
        os.remove(filerw.path)

def test_write_read_dry(filerw):
    if os.path.exists(filerw.path):
        os.remove(filerw.path)
    filerw.write(dry=True)
    assert not os.path.exists(filerw.path)
    f1 = FileRW(filerw.path)
    f1.read(dry=True)
    assert f1.content == None
    if os.path.exists(filerw.path):
        os.remove(filerw.path)

