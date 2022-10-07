#include<iostream>
using namespace std;

int add(int a, int b)
{
    cout << endl<<"Using function with 2 arguments" <<endl;
    return a+b;
}
int add(int a, int b, int c)
{
    cout << endl<<"Using function with 3 arguments" <<endl;
    return a+b+c;
}

int volume(double r, int h)
{
    return (3.14*r*r*h);
}
int volume(int a)
{
    return (a*a*a);
}
int volume(int l, int b, int h)
{
    return (l*b*h);
}

int main()
{
    // the compiler matches the actual paramaters with the prototype that is no. of formal parameters equal to no. of actual parameters 
    cout << "The sum of 3 and 6 is: " <<add(3,6)<<endl;
    cout << "The sum of 3, 7 and 6 is: " <<add(3,7,6)<<endl;
    cout << "The volume of cylender of r=3 & h=10 is: " <<volume(3,10)<<endl;
    cout << "The volume of cube of side=6 is: " <<volume(6)<<endl;
    cout << "The volume of cuboid of l=4, b=7 & h=3 is: " <<volume(4,7,3)<<endl;

}