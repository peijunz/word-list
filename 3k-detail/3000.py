#!/usr/bin/env python3
p=open('3000.txt','r')
st=p.read()
li=st.split('\n\n')
count=0
lcou=0
luni=0
uniwor=0
liswor=0
di='./3k-sep/'
fm=open(di+'3000List','w')
for i in li:
    if('List' in i):
        count+=1
        fw=open(di+'3000List'+str(count),'w')
        continue
    if ('Unit' in i) and ('United' not in i):
        continue
    li=i.split('\n')
    word=li[0]
    if('fusty' in i):
        print(li)
    for j in li:
        if (j != word) and ('考法' in j):
            cc=word+'\t'+j.split('】')[1]+'\n'
            fw.write(cc)
            fm.write(cc)
fw.close()
#fm.close()
#for i in li:
    #if len(i)>10:
        #count+=1
        #uniwor+=1
        #liswor+=1
    #if('List' in i):
        #lcou+=1
        #print(liswor)
        #print(i)
        #liswor=0
    #elif('Unit' in i) and ('United' not in i):
        #luni+=1
        #if(uniwor<10):
            #print(uniwor)
            #print(i)
        #uniwor=0
#print(count)#3073为正确结果
