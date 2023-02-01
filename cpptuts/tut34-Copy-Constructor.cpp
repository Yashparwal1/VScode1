#include <iostream>
using namespace std;

class Employee{
    int id;
    int salary;
    public:
        Employee(){}
        Employee(int , int);
        Employee(Employee &, Employee &);
        void display(){
            cout << "The salary of Emploiyee ID "<<id<<" is "<<salary<<endl;
        }
};
Employee::Employee(int i, int s){
    id = i;
    salary = s;
}

// When no copy constructor is found, compiler supplies its own copy constructor
Employee::Employee(Employee &i, Employee &s){  //COPY CONSTRUCTOR
    //The constructor which takes reference to its own class as argument is known as copy constructor.
    cout << "Copy Constructor Called...." <<endl;
    id = i.id;
    salary = s.salary;
}
int main()
{
    Employee yash, monu(102,12000.4), sonu(101,10000),sonuC;
    yash.display();
    monu.display();
    sonu.display();
    Employee sonuB(sonu); //COPY CONSTRUCTOR INVOKED
    sonuB.display();
    
    sonuC = sonu; //COPY CONSTRUCTOR NOT INVOKED
        
    Employee sonuD = sonu; //COPY CONSTRUCTOR INVOKED

    
    return 0;
}

class Add
{
    int x, y, z;
    public:
    Add(){}
    Add(int a, int b);
    Add(Add &);
    void calculate(void);
    void display(void);
};
Add::Add(int a, int b)
{
    x = a;
    y = b;
}
Add::Add(Add &p)
{
    x = p.x;
    y = p.y;
    cout<<"Value of x and y for new object: "<<x<<" and "<<y<<endl;
}
void Add ::calculate()
{
z = x + y;
}
void Add ::display()
{
    cout << z;
}
// int main()
// {
//     Add a(5, 6);
//     Add b(a);
//     b.calculate();
//     b.display();
// }
