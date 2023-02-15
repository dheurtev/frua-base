"""
Groups utility class

Uses:
- grp: https://docs.python.org/3/library/grp.html
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import grp

class Groups(object):
    """
    Groups Utility class
    """
    def __init__(self):
        pass

    def gid(self, group:str) -> int:
        """
        Return the group name associated to the gid

        Args:
            group (str): group name
        Returns:
            int: gid
        """
        return grp.getgrnam(group).gr_gid

    def group(self, gid:int) -> str:
        """
        Return the group name associated to the gid

        Args:
            gid (int): gid
        Returns:
            str: group name
        """
        return grp.getgrgid(gid).gr_name

if __name__ == '__main__':
    g = Groups()
    gid = g.gid('root')
    print(gid)
    print(g.group(gid))