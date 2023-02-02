#include<iostream>
using namespace std;
int c = 45;
int main()
{
    /*
    int a,b,c;
    cout << "Enter the value of a: "<<endl;
    cin >> a;
    cout << "Enter the value of b: "<<endl;
    cin >> b;
    c = a + b;
    cout << "Sum of a and b is: "<<c;
    // by default scope is local, so to access gloabel variable with the same name, use scope resolution opertor
    cout << "The global c is: "<<::c;   
    */

    // ************************** Float, Double and Long double Literals ****************************
    // float d=5.2; 
    // long double e=5.2;
    // float d=5.2f; //without f 5.2 is double, but as we written float at first, so d is already flaot.
    // long double e=5.2l;
    // cout << "the value of d is: "<<d<<endl<< "the value of e is: "<<e<<endl;
    // //unlike in C decimal laterals are of double type in cpp by default, so 5.2 is a double not float
    // // so to make 5.2 a float value, write it as 5.2f
    // // these things will help in function overloading
    // cout << "The size of d is: "<<sizeof(d);

    // **************************Reference variables******************************
    // call same variable with diff reference(names), just like yash --> babu --> parwal

    // float x = 5.2;
    // float &y = x; //y is storing the reference(address) of x
    // cout << x; //same 
    // cout << y; //same


    // **************************Typecasting******************************
    int l = 45;
    float m = 45.767;
    cout << "Value of m is: "<<int(m)<<endl;
    cout << "Value of m is: "<<(int)m<<endl; //we can also do this

    int p = int (m); //we can assign value<<endls like this also
    cout << "Value of p is: "<<p<<endl;

    cout << "l+m is: " <<l + m<<endl; //flot
    cout << "l+m is: " <<l + int(m)<<endl; //int
    cout << "l+m is: " <<l + (int)m<<endl; //int

}   