"""
Object identified with a unique identifier.

Uses:
- uuid.uuid4

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

from uuid import uuid4
from frua.base.obj.dictobj import DictObj

class UUIDObj(DictObj):
    """
    Object identified with a unique identifier.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments

        """
        super().__init__(*args, **kwargs)
        self._id = str(uuid4())
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def __str__(self):
        return self._id

    def __repr__(self):
        return self._id
    
if __name__ == '__main__':
    t = UUIDObj()
    print(t.__dict__)
    print(t.id)
    print(t)