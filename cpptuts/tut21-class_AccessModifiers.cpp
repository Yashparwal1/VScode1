#include<iostream>
using namespace std;
 
class Employee{
    private:
        int a,b,c;
    public:
        int d;
        void sData(int a, int b, int c, int d);
        void gData()
        {
            cout << "Value of a is "<<a<<endl;
            cout << "Value of b is "<<b<<endl;
            cout << "Value of c is "<<c<<endl;
            cout << "Value of d is "<<d<<endl;
        }
};

void Employee::sData(int w, int x, int y, int z){
    a = w;
    b = x;
    c = y;
    d = z;
}

int main()
{
    class Employee ep;
    // ep.a = 101 // ERROR-- cannot access 'a' directly becoz 'a' is private, so accessing 'a' from public using a function sData and gData which are defined in that class itself
    ep.sData(1,2,3,4);
    ep.gData();
    return 0;
}