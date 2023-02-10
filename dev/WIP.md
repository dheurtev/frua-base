cmd:exec

git:clone
git:downloadrepo
git:downloadrepounzip

fs:dirs:copy
fs:dirs:move
fs:dirs:perms
fs:dirs:owner
fs:dirs:group
fs:dirs:isdir
fs:dirs:setperms
fs:dirs:setowner
fs:dirs:setownerrootroot
fs:dirs:setowneruserroot(user)
fs:dirs:setowneruseruser(user)
fs:dirs:setgroup
fs:dirs:setpermsrecursive
fs:dirs:setownerrecursive
fs:dirs:setgrouprecursive
fs:dirs:hassubfolders
fs:dirs:subfolders
fs:dirs:files
fs:dirs:filesrecursive
fs:dirs:create(touch)
fs:dirs:update(touch)
fs:dirs:delete

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
