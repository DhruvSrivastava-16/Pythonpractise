# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:54:35 2020

@author: DHRUV
"""
import math

t_cases=int(input())
t_array=[]
ans=[]
temp=[]

for i in range(0,t_cases):
    t_array.append(int(input()))
    

for i in t_array:
    a=[x for x in range(0,i+1) if x**2<=i]
    b=a;
    for j in a:
        for z in b: 
            if(z**2+j**2==i):
                if z or j not in temp:
                    temp.append(z)
                    temp.append(j)
                    ans.append("("+str(z)+","+str(j)+")")
    
    for x in ans:
        print(x,end="")
    print("\n")
    
    ans=[]
