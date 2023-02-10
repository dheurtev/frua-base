"""
tests frua.base.obj.crudobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import datetime

from frua.base.obj.crudobj import CRUDObj
from frua.base.time.help import TimeHelp

@pytest.fixture
def crudobj():
    return CRUDObj()

def test_crudobj_init(crudobj):
    assert crudobj._dt != None
    assert crudobj._id != None
    assert crudobj.enabled == True
    assert crudobj.deleted == False
    assert crudobj.enabled_at != None
    assert crudobj.created_at != None
    assert crudobj.read_at == None
    assert crudobj.updated_at == None
    assert crudobj.deleted_at == None

def test_crudobj_create(crudobj):
    crudobj.create()
    assert crudobj.created_at > TimeHelp.epoch()
    assert crudobj.created_at < TimeHelp.now()

def test_crudobj_read(crudobj):
    crudobj.read()
    assert crudobj.read_at > TimeHelp.epoch()
    assert crudobj.read_at < TimeHelp.now()

def test_crudobj_update(crudobj):
    crudobj.update()
    assert crudobj.updated_at > TimeHelp.epoch()
    assert crudobj.updated_at < TimeHelp.now()

def test_crudobj_delete(crudobj):
    crudobj.delete()
    assert crudobj.deleted_at > TimeHelp.epoch()
    assert crudobj.deleted_at < TimeHelp.now()
    assert crudobj.deleted == True

def test_crudobj_undelete(crudobj):
    crudobj.delete()
    assert crudobj.deleted_at > TimeHelp.epoch()
    assert crudobj.deleted_at < TimeHelp.now()
    assert crudobj.deleted == True
    crudobj.undelete()
    assert crudobj.deleted == False
    assert crudobj.deleted_at == None    

def test_crudobj_enable(crudobj):
    crudobj.disable()
    assert crudobj.enabled == False
    assert crudobj.disabled_at > TimeHelp.epoch()
    assert crudobj.disabled_at < TimeHelp.now()
    crudobj.enable()
    assert crudobj.enabled_at > TimeHelp.epoch()
    assert crudobj.enabled_at < TimeHelp.now()
    assert crudobj.enabled == True

def test_crudobj_disable(crudobj):
    crudobj.enable()
    assert crudobj.enabled_at > TimeHelp.epoch()
    assert crudobj.enabled_at < TimeHelp.now()
    assert crudobj.enabled == True
    crudobj.disable()
    assert crudobj.enabled == False
    assert crudobj.disabled_at > TimeHelp.epoch()
    assert crudobj.disabled_at < TimeHelp.now()

def test_crudobj_is_enabled(crudobj):
    crudobj.enable()
    crudobj.is_enabled()
    assert crudobj.enabled == True

def test_crudobj_is_disabled(crudobj):
    crudobj.disable()
    crudobj.is_disabled()
    assert crudobj.enabled == False

def test_crudobj_is_active(crudobj):
    crudobj.undelete()
    crudobj.is_active()
    assert crudobj.deleted == False

def test_crudobj_is_deleted(crudobj):
    crudobj.delete()
    crudobj.is_deleted()
    assert crudobj.deleted == True
