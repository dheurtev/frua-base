"""
POSIX Path permissions constants
"""
__author__ = 'David HEURTEVENT'
__copyright__ = 'David HEURTEVENT'
__license__ = 'MIT'

URO=400 
URW=600
GRO=440
GRW=660
UEX=500
GEX=550
UALL=700
GALL=770

#Typical file permissions
PRIVATE_RO=400 #private read only (e.g. private keys)
FILES=644  #configuration files (files not updated by scripts, html, gif,etc...) #owner can read/write, group/others can read only.
FOLDERS=755 #web store folder, CGI scripts #owner can read/write/execute, group/others can read/execute. owner can read/write/search, others and group can only search. 
RO=444
RW=666 #data files
FULL=777 #CAREFUL!! #all can read/write/execute (full access). all can read/write/search. directories with proper permissions on files in directory.
LOGS=751
WEBALIZER=701 #web alizer etc
