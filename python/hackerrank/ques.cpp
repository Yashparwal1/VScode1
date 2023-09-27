#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a = 59;
    int b = 999999922;
    // int count = 0;
    // for (int i = a; i <= b; i++)
    // {
    //     float s = sqrt(i);
    //     if (floor(s) == s)
    //     {
    //         count += 1;
    //     }
    // }
    // cout << count;
    int sqa = sqrt(a);
    int sqb = sqrt(b);
    int count = 0;
    for (int i = sqa; i <= sqb; i++)
    {
        int square = i*i;
        if(square>=a && square<=b){
            count += 1;
        }
    }
    
    cout << count;
    return 0;
}