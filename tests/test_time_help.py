"""
tests frua.base.time.help.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import datetime

from frua.base.time.help import TimeHelp

def test_time_help():
    T = TimeHelp()
    assert isinstance(T, TimeHelp)

def test_now():
    assert TimeHelp().now() != None

def test_now_str():
    assert TimeHelp().now_str() != None
    assert isinstance(TimeHelp().now_str(), str)

def test_now_us_str():
    assert TimeHelp().now_us_str() != None
    assert isinstance(TimeHelp().now_us_str(), str)
    assert 'PM' in TimeHelp().now_us_str() or 'AM' in TimeHelp().now_us_str()

def test_now_eu_str():
    assert TimeHelp().now_eu_str() != None
    assert isinstance(TimeHelp().now_eu_str(), str)

def test_now_dt():
    assert TimeHelp().now_dt() != None
    assert isinstance(TimeHelp().now_dt(), datetime.datetime)

def test_now_ts():
    assert TimeHelp().now_ts() != None
    assert isinstance(TimeHelp().now_ts(), float)

def test_now_iso():
    assert TimeHelp().now_iso() != None
    assert isinstance(TimeHelp().now_iso(), str)

def test_utcnow():
    assert TimeHelp().utcnow() != None

def test_utcnow_str():
    assert TimeHelp().utcnow_str()!= None
    assert isinstance(TimeHelp().utcnow_str(), str)

def test_utcnow_dt():
    assert TimeHelp().utcnow_dt() != None
    assert isinstance(TimeHelp().utcnow_dt(), datetime.datetime)

def test_utcnow_ts():
    assert TimeHelp().utcnow_ts() != None
    assert isinstance(TimeHelp().utcnow_ts(), float)

def test_utcnow_iso():
    assert TimeHelp().utcnow_iso() != None
    assert isinstance(TimeHelp().utcnow_iso(), str)

def test_epoch():
    assert TimeHelp().epoch() != None
    assert TimeHelp().epoch() == datetime.datetime(1970, 1, 1, 0, 0)

