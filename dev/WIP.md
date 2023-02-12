git:clone
git:downloadrepo
git:downloadrepounzip

fs:dir:wipe (test)
fs:dir:copy
fs:dir:move
fs:dir:perms
fs:dir:owner
fs:dir:group
fs:dir:isdir
fs:dir:setperms
fs:dir:setowner
fs:dir:setownerrootroot
fs:dir:setowneruserroot(user)
fs:dir:setowneruseruser(user)
fs:dir:setgroup
fs:dir:setpermsrecursive
fs:dir:setownerrecursive
fs:dir:setgrouprecursive
fs:dir:hassubfolders
fs:dir:subfolders
fs:dir:files
fs:dir:filesrecursive
fs:dir:create(touch)
fs:dir:update(touch)
fs:dir:delete

fs:files:copy
fs:files:move
fs:files:owner
fs:files:group
fs:files:perms (str or oct)
fs:files:setperm(chmod)
fs:files:setowner(chown)
fs:files:setgroup(chgrp)
fs:files:setownerrootroot
fs:files:setowneruserroot(user)
fs:files:setowneruseruser(user)
fs:files:isfile
fs:files:issymlink
fs:files:ishardlink
fs:files:create(touch)
fs:files:update(touch)
fs:files:delete
fs:files:symlink(src, dst)
fs:files:unlink(src)

data:file:top
data:file:tail
data:file:appendtop
data:file:appendbottom
data:file:concat(a,b,dst)

const:perms
all:777
uro:400 (ro)
urw:600 (rw)
gro:440
grw:660
uex:500
gex:550
uall:700
gall:770
files:644
folders:755

users:
