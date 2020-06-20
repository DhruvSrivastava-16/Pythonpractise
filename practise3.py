# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:59:45 2020

@author: DHRUV
"""


n=int(input())
print("\n")
j=0;
while(n>=1):
    for i in range(0,n):
        print (i+1,end=" ")
    print("*"*(2*j-1),end=" ")
    j+=1
    print("\n")
    n-=1