"""
Object with CRUD operations

Extends DTObj

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

from frua.base.obj.dtobj import DTObj

from frua.base.time.help import TimeHelp


class CRUDObj(DTObj):
    """
    Object with CRUD operations

    Extends DTObj
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments
        """
        super().__init__(*args, **kwargs)
        if not hasattr(self, 'deleted'):
            self.deleted = False
        if not hasattr(self, 'created'):
            self.created_at = TimeHelp.now()
        if not hasattr(self, 'read_at'):
            self.read_at = None
        if not hasattr(self, 'updated_at'):
            self.updated_at = None
        if not hasattr(self, 'deleted_at'):
            self.deleted_at = None
        if not hasattr(self, 'enabled'):
            self.enabled = True
        if not hasattr(self, 'enabled_at'):
            self.enabled_at = TimeHelp.now()
        if not hasattr(self, 'disabled_at'):
            self.disabled_at = None
    
    def create(self) -> None:
        """
        Mark the object as created
        """
        self.created_at = TimeHelp().utcnow()

    def read(self) -> None:
        """
        Mark the object as read
        """
        self.read_at = TimeHelp().utcnow()
    
    def update(self) -> None:
        """
        Mark the object as updated
        """
        self.updated_at = TimeHelp().utcnow()
    
    def delete(self) -> None:
        """
        Mark the object as deleted
        """
        self.deleted_at = TimeHelp().utcnow()
        self.deleted = True
    
    def undelete(self) -> None:
        """
        Unmark the object as deleted
        """
        self.deleted_at = None
        self.deleted = False
       
    def enable(self) -> None:
        """
        Mark the object as enabled
        """
        self.enabled = True
        self.enabled_at = TimeHelp().utcnow()

    def disable(self) -> None:
        """
        Mark the object as disabled
        """
        self.enabled = False
        self.disabled_at = TimeHelp().utcnow()

    def is_deleted(self) -> bool:
        """
        Check if the object is deleted

        Returns:
            bool: True if the object is deleted
        """
        return self.deleted

    def is_active(self) -> bool: 
        """
        Check if the object is active

        Returns:
            bool: True if the object is active
        """
        return not self.deleted

    def is_enabled(self) -> bool:
        """
        Check if the object is enabled

        Returns:
            bool: True if the object is enabled
        """
        return self.enabled
    
    def is_disabled(self) -> bool:
        """
        Check if the object is disabled

        Returns:
            bool: True if the object is disabled
        """
        return not self.enabled
