# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:03:52 2020

@author: DHRUV
"""
import math

globalprime=[]
tested=[]

def prime_check(l,u,j):
    flag=0;
    k=math.sqrt(j)
    k=math.ceil(k)
    for i in range(2,k+1):
        if(j%i==0):
            flag=1;
            break;
    if(flag==0):
        globalprime.append(j)
        return 1
    else:
        return -1



if __name__=="__main__":
    n_test=int(input());
    ans=[]
    for i in range(0,n_test):
        inp=input()
        l,u=inp.split(" ")
        l=int(l)
        u=int(u)
  #      print("Limits are: ",l,u)
        temp=[]
        for j in range(l,u+1):
            if j!=2:
             #   if(j not in tested):
                ans_semi=prime_check(l,u,j)
                   # tested.append(j)
                    
                if(ans_semi==1 and j!=1):
                    temp.append(j)
                    globalprime.append(j)
            else:
           #     globalprime.append(j)
                temp.append(j)
            
        ans.append(temp)

for x in ans: 
    for y in x: 
        print (y,end=" ")
    print("\n")
        