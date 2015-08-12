#!/usr/bin/env python3
fp=open('aaa.kvtml','w')
head='''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE kvtml PUBLIC "kvtml2.dtd" "http://edu.kde.org/kvtml/kvtml2.dtd">
<kvtml version="2.0">
  <information>
    <generator>Parley 1.1.1</generator>
    <title>test title</title>
    <author>zpj</author>
    <contact>zpj@mail.ustc.edu.cn</contact>
    <license>公共领域</license>
    <date>2015-08-12</date>
    <category>语言</category>
  </information>
  <identifiers>
    <identifier id="0">
      <name>英语</name>
      <locale>en</locale>
    </identifier>
    <identifier id="1">
      <name>中文</name>
      <locale>zh</locale>
    </identifier>
  </identifiers>
  <entries>'''
def wentry(fp,num,eng,chn):
    fp.write('<entry id="'+str(num)+'">'+'\n')
    fp.write('<translation id="0">'+'\n')
    fp.write('<text>'+eng+'</text>'+'\n')
    fp.write('</translation>'+'\n')
    fp.write('<translation id="1">'+'\n')
    fp.write('<text>'+chn+'</text>'+'\n')
    fp.write('</translation>'+'\n')
    fp.write('</entry>'+'\n')
mid='''</entries>
  <lessons>'''
def wcontainer(fp,name,start,end):
    fp.write('<container>'+'\n')
    fp.write('<name>'+name+'</name>'+'\n')
    fp.write('<inpractice>true</inpractice>'+'\n')
    for i in range(start,end+1):
        fp.write('<entry id="'+str(i)+'"/>'+'\n')
    fp.write('</container>'+'\n')
tail='''</lessons>
</kvtml>'''
flist=['3000List'+str(i+1) for i in range(31)]# A list of file names
endp=[0 for i in flist]
num=0
fp.write(head)
for i,fn in enumerate(flist):
    fr=open(fn,'r')
    for k in fr:
        l=k.split('\t')
        if len(l)<2:
            continue
        eng=l[0]
        chn=l[1]
        endp[i]+=1
        wentry(fp,num,eng,chn)
        num+=1
    endp[i]=num#这是下一条的号码
fp.write(mid)
for i,nm in enumerate(flist):
    if(i==0):
        star=0
    else:
        star=endp[i-1]
    en=endp[i]-1
    wcontainer(fp,nm,star,en)
fp.write(tail)
fp.close()
