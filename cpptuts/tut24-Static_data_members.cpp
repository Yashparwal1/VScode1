#include <iostream>
using namespace std;

/*
    ====> Static Data Members <====
 *  The data member of a class preceded by the keyword static is known as static member.

**  When we precede a member variable's declaration with static, we are telling the compiler that only
    one copy of that variable will exist and that all objects of the class will share that variable. Hence
    static variables are called class variables.

 *  Unlike regular data members, individual copies of a static member variable are not made for each
    object. No matter how many objects of a class are created, only one copy of a static data member
    exists. Thus, all objects of that class use that same variable.

 *  All static variables are initialized to zero before the first object is created.

 *  Normal data members are called object variable but static data members are called class variables.

 */
class Employee
{
    int eid;
    static int count; // default value of static var. is 0
    // if we do not make it static then for each object it will print '1' but using static it will take memory only oney time so will be updated with the latest value whenever called with another object.
public:
    void setData(void)
    {
        cout << "Enter ID: ";
        cin >> eid;
        count++;
    }
    void Display(void)
    {
        cout << "ID " <<eid<<" is employee no.: " << count << endl;
    }
    static void total(){
        // cout << eid <<endl; //ERROR: becoz static function can only access static variables
        cout << "Total no. of employees = "<<count<<endl;
    }
};

int Employee::count;
// need to define count outside of the class
// without this we'll receive an error: "undefined reference to `Employee::count` "
int main()
{
    Employee ep, yash, sonu, monu;

    ep.setData();
    ep.Display();
    yash.setData();
    yash.Display();
    sonu.setData();
    sonu.Display();
    monu.setData();
    monu.Display();
    Employee::total();
    return 0;
}

// ---------------------------------------------------------------------
// class A
// {
//     int p;
//     static int q;

// public:
//     A();
//     void incr(void);
//     void display(void);
// };
// A ::A()
// {
//     p = 5;
// }
// int A::q = 10;
// void A::incr()
// {
//     p++;
//     q++;
// }
// void A::display()
// {
//     cout << p <<"\t" << q << endl;
// }
// int main()
// {
//     A a1, a2, a3;
//     a1.incr();
//     a1.display();
//     a2.incr();
//     a2.display();
//     a3.incr();
//     a3.display();
// }
