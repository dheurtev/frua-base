"""
tests frua.base.obj.dictobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging
import logging.config

from frua.base.obj.dictobj import DictObj

@pytest.fixture
def dictobj():
    dictobj = DictObj()
    return dictobj

def test_init(dictobj):
    assert isinstance(dictobj, DictObj)
    assert '_args' in dictobj.__dict__

def test_init_with_args():
    obj = DictObj(1, 2)
    assert isinstance(obj, DictObj)
    assert obj._args != None

def test_init_with_kwargs():
    obj = DictObj(a=1, b=2)
    assert isinstance(obj, DictObj)
    assert obj.a == 1
    assert obj.b == 2

def test_init_with_args_and_kwargs():
    obj = DictObj(1, 2, c=3)
    assert isinstance(obj, DictObj)
    assert obj._args != None
    assert obj.c == 3

def test_from_dict(dictobj):
    obj = DictObj()
    assert isinstance(obj, DictObj)
    dictio = {'a': 1, 'b': 2}
    obj = obj.from_dict(dictio)
    assert obj.a == 1
    assert obj.b == 2
    