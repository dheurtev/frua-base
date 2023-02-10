"""
tests frua.base.obj.dtobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import datetime

from frua.base.obj.dtobj import DTObj

@pytest.fixture
def dtobj():
    return DTObj()

def test_dtobj_init(dtobj):
    assert dtobj._dt != None
    assert '_dt' in dtobj.__dict__

def test_dtobj_set_get_dt(dtobj):
    dt = datetime.datetime.now()
    dtobj.dt = dt
    assert dtobj._dt == dt
    assert dtobj.dt == dt

def test_dtobj_reset_dt(dtobj):
    dt = dtobj.reset_dt()
    assert dtobj._dt == dt