"""
Time helpers functions

Uses:
- datetime: https://docs.python.org/3/library/datetime.html

"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import datetime

class TimeHelp(object):
    """
    Time helpers functions
    """

    @staticmethod
    def now() -> datetime.datetime:
        """
        Returns the current time

        Returns:
            datetime.datetime: the current time
        """
        return datetime.datetime.now()

    @staticmethod
    def now_str() -> str:
        """
        Returns the current time as a string

        Returns:
            str: the current time as a string
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")

    @staticmethod
    def now_us_str() -> str:
        """
        Returns the current time as a str in US format

        Returns:
            str: the current time as a str in US format
        """
        return datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p %Z")

    @staticmethod
    def now_eu_str() -> str:
        """
        Returns the current time as a str in Europe format

        Returns:
            str: the current time as a str in Europe format
        """
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %Z")

    @staticmethod
    def now_dt() -> datetime.datetime:
        """
        Returns the current time as a datetime

        Returns:
            datetime.datetime: the current time as a datetime
        """
        return datetime.datetime.now()

    @staticmethod
    def now_ts() -> float:
        """
        Returns the current time as a timestamp

        Returns:
            float: the current time as a timestamp
        """
        return datetime.datetime.now().timestamp()

    @staticmethod
    def now_iso() -> str:
        """
        Returns the current time as a str in ISO format

        Returns:
            str: the current time as a str in ISO format
        """
        return str(datetime.datetime.now().isoformat())

    @staticmethod
    def utcnow() -> datetime.datetime:
        """
        Returns the current time in UTC

        Returns:
            datetime.datetime: the current time in UTC
        """
        return datetime.datetime.utcnow()
    
    @staticmethod
    def utcnow_str() -> str:
        """
        Returns the current time in UTC as a string

        Returns:
            str: the current time in UTC as a string
        """
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def utcnow_dt() -> datetime.datetime:
        """
        Returns the current time in UTC as a datetime

        Returns:
            datetime.datetime: the current time in UTC as a datetime
        """
        return datetime.datetime.utcnow()
    
    @staticmethod
    def utcnow_ts() -> float:
        """
        Returns the current time in UTC as a timestamp

        Returns:
            float: the current time in UTC as a timestamp
        """
        return datetime.datetime.utcnow().timestamp()

    @staticmethod
    def utcnow_iso() -> str:
        """
        Returns the current time in UTC as a string in ISO format

        Returns:
            str: the current time in UTC as a string in ISO format
        """
        return str(datetime.datetime.utcnow().isoformat())

    @staticmethod
    def epoch() -> datetime.datetime:
        """
        Returns the epoch time

        Returns:
            datetime.datetime: the epoch time
        """
        return datetime.datetime.utcfromtimestamp(0)
   
if __name__ == '__main__':
    print(TimeHelp.now())
    print(TimeHelp.now_str())
    print(TimeHelp.now_us_str())
    print(TimeHelp.now_eu_str())
    print(TimeHelp.now_dt())
    print(TimeHelp.now_ts())
    print(TimeHelp.now_iso())
    print(TimeHelp.utcnow())
    print(TimeHelp.utcnow_str())
    print(TimeHelp.utcnow_dt())
    print(TimeHelp.utcnow_ts())
    print(TimeHelp.utcnow_iso())
    print(TimeHelp.epoch())
    

