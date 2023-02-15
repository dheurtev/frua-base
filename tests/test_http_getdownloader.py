"""
tests frua.base.http.getdownloader.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os

from frua.base.http.getdownloader import GetDownloader

@pytest.fixture
def dobj():
    obj = GetDownloader()
    return obj

def test_init(dobj):
    assert isinstance(dobj, GetDownloader)
    assert hasattr(dobj, '_url')
    assert hasattr(dobj, '_file_name')
    assert hasattr(dobj, '_file_dir')

def test_init2():
    filename = 'getdownloader.txt'
    filedir = '/tmp'
    url = 'https://example.com/'
    obj = GetDownloader(url=url, file_name=filename, file_dir=filedir)
    assert isinstance(obj, GetDownloader)
    assert hasattr(obj, '_url')
    assert obj._url == url
    assert hasattr(obj, '_file_name')
    assert obj._file_name == filename
    assert hasattr(obj, '_file_dir')
    assert obj._file_dir == filedir

def test_download(dobj):
    filename = 'getdownloader.txt'
    filedir = '/tmp'
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = 'https://example.com/'
    dobj.file_name = filename
    dobj.file_dir = filedir
    #test url, file_name and file_dir set
    assert dobj._url is not None
    assert dobj._file_name is not None
    assert dobj._file_dir is not None
    #download
    dobj.download()
    #test
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 0
    #teardown
    if os.path.isfile(path):
        os.remove(path)

def test_download_overwrite(dobj):
    filename = 'getdownloader.txt'
    filedir = '/tmp'
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = 'https://example.com/'
    dobj.file_name = filename
    dobj.file_dir = filedir
    #test url, file_name and file_dir set
    assert dobj._url is not None
    assert dobj._file_name is not None
    assert dobj._file_dir is not None
    #download
    dobj.download()
    #test
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 0
    mtime = os.path.getmtime(path)
    #download again with overwrite
    dobj.download(overwrite=True)
    #test
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 0
    mtime2 = os.path.getmtime(path)
    assert mtime2 > mtime
    #teardown
    if os.path.isfile(path):
        os.remove(path)

def test_download_existing_file(dobj):
    filename = 'getdownloader.txt'
    filedir = '/tmp'
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = 'https://example.com/'
    dobj.file_name = filename
    dobj.file_dir = filedir
    #test url, file_name and file_dir set
    assert dobj._url is not None
    assert dobj._file_name is not None
    assert dobj._file_dir is not None
    #download
    dobj.download()
    #test
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 0
    mtime = os.path.getmtime(path)
    #download again without overwrite (should fail)
    ret = dobj.download(overwrite=False)
    #test
    assert not ret
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 0
    mtime2 = os.path.getmtime(path)
    #no modification
    assert mtime2 == mtime
    #teardown
    if os.path.isfile(path):
        os.remove(path)

def test_url_not_set(dobj):
    filename = 'getdownloader.txt'
    filedir = '/tmp'
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = None
    dobj.file_name = filename
    dobj.file_dir = filedir
    #test url, file_name and file_dir set
    assert dobj._url is None
    assert dobj._file_name is not None
    assert dobj._file_dir is not None
    #download
    ret = dobj.download()
    #test
    assert not ret
    assert not os.path.isfile(path)
    #teardown
    if os.path.isfile(path):
        os.remove(path)    

def test_filename_not_set(dobj):
    filename = 'example.com'
    filedir = '/tmp'
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = 'https://example.com/'
    dobj.file_name = None
    dobj.file_dir = filedir
    #test url, file_name and file_dir set
    assert dobj._url is not None
    assert dobj._file_name is None
    assert dobj._file_dir is not None
    #download
    ret = dobj.download()
    #test
    assert dobj._file_name is not None
    assert dobj._file_name == filename #must be the domain name
    assert os.path.isfile(path)
    #teardown
    if os.path.isfile(path):
        os.remove(path)

def test_filedir_not_set(dobj):
    filename = 'example.com'
    filedir = os.path.normpath(os.path.join(os.getcwd(), '..'))
    #setup
    path = os.path.join(filedir, filename)
    if os.path.isfile(path):
        os.remove(path)
    #start
    dobj.url = 'https://example.com/'
    dobj.file_name = filename
    dobj.file_dir = None
    #test url, file_name and file_dir set
    assert dobj._url is not None
    assert dobj._file_name is not None
    assert dobj._file_dir is None
    #download
    ret = dobj.download()
    #test
    assert dobj._file_dir is not None
    assert dobj._file_dir == filedir #must be the current directory
    assert os.path.isfile(path)
    #teardown
    if os.path.isfile(path):
        os.remove(path)





