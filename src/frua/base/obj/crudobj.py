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
    
    def __init__(self, *args, **kwargs):
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments
        """
        super().__init__(*args, **kwargs)
        if not hasattr(self, 'enabled'):
            self.enabled = False
            self.enabled_at = TimeHelp.now()
        if not hasattr(self, 'disabled'):
            self.deleted = False
            self.created_at = TimeHelp.now()
        if not hasattr(self, 'read_at'):
            self.read_at = None
        if not hasattr(self, 'updated_at'):
            self.updated_at = None
        if not hasattr(self, 'deleted_at'):
            self.deleted_at = None
    
    def read(self):
        """
        Mark the object as read
        """
        self.read_at = TimeHelp().utcnow()
    
    def create(self):
        """
        Mark the object as created
        """
        self.created_at = TimeHelp().utcnow()

    def update(self):
        """
        Mark the object as updated
        """
        self.updated_at = TimeHelp().utcnow()
    
    def delete(self):
        """
        Mark the object as deleted
        """
        self.deleted_at = TimeHelp().utcnow()
        self.deleted = True
    
    def disable(self):
        """
        Mark the object as disabled
        """
        self.enabled = False
        self.disabled_at = TimeHelp().utcnow()
    
    def enable(self):
        """
        Mark the object as enabled
        """
        self.enabled = True
        self.enabled_at = TimeHelp().utcnow()

    def is_deleted(self):
        """
        Check if the object is deleted

        Returns:
            bool: True if the object is deleted

        """
        return self.deleted

    def is_active(self): 
        """
        Check if the object is active

        Returns:
            bool: True if the object is active
        """
        return not self.deleted

    def is_enabled(self):
        """
        Check if the object is enabled

        Returns:
            bool: True if the object is enabled

        """
        return self.enabled
    
    def is_disabled(self):
        """
        Check if the object is disabled

        Returns:
            bool: True if the object is disabled
        """
        return not self.enabled

if __name__ == '__main__':
    d = CRUDObj()
    print(d.__dict__)
