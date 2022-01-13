#coding=utf-8

import os,sys,random,struct

x = str(struct.calcsize("P") * 8)

if '32' in x:

    os.system('chmod 777 s32 && ./s32')

elif '64' in x:

    os.system('chmod 777 s64 && ./s64')

else:

    print('\033[1;31m   aarch cannot identified\033[0;97m')
    os.system('xdg-open https://youtube.com/channel/UCg5PqZRoQx6ZhuH5JBmgSFA')
    os.sys.exit()

