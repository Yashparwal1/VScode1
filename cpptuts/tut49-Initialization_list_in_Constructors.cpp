/* 
 ===> Syntax for Initialization list in constructors:
Constructor (args-list) : initialization-section
{
    assignment + other code
}
}
*/
#include<iostream>
using namespace std;

class Test{
    int a;
    int b;
    public:
        // Test(int i, int j) : a(i), b(j)
        // Test(int i, int j) : a(i), b(i+j)
        // Test(int i, int j) : a(i), b(a+j)
        Test(int i, int j) : b(j), a(i+b) // ERROR: this will create problem coz 'a' will be initialized first.
        {
            // constructor-body
            cout << "Constructor executed !!!" <<endl;
            cout << "a = "<<a<<endl;
            cout << "b = "<<b<<endl;
        }
};
int main()
{   
    Test obj(3,4);
    return 0;
}


// ---------------------------------AGGREGATION--------------------------------------
/*
In C++, aggregation refers to the relationship between a class and an object of another class as a member variable. It is a way of creating a has-a relationship between objects, where an object of one class contains an object of another class as a member. This allows for creating complex objects by combining simpler objects, rather than inheriting the properties and behaviors of the contained object.

For example, consider a class "Car" that has a member variable of type "Engine". The Car class has-a Engine object, creating an aggregation relationship between the two classes. The Engine object is contained within the Car object, and can be accessed and used through the Car object, but it retains its own identity and can be used independently if needed.
*/

// #include <iostream>

// class Engine {
//  public:
//   void start() {
//     std::cout << "Engine started" << std::endl;
//   }
// };

// class Car {
//  public:
//   Car() : engine() {}
//   Engine engine;
// };

// int main() {
//   Car car;
//   car.engine.start();
//   return 0;
// }
