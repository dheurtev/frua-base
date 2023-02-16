"""
tests frua.base.data.file.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os

from frua.base.data.file import File

@pytest.fixture
def file():
    path = '/tmp/file.txt'
    content = 'test'
    f = File(path, content)
    return f

def test_init(file):
    assert isinstance(file, File)
    assert file.path == '/tmp/file.txt'
    assert file.content == 'test'

def test_write_read(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write
    file.write()
    #test
    assert os.path.exists(file.path)
    #read back 
    f1 = File(file.path)
    f1.read()
    #test
    assert f1.content[0] == 'test'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_write_read_dry(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write
    file.write(dry=True)
    #test
    assert not os.path.exists(file.path)
    #read back
    f1 = File(file.path)
    f1.read(dry=True)
    #test
    assert f1.content == None
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_head(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write test content and test
    file.content = ['line1\n', 'line2']
    file.write()
    assert os.path.exists(file.path)
    #perform head
    cread = file.head()
    #test
    assert len(cread) == 1
    assert cread[0] == 'line1\n'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_tail(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write test content and test
    file.content = ['line1\n', 'line2']
    file.write()
    assert os.path.exists(file.path)
    #perform tail
    cread = file.tail()
    #test
    assert len(cread) == 1
    assert cread[0] == 'line2'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_append_bottom(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write existing content
    file.content = ['test\n']
    file.write()
    assert os.path.exists(file.path)
    #append
    file.content = ['line1\n', 'line2\n']
    file.append_bottom()
    #read back
    f1 = File(file.path)
    f1.read()
    #test
    assert os.path.exists(f1.path)
    assert len(f1.content) == 3
    assert f1.content[0] == 'test\n'
    assert f1.content[1] == 'line1\n'
    assert f1.content[2] == 'line2\n'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_append_top(file):
    #setup
    if os.path.exists(file.path):
        os.remove(file.path)
    #write existing content
    file.write()
    assert os.path.exists(file.path)
    #append
    file.content = ['line1\n', 'line2\n']
    file.append_top()
    #read back
    f1 = File(file.path)
    f1.read()
    #test
    assert os.path.exists(f1.path)
    assert len(f1.content) == 3
    assert f1.content[0] == 'line1\n'
    assert f1.content[1] == 'line2\n'
    assert f1.content[2] == 'test'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)

def test_merge(file):
    #setup
    ##first file
    if os.path.exists(file.path):
        os.remove(file.path)
    #create first file
    file.content = ['test\n']
    file.write()
    ##second file
    path2 = '/tmp/file2.txt'
    if os.path.exists(path2):
        os.remove(path2)
    #create second file
    content2 = 'test2\n'
    file2 = File(path2, content2)
    file2.write()
    ##third file
    dst = '/tmp/file3.txt'
    if os.path.exists(dst):
        os.remove(dst)
    #merge the two files
    file.merge(file2.path, dst)
    #test
    assert os.path.exists(dst)
    #read back
    f3 = File(dst)
    f3.read()
    #test
    assert len(f3.content) == 2
    assert f3.content[0] == 'test\n'
    assert f3.content[1] == 'test2\n'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)
    if os.path.exists(file2.path):
        os.remove(file2.path)
    if os.path.exists(dst):
        os.remove(dst)

def test_merge_remove(file):
    #setup
    ##first file
    if os.path.exists(file.path):
        os.remove(file.path)
    #create first file
    file.content = ['test\n']
    file.write()
    ##second file
    path2 = '/tmp/file2.txt'
    if os.path.exists(path2):
        os.remove(path2)
    #create second file
    content2 = 'test2\n'
    file2 = File(path2, content2)
    file2.write()
    ##third file
    dst = '/tmp/file3.txt'
    if os.path.exists(dst):
        os.remove(dst)
    #merge the two files
    file.merge(file2.path, dst, remove_src=True)
    #test
    assert os.path.exists(dst)
    assert not os.path.exists(file2.path)
    assert not os.path.exists(file.path)
    #read back
    f3 = File(dst)
    f3.read()
    #test
    assert len(f3.content) == 2
    assert f3.content[0] == 'test\n'
    assert f3.content[1] == 'test2\n'
    #teardown
    if os.path.exists(file.path):
        os.remove(file.path)
    if os.path.exists(file2.path):
        os.remove(file2.path)
    if os.path.exists(dst):
        os.remove(dst)

