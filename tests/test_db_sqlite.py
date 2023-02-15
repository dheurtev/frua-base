"""
tests frua.base.db.sqlite.py

In-memory test

Uses example data from https://docs.python.org/3/library/sqlite3.html

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

def test_connect(sobj):
    assert sobj._conn == None
    sobj.connect()
    assert sobj._conn != None

def test_conn(sobj):
    sobj.connect()
    assert sobj.conn != None
    assert sobj.conn == sobj._conn

def test_cursor(sobj):
    sobj.connect()
    assert sobj.cursor != None

def test_close(sobj):
    sobj.connect()
    sobj.close()
    assert True

def test_execute(sobj):
    sobj.connect()
    sobj.execute("SELECT 1")
    assert True

def test_execute_create_table(sobj):
    sobj.connect()
    res = sobj.execute("CREATE TABLE movie(title, year, score)")
    row = res.fetchone()
    assert row == None

def test_execute_create_table_select_table(sobj):
    sobj.connect()
    sobj.execute("CREATE TABLE movie(title, year, score)")
    res = sobj.execute("SELECT name FROM sqlite_master")
    row = res.fetchone()
    assert 'movie' in row

def test_execute_create_table_select_table_none(sobj):
    sobj.connect()
    sobj.execute("CREATE TABLE movie(title, year, score)")
    res = sobj.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    row = res.fetchone()
    assert row is None

def test_execute_create_table_insert_commit(sobj):
    sobj.connect()
    sobj.execute("CREATE TABLE movie(title, year, score)")
    sql = ("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
    sobj.execute(sql)
    sobj.commit()
    res = sobj.execute("SELECT score FROM movie")
    row = res.fetchall()
    assert len(row) is 2

def test_execute_create_table_insert_rollback(sobj):
    sobj.connect()
    sobj.execute("CREATE TABLE movie(title, year, score)")
    sql = ("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
    sobj.execute(sql)
    res = sobj.execute("SELECT score FROM movie")
    row = res.fetchall()
    assert len(row) is 2
    sobj.rollback()
    res1 = sobj.execute("SELECT score FROM movie")
    row1 = res1.fetchall()
    assert len(row1) == 0

def test_executemany(sobj):
    sobj.connect()
    sobj.execute("CREATE TABLE movie(title, year, score)")
    data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
    ]    
    sobj.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    sobj.commit()
    res1 = sobj.execute("SELECT score FROM movie")   
    rows = res1.fetchall()
    assert len(rows) == 3
