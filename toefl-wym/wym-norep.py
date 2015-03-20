#!/usr/bin/env python3
import sys
lis=open("wym.txt",'r')
dic={}
former=''
for line in lis:
    line=line.strip('\n')
    if(len(line)==0):
        break
    w=line.split('\t')
    word=w[0]
    prop=w[1]
    if(prop=='词组'):
        prop=''
    chi=w[3]
    if len(word)==0:
        dic[former].append(prop+chi)
    else:
        former=word
        dic[word]=[prop+chi,]
sl=sorted(dic.items(), key=lambda d:d[0])
for i in sl:
    print(i[0],end='\t')
    print(' '.join(i[1]))
