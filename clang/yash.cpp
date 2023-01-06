#include <iostream>
using namespace std;
// 1. Program to Print a massage “ Welcome to C++ Programming” without using Class.

// int main()
// {
//     cout << "Welcome to C++ Programming" <<endl;
// }

// 2. Program to display a “Most Welcome to GNIOT College” massage by using class.

// class Msg
// {
// public:
//     void getname()
//     {
//         cout << "Most Welcome to GNIOT College" <<endl;
//     }
// };

// int main()
// {
//     Msg name;
//     name.getname();
// }

// 3. Program to display Names, Roll No., class name and grades of students input by user.

// class Student
// {
//     private:
//         string name;
//         int roll;
//         string cls;
//         float grade;
//     public:
//         Student()
//         {
//             cout << "Enter name: ";
//             cin >> name;
//             cout << "Enter Roll no.: ";
//             cin >> roll;
//             cout << "Enter Class: ";
//             cin >> cls;
//             cout << "Enter Grades: ";
//             cin >> grade;
//         }
//         void display()
//         {
//             cout << "\n-------- INFO. STORED--------" <<endl;
//             cout << "Name   : "<<name <<endl;
//             cout << "Roll No: "<<roll <<endl;
//             cout << "Class  : "<<cls <<endl;
//             cout << "Grades : "<<grade <<endl;
//         }
// };

// int main()
// {
//     Student obj;
//     obj.display();
// }

// 4. Write a program to declare Struct. Initialize and display contents of member variables.

// struct Person
// {
//     string name;
//     int age;
//     char gender;
// };

// int main()
// {
//     // Declare a variable of type "Person" and initialize its member variables.
//     struct Person p;
//     p.name = "Yash";
//     p.age = 19;
//     p.gender = 'M';
//     // Display the contents of the member variables.
//     cout << "Name: " << p.name << endl;
//     cout << "Age: " << p.age << endl;
//     cout << "Gender: " << p.gender << endl;

//     return 0;
// }

// 5. Write a program to declare a class. and pointer to class. Initialize and display contents of class member.

// class Vehicle
// {
// public:
//     string name;
//     int type;
//     int no;
// };

// int main()
// {
//     // Create a pointer to an instance of the "Person" class.
//     Vehicle *v = new Vehicle();

//     v->name = "Splender";
//     v->type = 2;
//     v->no = 9521;

//     cout << "Name of Vehicle     : " << v->name << endl;
//     cout << "2-Wheeler/3-Wheeler : " << v->type << endl;
//     cout << "Vehicle No.         : " << v->no<< endl;

//     // Free the dynamically-allocated object!
//     delete v;
//     return 0;
// }

// 6. Write a program of Parameterized constructor and destructor

// class Add{
//     private:
//         int a;
//         int b;
//     public:
//         Add(int x, int y){
//             a = x;
//             b = y;
//         }
//         void sum(){
//             cout << "x + y = "<<a+b<<endl;
//         }
//         ~Add(){
//             cout << "Object of class Add is destroyed " <<endl;
//         }
// };
// int main(){
//     Add obj(10,20);
//     obj.sum();
// }

// 7.
// class Employee{
//     private:
//         int EmployeeNumber;
//         string EmployeeName;
//         int Salary;
//     public:
//         Employee(){
//             EmployeeNumber = 96108;
//             EmployeeName = "Amit";
//             Salary = 95000;
//         }
//         void display(){
//             cout << "Employee Name  : "<<EmployeeName <<endl;
//             cout << "Employee Number: "<<EmployeeNumber <<endl;
//             cout << "Employee Salary: "<<Salary <<endl;
//         }
// };
// int main()
// {
//     Employee obj;
//     obj.display();
// }

// 8. Write a program to illustrate the concepts of console I/O operations.

// int main()
// {
//     string name;

//     // Output to the console using std::cout
//     cout << "Enter your name: ";
//     // Input from the console using std::cin
//     cin >> name;
//     // To read an entire line of input,
//     // getline(cin, name);
//     // Output the input back to the console
//     cout << "Hello, " << name << "!\n";
//     return 0;
// }

// 9. Write a program to use scope resolution operator. Display the various values of the same variables declared at different scope levels

// int x = 20;
// int main()
// {
//     int x = 10;
//     cout << "X (for local valriable): "<<x<<endl;
//     cout << "X (for global valriable): "<<::x<<endl;
//     return 0;
// }

// 10. Write a program to allocate memory using new operator

// int main()
// {
//     // Allocate an integer on the heap using new
//     int *p = new int;
//     *p = 10;
//     std::cout << "*p: " << *p << '\n';
//     // Deallocate memory for p
//     delete p;
//     return 0;
// }

/* 
This program starts by using the new operator to allocate a single integer on the heap. The new operator returns a pointer to the allocated memory, which is stored in the variable p. The program then stores a value in the allocated memory using the dereference operator (*), and outputs the value using the same operator.

Finally, the program deallocates the memory using the delete operator, which releases the memory back to the system. It is important to use delete to deallocate memory that was allocated with new, to prevent memory leaks.
*/


// 11. Write a program to create multilevel inheritance

/* // Base class
class First
{
public:
    int a;
    First(int x){
        a = x;
    }
};

// Intermediate class
class Second : public First
{
public:
    int b;
    Second(int x, int y) : First(x){
        b = y;
    }
};

// Derived class
class Third : public Second
{
public:
    int c;
    Third(int x, int y, int z) : Second(x, y){
        c = z;
    }
};

int main()
{
    Third obj(1, 2, 3);

    cout << "obj.a: " << obj.a <<endl;
    cout << "obj.b: " << obj.b <<endl;
    cout << "obj.c: " << obj.c <<endl;

    return 0;
}
 */

// 12. Write a program to create an array of pointers. Invoke functions using array objects.

int func(int x){
    cout << "Value of x is: "<<x<<endl;
}
int main()
{
    void (*arr[3])(int) = {func, func, func};
    // assign address of function into array
    // for (int i = 0; i < 5; i++)
    // {
    //     arr[i] = func;
    // }
    // call function using array objects/elements
    // for (int i = 0; i < 5; i++)
    // {
    //     arr[i](i);
    // }
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    
    
}

// 13. Write a Program to create operator overloading in polymorphism

// class Complex{
//     private:
//         int a;
//         int b;
//     public:
//         void SetData(int x, int y) {
//             a = x;
//             b = y;
//         }
//         void Display(){
//             cout << "c3(x,y) = " << a<<","<<b <<endl;
//         }
//         // Complex add(Complex c2)
//         Complex operator +(Complex c2){
//             Complex c;
//             c.a = a + c2.a;
//             c.b = b + c2.b;
//             return(c);
//         }       
// };
// int main(){
//     Complex c1,c2,c3;
//     c1.SetData(1,2);
//     c2.SetData(3,4);
//     // c3 = c1.add(c2); //calling add() through c1 with parameter as c2
//     c3 = c1+c2; //operator overloading
//     c3.Display();
//     return 0;
// }

// 14. Write a program to print multi data value by single data-type (by using template function or class).
