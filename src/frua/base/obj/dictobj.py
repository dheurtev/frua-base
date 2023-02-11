"""
Object loaded from dict

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

class DictObj(object):
    """
    Object loaded from dict
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor

        Args:
            args : positional arguments
            kwargs : optional arguments
        """
        super().__init__()
        self._args = args
        self.__dict__.update(kwargs)

    def from_dict(self, d:dict) -> object:
        """
        Load object from dict

        Args:
            d (dict) : dict

        Returns:
            self
        """
        for k, v in d.items():
            setattr(self, k, v)               
        return self

    def __eq__(self, other) -> bool:
        """
        Check equality

        Args:
            other (object) : object

        Returns:
            bool
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        """
        Check inequality

        Args:
            other (object) : object

        Returns:
            bool
        """
        return self.__dict__!= other.__dict__

