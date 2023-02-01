//  ===> Constructors in Derived Class <===

// 1. We can use constructors in derived classes in C++
// 2. If the base class constructor does not have any arguments, there is no need for any constructor in the derived class
// 3. But if there are one or more arguments in the base class constructor, derived class need to pass argument to the base class constructor
// 4. If both base and derived classes have constructors, base class constructor is executed first

//  ===> Constructors in Multiple Inheritances <===

// --> In multiple inheritances, base classes are constructed in the order in which they appear in the class deceleration.
// For example if there are three classes “A”, “B”, and “C”, and the class “C” is inheriting classes “A” and “B”.
// If the class “A” is written before class “B” then the constructor of class “A” will be executed first.
// But if the class “B” is written before class “A” then the constructor of class “B” will be executed first.

// --> In multilevel inheritance, the constructors are executed in the order of inheritance.
// For example if there are three classes “A”, “B”, and “C”, and the class “B” is inheriting classes “A” and the class “C” is inheriting classes “B”.
// Then the constructor will run according to the order of inheritance such that the constructor of class “A” will be called first,
// then the constructor of class “B” will be called,
// and at the end constructor of class “C” will be called.

// --> Syntax Example:

// Derived-Constructor (arg1, arg2, arg3....): Base 1-Constructor (arg1,arg2), Base 2-Constructor(arg3,arg4)
// {
// ….
// } Derived -Constructor (arg5,arg6)

//  ===> Special Case of Virtual Base Class <===

// The constructors for virtual base classes are invoked before a non-virtual base class
// If there are multiple virtual base classes, they are invoked in the order declared
// Any non-virtual base class are then constructed before the derived class constructor is executed

// -------------------------------------------- 48 ------------------------------------------------

/*
Case1:
class B: public A{
   // Order of execution of constructor -> first A() then B()
};

Case2:
class A: public B, public C{
    // Order of execution of constructor -> B() then C() and A()
};

Case3:
class A: public B, virtual public C{
    // Order of execution of constructor -> C() then B() and A()
};

*/
#include <iostream>
using namespace std;

class Base1
{
    int data1;

public:
    Base1(int i)
    {
        data1 = i;
        cout << "Base1 class constructor called" << endl;
    }
    void printDataBase1(void)
    {
        cout << "The value of data1 is " << data1 << endl;
    }
};

class Base2
{
    int data2;

public:
    Base2(int i)
    {
        data2 = i;
        cout << "Base2 class constructor called" << endl;
    }
    void printDataBase2(void)
    {
        cout << "The value of data2 is " << data2 << endl;
    }
};

class Derived : public Base2, public Base1
{
    int derived1, derived2;

public:
    Derived(int a, int b, int c, int d) : Base1(b), Base2(a) // this sequesnce doesn't matter
    {
        derived1 = c;
        derived2 = d;
        cout << "Derived class constructor called" << endl;
    }
    void printDataDerived(void)
    {
        cout << "The value of derived1 is " << derived1 << endl;
        cout << "The value of derived2 is " << derived2 << endl;
    }
};

int main()
{
    Derived harry(1, 2, 3, 4);
    harry.printDataBase1();
    harry.printDataBase2();
    harry.printDataDerived();
    return 0;
}
