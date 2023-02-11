"""
Object identified with a unique identifier (UUID4).

Extends DictObj

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

    Extends DictObj
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments

        """
        super().__init__(*args, **kwargs)
        self._id = str(uuid4())
    
    @property
    def id(self) -> str:
        """
        Getter for id

        Returns:
            str : id
        """
        return str(self._id)

    @id.setter
    def id(self, value:uuid4):
        """
        Setter for id

        Args:
            value : id
        """
        self._id = str(value)

    def __str__(self) -> str:
        """
        String representation

        Returns:
            str : id
        """
        return str(self._id)

    def __repr__(self) -> str:
        """
        String representation

        Returns:
            str : id
        """
        return str(self._id)

