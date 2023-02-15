"""
sqlite3 object module

Uses:
- sqlite3: https://docs.python.org/3/library/sqlite3.html
"""
__author__ = "David HEURTEVENT"
__copyright__ = "David HEURTEVENT"
__license__ = "MIT"

import logging
import sqlite3

from sqlite3 import Error

class Sqlite(object):

    def __init__(self, db_file:str='', *args, **kwargs) -> None:
        """
        Constructor

        Args:
            db_file (str): database file (optional, by default in memory)
            logger (logging.Logger): the logger to use (optional)
            args: positional arguments
            kwargs: keyword arguments
        """
        super().__init__()
        #other attributes
        self._args = args
        self.__dict__.update(kwargs)
        #handle logger
        if not hasattr(self, 'logger'):
            self._logger = logging.getLogger(__name__)
        #handle other attributes
        self.db_file = db_file
        #conn and cursor
        self._conn = None

    @property
    def conn(self):
        """
        Returns the database connection
        """
        return self._conn
    
    @conn.setter
    def conn(self, conn):
        """
        Sets the connection

        Args:
            conn: the connection object
        """
        self._conn = conn

    @property
    def cursor(self):
        """
        Returns the database cursor
        """
        return self._conn.cursor()

    def connect(self) -> None:
        """ create a database connection to a SQLite database
        """
        #create a connection to the database
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(self.db_file)
                self._logger.debug('Connected to database: %s' % self.db_file)
                self._logger.debug('SQLITE - Version:%s' % sqlite3.sqlite_version)
            except Error as e:
                self._logger.error('Failed to connect to database: %s' % self.db_file)
                self._logger.error(e)

    def close(self) -> None:
        """ close the database connection """
        if self.conn:
            self.conn.close()
            self._logger.debug('Connection to database %s closed' % self.db_file)

    def execute(self, sql:str) -> int:
        """ create a table from the create_table_sql statement
        Args:
            sql (str): a SQL statement
        Returns:
            Rows or None (if error)
        """
        try:
            self._logger.debug('Executed SQL Statement : %s' % sql)
            return self.cursor.execute(sql)
        except Error as e:
            self._logger.debug('Failed to execute SQL Statement : %s' % sql)
            return None

    def commit(self) -> None:
        """ commit the changes to the database """
        if self.conn != None:
            self.conn.commit()
            self._logger.debug('Changes committed')
    
    def rollback(self) -> None:
        """Rollback changes in the database"""
        if self.conn != None:
            self.conn.rollback()
            self._logger.debug('Rollback requested')

    def executemany(self, sql:str, data:list) -> None:
        """Executes many SQL statements
        
        Args:
            sql (str): a SQL statement
            data (list): a list of tuples
        """
        if self.conn != None:
            self.conn.executemany(sql, data)

