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
    
    def __init__(self, *args, **kwargs):
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
            d : dict

        Returns:
        self
        """
        for k, v in d.items():
            setattr(self, k, v)               
        return self

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__!= other.__dict__


if __name__ == '__main__':
    d = DictObj(a=1, b=2, c=3)
    print(d.__dict__)