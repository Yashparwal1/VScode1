#include<iostream>
using namespace std;
 
// class Employee{
//     int eid;
//     int salary;
//     public:
//         void set(void){
//             cout << "Enter ID: ";
//             cin >> eid;
//             salary = 100;
//         }
//         void display(void){
//             cout << "ID and salary are: " << eid<<" and "<<salary <<endl;
//         }
// };
// int main()
// {
//     Employee yash, sonu, monu;
//     // yash.set();
//     // yash.display();
//     // sonu.set();
//     // sonu.display();
//     // monu.set();
//     // monu.display();

//     Employee fb[4]; //its an array of object just like any other array.... no big deal!!
//     for (int i = 0; i < 4; i++)
//     {
//         fb[i].set();
//         fb[i].display();
//     }
//     return 0;
// }

// ---------------------- PASSING OBJECTS AS ARGS.--------------------------- 
class Complex
{
    int a;
    int b;
public:
    void set(int x, int y)
    {
        a = x;
        b = y;
    }
    void Sum(Complex n1, Complex n2)
    {
        a = n1.a+n2.a;
        b = n1.b+n2.b;
    }
    void display(){
        cout << "Result: "<<a<<"+"<<b<<"i"<<endl;
    }
};

int main()
{
    Complex c1,c2,c3;
    c1.set(1,2);
    c1.display();
    
    c2.set(3,4);
    c2.display();

    c3.Sum(c1,c2); //passing objects as arguments
    c3.display();
    return 0;
}