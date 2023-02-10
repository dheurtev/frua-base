"""
tests frua.base.obj.crudobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import datetime

from frua.base.obj.crudobj import CRUDObj

@pytest.fixture
def crudobj():
    return CRUDObj()

def test_crudobj_init(crudobj):
    assert crudobj._dt != None
    assert crudobj._id != None
    assert crudobj.enabled == False
    assert crudobj.deleted == False
    assert crudobj.enabled_at != None
    assert crudobj.created_at != None
    assert crudobj.read_at == None
    assert crudobj.updated == None
    assert crudobj.deleted_at == None

