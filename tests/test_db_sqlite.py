"""
tests frua.base.db.sqlite.py

In-memory test
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging

from frua.base.db.sqlite import Sqlite

@pytest.fixture
def sobj():
    obj = Sqlite()
    return obj

def test_init(sobj):
    assert isinstance(sobj, Sqlite)
