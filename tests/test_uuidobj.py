"""
tests frua.base.obj.uidobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging
import logging.config

from frua.base.obj.uidobj import UUIDObj

@pytest.fixture
def idobj():
    obj = UUIDObj()
    return obj

def test_id(idobj):
    assert idobj.id != None
