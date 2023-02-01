#include<iostream>
using namespace std;
 
class simple{
    int data1;
    int data2;
    public:
        simple(int a, int b=6){ //b is default parameter unnless argument is not given already.
            data1 = a;
            data2 = b;
        }
        void display(){
            cout << "THe values of data1 and data2 are: "<<data1<< " and " <<data2 << " respectively."<<endl;
        }
};
int main()
{
    simple s1(2);
    s1.display();
    simple s2(10,20);
    s2.display();
    return 0;
}