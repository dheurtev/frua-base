"""
Object serialized/deserialized to/from JSON

Extends UUIDObj

Uses:
- os: https://docs.python.org/3/library/os.html
- json: https://docs.python.org/3/library/json.html
- logging: https://docs.python.org/3/library/logging.html
- copy: https://docs.python.org/3/library/copy.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import json
import os
import logging
import copy


from frua.base.obj.uidobj import UUIDObj

class JSONObj(UUIDObj):
    """
    Object with a datetime

    Object serialized/deserialized to/from JSON

    Extends UUIDObj
    """
    
    def __init__(self, *args, **kwargs):
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments
        """
        super().__init__(*args, **kwargs)
        #other attributes
        #handle logger
        if not hasattr(self, '_logger'):
            self._logger = logging.getLogger(__name__)

    def json_serialize(self, sort_keys=True, indent=4):
        """
        Serialize object to JSON

        Args:
            sort_keys : sort keys
            indent : indentation of the json output

        Returns:
            :str: JSON string representation of the object
        """
        try:
            cobj = copy.deepcopy(self)
            if hasattr(self, '_logger'):
                del(cobj.__dict__["_logger"])
            jsonstr = json.dumps(cobj.__dict__, sort_keys=sort_keys, indent=indent)
        except TypeError:
            raise TypeError('Cannot serialize object to JSON')
        return jsonstr

    def json_deserialize(self, jsonstring, copy=True):
        """
        Deserialize a JSON String into the object

        Args:
            jsonstring : JSON string representation of the object
            copy : if True, copy to the __dict__ of the deserialized object

        Returns:
            :obj: deserialized object
        """
        try:
            obj = json.loads(jsonstring)    
        except TypeError:
            raise TypeError('Cannot deserialize object from JSON')
        if copy:
            self.__dict__.update(obj)
            return self
        else:
            return obj

    def tojson(self, obj=None):
        """
        Serialize object to JSON

        If an object is provided, serialize it to JSON without copying to the container object (self)

        Args:
            obj : object to serialize (optional)

        Returns:
            :str: JSON string representation of the object
        """
        if obj == None:
            return self.json_serialize()
        else:
            s = JSONObj().from_dict(self.__dict__)
            return json.dumps(obj)

    def fromjson(self, jsonstring, copy=True):
        """
        Deserialize a JSON String into the object

        Args:      
           copy : if True, copy to the __dict__ of the deserialized object

        Returns:
            :dict: The __dict__ of the deserialized object
        """
        if copy:
            return self.json_deserialize(jsonstring, copy=copy)
        else:
            return json.loads(jsonstring)
    
    
    def json_serialize_to_file(self, filepath, create_dir=True, sort_keys=True, indent=4):
        """
        Serialize object to JSON and write it to a file

        Args:
            filepath : filepath to write to
            create_dir : create directory if it does not exist
            sort_keys : sort keys
            indent : indentation of the json output

        Returns:
            filepath
        """
        #check if directory exists, else create it
        if create_dir and not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
                if hasattr(self, '_logger'):
                    self._logger.debug('Created dir for %s'%filepath)
            except OSError as exc: # Guard against race condition
                if exc.errno!= errno.EEXIST:
                    raise
        #dump to the file
        try:
            with open(filepath, 'w') as file:
                cobj = copy.deepcopy(self)
                if hasattr(self, '_logger'):
                    del(cobj.__dict__["_logger"])
                json.dump(cobj.__dict__, file, sort_keys=sort_keys, indent=indent)
                file.close()
                if hasattr(self, '_logger'):
                    self._logger.debug('JSON Object %s dumped to %s'%(self._id, filepath))
            return filepath
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error('Could not dump JSON Object %s to %s'%(self._id, filepath))
                self._logger.error(e)
            raise e
        return None

    def json_deserialize_from_file(self, filepath):
        """
        Deserialize a JSON File into the object

        Args:
            filepath : filepath to read from

        Returns:
            JSON Object representation
        """
        #check if file exists
        if not os.path.exists(filepath):
            if hasattr(self, '_logger'):
                self._logger.error('JSON file not found in %s'%(filepath))
            return None
        #load from the file
        try:
            with open(filepath, 'r') as file:
                self = json.load(file)    
                file.close()
            if hasattr(self, '_logger'):
                self._logger.debug('JSON Object %s read from %s'%(self._id, filepath))
            return str(self)
        except Exception as e:
            if hasattr(self, '_logger'):
                self._logger.error('Could not read JSON Object %s from %s'%(self._id, filepath))
                self._logger.error(e)
            raise e
        return None
       
    def tojson_file(self, filepath, create_dir=True, sort_keys=True, indent=4):
        """
        Serialize object to JSON and write it to a file

        Args:
            filepath : filepath to write to
            create_dir : create directory if it does not exist
            sort_keys : sort keys
            indent : indentation of the json output

        Returns:
            filepath
        """
        return self.json_serialize_to_file(filepath, create_dir, sort_keys, indent)

    def fromjson_file(self, filepath):
        """
        Deserialize a JSON File into the object

        Args:
            filepath : filepath to read from

        Returns:
            JSON Object representation
        """
        return self.json_deserialize_from_file(filepath)

    def __str__(self):
        return self.json_serialize()

    def __repr__(self):
        return self.json_serialize()

if __name__ == '__main__':
    d = JSONObj()
    print(d.__dict__)
    jsonstring = d.json_serialize()
    print(jsonstring)
    print(d.tojson())
    print(d.fromjson(jsonstring))
    print(d.json_serialize_to_file('/tmp/test.json'))
    print(d.json_deserialize_from_file('/tmp/test.json'))
    print(d.tojson_file('/tmp/test1.json'))
    print(d.fromjson_file('/tmp/test1.json'))