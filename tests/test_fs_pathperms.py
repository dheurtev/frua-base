"""
tests frua.base.fs.pathperms.py

Assumes /tmp is owned by root:root and has rwxrwxrwx permissions.

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os
import os.path

from frua.base.fs.pathperms import PathPerms

@pytest.fixture
def ppobj():
    obj = PathPerms()
    return obj

def test_init(ppobj):
    assert isinstance(ppobj, PathPerms)

def test_property(ppobj):
    assert ppobj._path is None

def test_set_path(ppobj):
    ppobj.path = '/tmp/testfile.txt'
    assert ppobj.path == '/tmp/testfile.txt'

def test_gid(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.gid == 0

def test_uid(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.uid == 0

def test_stats(ppobj):
    #test starting
    ppobj.path = '/tmp'
    assert ppobj.stats.st_uid == 0
    
def test_perms_str(ppobj):
    #setup
    path = '/tmp/testfile.txt'
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'w') as file: 
        pass
    os.chmod(path, 0o644)
    #test starting
    ppobj.path = '/tmp/testfile.txt'
    assert ppobj.perms(rep='str') == '-rw-r--r--'
    #tear down
    if os.path.exists(path):
        os.remove(path)

def test_perms_oct(ppobj):
    #setup
    path = '/tmp/testfile.txt'
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'w') as file: 
        pass
    os.chmod(path, 0o644)
    #test starting
    ppobj.path = '/tmp/testfile.txt'
    assert ppobj.perms(rep='oct') == oct(0o100644)
    #tear down
    if os.path.exists(path):
        os.remove(path)

def test_owner_name(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.owner_name == 'root'

def test_group_name(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.group_name == 'root'

def test_other_perms(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.others_perms() == 'rwx'

def test_group_perms(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.group_perms() == 'rwx'

def test_owner_perms(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.owner_perms() == 'rwx'

def test_is_readable(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_readable() == True

def test_is_writablle(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_writable() == True

def test_is_executable(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_executable() == True

def test_is_read_only(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_read_only() == False

def test_is_read_writable(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_read_writable() == False

def test_is_read_executable(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_read_executable() == False

def test_is_full_access(ppobj):
    ppobj.path = '/tmp'
    assert ppobj.is_full_access() == True
