"""
tests frua.base.fs.users.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest

from frua.base.fs.users import Users

@pytest.fixture
def userobj():
    obj = Users()
    return obj

def test_init(userobj):
    assert isinstance(userobj, Users)

def test_uid_from_name(userobj):
    uid = userobj.uid('root')
    assert uid == 0

def test_name_from_uid(userobj):
    uid = userobj.uid('root')
    assert userobj.user(uid) == 'root'

