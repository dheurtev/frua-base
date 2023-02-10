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
    assert '_id' in jsonobj.__dict__
    assert '_args' in jsonobj.__dict__

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
    assert '_id' in jsonobj1.__dict__
    assert '_args' in jsonobj1.__dict__
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
    assert '_id' in jsonobj1.__dict__
    assert '_args' in jsonobj1.__dict__
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
    assert '_id' in compobj1
    assert '_args' in compobj1

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
    assert '_id' in compobj1
    assert '_args' in compobj1
