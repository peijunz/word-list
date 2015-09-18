#!/usr/bin/env python3
import sys
import os
def nolst(s):
    return s.split('.lst')[0]
def splitf(fname):
    d='/'.join(fname.split('/')[:-1])+'/sub/'
    ker=(fname.split('/')[-1]).split('.lst')[0]
    f=open(fname,'r')
    if not os.path.exists(d):
        os.makedirs(d)
    count=0
    for i in f:
        if('# List' in i):
            count+=1
            fw=open(d+ker+'-'+str(count)+'.lst','w')
            continue
        else:
            fw.write(i)
if __name__=='__main__':
    if len(sys.argv)>1:
        ls=sys.argv[1:]
    else:
        s=input('请输入文件名，多个文件以空格分割：\n')
        ls=s.split()
    for i in ls:
        splitf(i)
        

