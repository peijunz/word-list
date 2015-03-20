#!/usr/bin/env python3
a='hello'
b='3k1'
D=dict()
fa=open(a,'r')
fb=open(b,'r')
for line in fb:
    line=line.strip('\n')
    if len(line)==0:
        break
    tmp=line.split('\t')
    D[tmp[0]]=tmp[1]
for line in fa:
    line=line.strip('\n')
    if line in D:
        print(line+'\t'+D[line])
