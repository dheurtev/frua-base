"""
Object serialized/deserialized to/from JSON

Extends UUIDObj

Uses:
- os: https://docs.python.org/3/library/os.html
- json: https://docs.python.org/3/library/json.html
- logging: https://docs.python.org/3/library/logging.html
- copy: https://docs.python.org/3/library/copy.html
- errno: https://docs.python.org/3/library/errno.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import json
import os
import logging
import copy
import errno


from frua.base.obj.uidobj import UUIDObj

class JSONObj(UUIDObj):
    """
    Object with a datetime

    Object serialized/deserialized to/from JSON

    Extends UUIDObj
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments
        """
        super().__init__(*args, **kwargs)
        #other attributes
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)

    def json_serialize(self, sort_keys:bool=True, indent:int=4) -> str:
        """
        Serialize object to JSON

        Args:
            sort_keys (bool, optional): sort keys
            indent (int, optional): indentation of the json output

        Returns:
            str: JSON string representation of the object
        """
        try:
            cobj = copy.deepcopy(self)
            if hasattr(self, '_logger'):
                del(cobj.__dict__["_logger"])
            jsonstr = json.dumps(cobj.__dict__, sort_keys=sort_keys, indent=indent)
        except TypeError:
            raise TypeError('Cannot serialize object to JSON')
        return jsonstr

    def json_deserialize(self, jsonstring:str, copy:bool=True) -> object:
        """
        Deserialize a JSON String into the object

        Args:
            jsonstring (str) : JSON string representation of the object
            copy (bool, optional)  : if True, copy to the __dict__ of the deserialized object

        Returns:
            obj: deserialized object
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

    def tojson(self, obj:object=None) -> str:
        """
        Serialize object to JSON

        If an object is provided, serialize it to JSON without copying to the container object (self)

        Args:
            obj (object, optional): object to serialize

        Returns:
            str: JSON string representation of the object
        """
        if obj == None:
            return self.json_serialize()
        else:
            s = JSONObj().from_dict(self.__dict__)
            return json.dumps(obj)

    def fromjson(self, jsonstring:str, copy=True) -> dict:
        """
        Deserialize a JSON String into the object

        Args:      
            jsonstring (str, optional): JSON string representation of the object
            copy (bool, optional): if True, copy to the __dict__ of the deserialized object

        Returns:
            dict: The __dict__ of the deserialized object
        """
        if copy:
            return self.json_deserialize(jsonstring, copy=copy)
        else:
            return json.loads(jsonstring)
    
    
    def json_serialize_to_file(self, filepath:str, create_dir:bool=True, sort_keys:bool=True, indent:int=4) -> str:
        """
        Serialize object to JSON and write it to a file

        Args:
            filepath (str): filepath to write to
            create_dir (bool, optional): create directory if it does not exist
            sort_keys (bool, optional): sort keys
            indent (int, optional): indentation of the json output

        Returns:
            str: filepath
        """
        #check if directory exists, else create it
        if create_dir and not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
                if hasattr(self, '_logger'):
                    self._logger.debug('Created dir for %s'%filepath)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
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

    def json_deserialize_from_file(self, filepath:str) -> object:
        """
        Deserialize a JSON File into the object

        Args:
            filepath (str): filepath to read from

        Returns:
            object: JSON Object representation
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
       
    def tojson_file(self, filepath:str, create_dir:bool=True, sort_keys:bool=True, indent:int=4) -> str:
        """
        Serialize object to JSON and write it to a file

        Args:
            filepath (str): filepath to write to
            create_dir (bool, optional) : create directory if it does not exist
            sort_keys (bool, optional) : sort keys
            indent (int, optional) : indentation of the json output

        Returns:
            str: filepath
        """
        return self.json_serialize_to_file(filepath, create_dir, sort_keys, indent)

    def fromjson_file(self, filepath:str) -> object:
        """
        Deserialize a JSON File into the object

        Args:
            filepath(str): filepath to read from

        Returns:
           object: JSON Object representation
        """
        return self.json_deserialize_from_file(filepath)

    def __str__(self) -> str:
        return self.json_serialize()

    def __repr__(self) -> str:
        return self.json_serialize()

