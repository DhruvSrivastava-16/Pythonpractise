#include<iostream>
using namespace std;
#define max 1000
int right_check(long int b[1000],int s,int itr)
{
    int flag=0,k=itr+1;
    while(flag==0)
    {
        if(b[k]>b[itr])
        {
            itr=k;
            k+=1;
        }
        else if(k==s-1 and flag==0)
        {
            return 1;
        }
        else
        {
            return -1;
        }
        
    }
}

void left_check(long int b[1000],int s)
{
    int flag=0,itr=1,k=0,ovr=1;
    while(flag==0)
    {
        if(b[k]<b[itr])
        {
            k=itr;
            itr+=1;
        }
        else if(itr==s-1)
            cout<<false;
        else
        {
            flag=1;
            break;
        }    
    }
    ovr=right_check(b,s,itr);
    if(ovr==1)
    {
        cout<<true;
    }
    else
    {
        cout<<false;
    }
    
}

int main()
{
    long int a[1000];
    int s;
    cin>>s;
    for(int i=0;i<s;i++)
        cin>>a[i];

    left_check(a,s);
    return 0;
}