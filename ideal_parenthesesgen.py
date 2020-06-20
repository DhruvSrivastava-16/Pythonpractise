# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:19:52 2020

@author: DHRUV
"""

sum1=0
l=[]
while sum1>=0:
    i=int(input())
    sum1=sum1+i;
    if(sum1>0):
        l.append(i)

for i in l:
    print(i)