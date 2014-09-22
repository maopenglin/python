#!/usr/bin/python
version='1.0.0'
import os
import time

source=['/Users/cmstop/Desktop/demo/QQApiSDK']
targetdir='/Users/cmstop/Desktop/demo/'
target = targetdir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s"% (target, ' '.join(source))
print zip_command
cmd="zip -qr '",target,"'" ,' '.join(source)

print cmd
if os.system(zip_command) == 0:
     print 'Successful backup to', target
else:
    print 'Backup FAILED'

