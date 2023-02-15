"""
tests frua.base.fs.groups.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest

from frua.base.fs.groups import Groups

@pytest.fixture
def groupobj():
    obj = Groups()
    return obj

def test_init(groupobj):
    assert isinstance(groupobj, Groups)

def test_gid_from_name(groupobj):
    gid = groupobj.gid('root')
    assert gid == 0

def test_name_from_gid(groupobj):
    gid = groupobj.gid('root')
    assert groupobj.group(gid) == 'root'

