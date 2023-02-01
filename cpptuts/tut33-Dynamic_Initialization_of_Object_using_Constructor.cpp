#include<iostream>
using namespace std;

class Bank{
    int principal;
    int time;
    float rate;
    float roi;
    public:
        Bank(){}
        Bank(int p, int t, int r);
        Bank(int p, int t, float r);
        void display();
};

Bank::Bank(int p, int t, int r){
    principal = p;
    time = t;
    rate = float(r)/100;
    cout << rate <<endl;
    roi = principal;
    for (int i = 0; i < t; i++) 
    {
        roi = roi*(1+rate); //compound interest
    }
    cout << roi <<endl;
}
Bank::Bank(int p, int t, float r){
    principal = p;
    time = t;
    rate = r;

    roi = principal;
    for (int i = 0; i < t; i++) 
    {
        roi = roi*(1+rate); //compound interest
    }
}
void Bank::display(){
    cout << "Principal Amount was: "<<principal<<endl
    <<"Return value after "<<time<<" years is: "<<roi<<endl;
}
int main()
{
    Bank amt1(100, 1, 4);
    amt1.display();
    Bank amt2(100, 1, 0.04);
    amt2.display();
    Bank amt3();
    amt3.display();
    return 0;
}

// -----------------------------------------------------------------------


