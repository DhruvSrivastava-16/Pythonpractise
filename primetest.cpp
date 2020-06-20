#include <iostream>
using namespace std; 

int main()
{
    long int n,i;
    int flag=1;
    cin>>n;

    for(i=2;i<n/2;i++)
    {
        if(n==2)
        {
            break;
        }
       else if(n%i==0)
        {
            flag=-1;
            cout<<"Flag became -1";
            break;
        }
    }

    if(flag==1)
        cout<<"Prime";
    else
        cout<<"Not Prime";
        
    return 0;
    
}