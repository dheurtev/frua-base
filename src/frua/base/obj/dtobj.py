"""
Object with a datetime
Datetime is a string that contains the date and time when the object was created.
By default, it is set to the current time in utc time.

Extends UUIDObj

Uses:
- datetime: https://docs.python.org/3/library/datetime.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import datetime

from frua.base.time.help import TimeHelp
from frua.base.obj.uidobj import UUIDObj

class DTObj(UUIDObj):
    """
    Object with a datetime

    Datetime is a string that contains the date and time when the object was created.
    By default, it is set to the current time in utc time.

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
        self._dt = TimeHelp().utcnow()

    @property
    def dt(self) -> datetime.datetime:
        return self._dt

    @dt.setter
    def dt(self, value:datetime.datetime) -> None:
        self._dt = value
    
    def reset_dt(self) -> datetime.datetime:
        """
        Reset the datetime to the current datetime and return it
        """
        self._dt = TimeHelp().utcnow()
        return self._dt
