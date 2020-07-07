#!/usr/bin/env python3
import os
fileName=input('plase enter a name of file with filetag like("filename.txt")')
target=input('please select a name for target file with type')
key=int(input('plese enter a key for lock program .only int'))
f=open(fileName,'rb')
file=f.read()
f.close()
file=bytearray(file)
for index,value in enumerate(file):
	file[index]=value^key
l=fileName.split('.')
os.rename(fileName,target)
