#!/usr/bin/env python3
def rev(s):
    return s[::-1]
f=open('../toefl-wym/wym.txt')
linn=f.readlines()
lin=[i.strip('\n')[::-1] for i in linn]
lin.sort()
li=[i[::-1] for i in lin]
for i in li:
    print(i)
#if __name__=='__main__':
    
