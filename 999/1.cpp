#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int n;
    int m;
    int sum;
    int x[1020];
    cin>>n;
    while(n--)
    {
        cin>>m;
        for(int i=0;i<m;i++)
        {
            cin>>x[i];
        }
        sort(x,x+m);
        sum=0;
        for(int j=0;j<m;j++)
        {
            sum+=x[j]*(m-1-j);
        }
        cout<<sum/m<<endl;
    }
    return 0;
}