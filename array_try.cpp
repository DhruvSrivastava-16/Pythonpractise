#include<iostream>
#include<vector>
using namespace std;

void check(vector <int> v)
{
    v[0]=-1;
    cout<<v[1];
}


int main()
{
    vector <int> arr{1,2,3,4,5};
    //cout<<"yo";
    check(arr); 
    for(int i=0;i<5;i++)
    {
        cout<<arr[i]<<" , ";
    }
    return 0;
}