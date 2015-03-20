#!/usr/bin/env python3
#c=a-b
import sys
asp=' '
bsp='\t'
a='mer'
b='3k1'
fa=open(a,'r')
fb=open(b,'r')
A=set()
B=set()
for line in fa:
    word=line.split(asp)[0]
    if len(word)==0:
        break
    A.add(word)
for line in fb:
    word=line.split(bsp)[0]
    if len(word)==0:
        break
    B.add(word)
C=B-A
for i in C:
    print(i)
