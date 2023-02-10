"""
tests frua.base.log.logobj.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import logging
import logging.config

from frua.base.log.logobj import LogObj

##############
LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        },
        'my.packg': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}
##############


@pytest.fixture
def logobj():
    obj = LogObj()
    return obj

def test_init(logobj):
    assert isinstance(logobj, LogObj)
    assert isinstance(logobj.logger, logging.Logger)

def test_load_logger(logobj):
    logobj.load_logger(__name__)
    assert logobj.logger

def test_load_logger_from_dict(logobj):
    logobj.load_logger_from_dict(LOGGING_CONFIG)
    assert logobj.logger

def test_set_level(logobj):
    logobj.setLevel(logging.DEBUG)
    assert logobj.logger

def test_get_logger(logobj):
    assert logobj.logger == logobj._logger

def test_set_logger(logobj):
    logobj.logger = logging.getLogger(__name__)
    assert logobj.logger

def test_debug(logobj):
    logobj.debug('test')
    assert logobj.logger

def test_info(logobj):
    logobj.info('test')
    assert logobj.logger

def test_warning(logobj):
    logobj.warning('test')
    assert logobj.logger

def test_critical(logobj):
    logobj.critical('test')
    assert logobj.logger

def test_exception(logobj):
    logobj.exception('test')
    assert logobj.logger

def test_log(logobj):
    logobj.log(logging.INFO, 'test')
    assert logobj.logger

def test_disable(logobj):
    logobj.disable()
    assert not logobj.is_enabled()

def test_enable(logobj):
    logobj.enable()
    assert logobj.is_enabled()

def test_is_disabled(logobj):
    logobj.disable()
    assert logobj.is_disabled()

def test_is_enabled(logobj):
    logobj.enable()
    assert logobj.is_enabled()

def test_add_basic_console_logger(logobj):
    logobj.add_basic_console_logger()
    assert logobj.logger

def test_add_console_logger(logobj):
    logobj.add_console_logger()
    assert logobj.logger

def test_add_file_logger(logobj):
    logobj.add_file_logger()
    assert logobj.logger