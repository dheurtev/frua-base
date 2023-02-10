"""
tests frua.base.obj.jsonobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
from frua.base.obj.jsonobj import JSONObj
import json
import os

curdir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def jsonobj():
    obj = JSONObj()
    return obj

def test_init(jsonobj):
    assert jsonobj.__dict__ != None

def test_json_serialize(jsonobj):
    jsonobj.p = 'test'
    jsonstring = jsonobj.json_serialize()
    compobj = json.loads(jsonstring)
    assert compobj['p'] == 'test'

def test_json_deserialize(jsonobj):
    jsonobj.p = 'test'
    jsonstring = jsonobj.json_serialize()
    jsonobj1 = JSONObj()
    jsonobj1.json_deserialize(jsonstring)
    assert jsonobj.p == 'test'

def test_tojson(jsonobj):
    jsonobj.p = 'test'
    jsonstring = jsonobj.tojson()
    compobj = json.loads(jsonstring)
    assert compobj['p'] == 'test'

def test_fromjson(jsonobj):
    jsonobj.p = 'test'
    jsonstring = jsonobj.tojson()
    jsonobj1 = JSONObj()
    jsonobj1.fromjson(jsonstring)
    assert jsonobj.p == 'test'

def test_json_serialize_to_file(jsonobj):
    filepath = '/tmp/test.json'
    #remove the file if it exists
    if os.path.isfile(filepath):
        os.remove(filepath)
    #write
    compobj1 = jsonobj.json_serialize_to_file(filepath)
    #check file exists
    assert os.path.isfile(filepath)  

def test_json_deserialize_from_file(jsonobj):
    filepath = os.path.join(curdir, 'test.json')
    compobj1 = jsonobj.json_deserialize_from_file(filepath)
    assert compobj1 != None

def test_tojson_file(jsonobj):
    filepath = '/tmp/test.json'
    #remove the file if it exists
    if os.path.isfile(filepath):
        os.remove(filepath)
    #write
    compobj1 = jsonobj.tojson_file(filepath)
    #check file exists
    assert os.path.isfile(filepath)  
    
def test_fromjson_file(jsonobj):
    filepath = os.path.join(curdir, 'test.json')
    compobj1 = jsonobj.fromjson_file(filepath)
    assert compobj1 != None

def test_to_json_list():
    sobj = [1, 2, 3, 4]
    jstr = '[1, 2, 3, 4]'
    jobj = JSONObj().tojson(sobj)
    assert jobj == jstr

def test_to_json_dict():
    sobj = {'test1':'A', 'test2':'B'}
    jstr = '{"test1": "A", "test2": "B"}'
    jobj = JSONObj().tojson(sobj)
    assert jobj == jstr

def test_from_json_list():
    jstr = '[1, 2, 3, 4]'
    sobj = JSONObj().fromjson(jstr, copy=False)
    assert sobj == [1, 2, 3, 4]

def test_from_json_dict():
    jstr = '{"test1": "A", "test2": "B"}'
    sobj = JSONObj().fromjson(jstr, copy=False)
    assert sobj == {'test1': 'A', 'test2': 'B'}
