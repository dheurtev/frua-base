"""
tests frua.base.archive.zip.py
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

import pytest
import os
import sys
from pathlib import Path

from frua.base.cmd.cmd import Cmd, CmdLine

curdir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def cmdobj():
    cmdobj = Cmd()
    return cmdobj

@pytest.fixture
def cmdlineobj():
    cmdlineobj = CmdLine()
    return cmdlineobj

def test_cmdline_init(cmdlineobj):
    assert isinstance(cmdlineobj, CmdLine)
    assert not hasattr(cmdlineobj.__dict__, 'args')

def test_cmdline_init_str():
    cmdlineobj = CmdLine("ls -a")
    assert isinstance(cmdlineobj, CmdLine)
    assert '_args' in cmdlineobj.__dict__
    assert cmdlineobj._args == ["ls", "-a"]

def test_cmdline_get_line():
    cmdlineobj = CmdLine("ls -a")
    assert isinstance(cmdlineobj, CmdLine)
    assert '_args' in cmdlineobj.__dict__
    assert cmdlineobj.line == 'ls -a'

def test_cmdline_set_line(cmdlineobj):
    assert isinstance(cmdlineobj, CmdLine)
    cmdlineobj.line = "ls -a"
    assert '_args' in cmdlineobj.__dict__
    assert cmdlineobj._args == ["ls", "-a"]

def test_cmdline_get_args(cmdlineobj):
    cmdlineobj._args = ["ls", "-a"]
    assert isinstance(cmdlineobj, CmdLine)
    assert '_args' in cmdlineobj.__dict__
    assert cmdlineobj.args == ["ls", "-a"]    

def test_cmdline_set_args(cmdlineobj):
    cmdlineobj.args = ["ls", "-a"]
    assert isinstance(cmdlineobj, CmdLine)
    assert '_args' in cmdlineobj.__dict__
    assert cmdlineobj._args == ["ls", "-a"]    

def test_cmd_init(cmdobj):
    assert isinstance(cmdobj, Cmd)
    assert '_args' in cmdobj.__dict__
    assert cmdobj._args == ()
    assert '_logger' in cmdobj.__dict__
    assert cmdobj._logger != None    

def test_cmd_init_with_args():
    cmdobj1 = Cmd('arg1', 'arg2')
    assert isinstance(cmdobj1, Cmd)
    assert '_args' in cmdobj1.__dict__
    assert cmdobj1.cmdlineargs == ['arg1']
    assert cmdobj1._args[0] == 'arg2'
    assert '_logger' in cmdobj1.__dict__
    assert cmdobj1._logger != None    

def test_cmd_init_with_line():
    """also tests _clean_cmdline indirectly"""
    cmdobj1 = Cmd('ls -a /home')
    assert isinstance(cmdobj1, Cmd)
    assert '_args' in cmdobj1.__dict__
    assert cmdobj1.cmdlineargs == ['ls', '-a', '/home']
    assert cmdobj1._args == ()
    assert '_logger' in cmdobj1.__dict__
    assert cmdobj1._logger != None    

def test_raw(cmdobj):
    line = ["ls"]
    res = cmdobj.raw(line)
    assert res.returncode == 0
    
def test_raw_mkdir(cmdobj):
    path = "/tmp/testcmd"
    if os.path.exists(path):
        os.rmdir(path)
    line = ["mkdir %s"%path]
    res = cmdobj.raw(line,shell=True)
    assert res.returncode == 0
    assert os.path.exists(path)
    if os.path.exists(path):
        os.rmdir(path)

def test_raw_shell_mode(cmdobj):
    line = ["echo '1'"]
    res = cmdobj.raw(line, shell=True)
    assert res.returncode == 0

def test_raw_with_pre_existing_list(cmdobj):
    """Test with raw python code"""
    line = [sys.executable, "-c", "print('ocean')"]
    res = cmdobj.raw(line)
    assert res.returncode == 0
    assert 'ocean' in str(res.stdout)

def test_raw_with_line(cmdobj):
    """Line argument should not work"""
    line = "echo 1"
    try:
        res = cmdobj.raw(line)
        pytest.fail("")
    except:
        assert True 
 
def test_cmd(cmdobj):
    path = "/tmp/testcmd"
    if os.path.exists(path):
        os.rmdir(path)
    line = "mkdir %s"%path
    res = cmdobj.cmd(line)
    assert res.returncode == 0
    assert os.path.exists(path)
    if os.path.exists(path):
        os.rmdir(path)

def test_shell(cmdobj):
    line = "echo 1"
    res = cmdobj.shell(line)
    assert res.returncode == 0

def test_bash_script(cmdobj):
    filepath = os.path.join(curdir, 'testcmd.sh')
    res = cmdobj.bash_script(filepath)
    assert res.returncode == 0
    assert res.stdout == b'Running\n'

def test_bash_command(cmdobj):
    command = "echo 1"
    res = cmdobj.bash(command)
    assert res.returncode == 0
    assert res.stdout == b'1\n'

def test_python_script(cmdobj):
    filepath = os.path.join(curdir, 'testcmd.py')
    res = cmdobj.python_script(filepath)
    assert res.returncode == 0
    assert res.stdout == b'Running\n'

def test_python_command(cmdobj):
    command = "print('ocean')"
    res = cmdobj.python(command)
    assert res.returncode == 0
    assert 'ocean' in str(res.stdout)

def test_raw_line(cmdobj):
    path = "/tmp/testcmd"
    if os.path.exists(path):
        os.rmdir(path)
    line = "mkdir %s"%path
    res = cmdobj.raw_line(line, shell=True)
    assert res.returncode == 0
    assert os.path.exists(path)
    if os.path.exists(path):
        os.rmdir(path)

def test_raw_os_success(cmdobj):
    """Test with raw command that succeeds"""
    line = "echo 1"
    res = cmdobj.raw_os(line)
    assert res == 0

def test_raw_os_fail(cmdobj):
    """Test command that does not exist"""
    line = "test"
    res = cmdobj.raw_os(line)
    assert res > 0
