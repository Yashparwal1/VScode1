#include<iostream>
using namespace std;

class Base1{
    public:
        void greet(){
            cout << "Good Morning" <<endl;
        }  
};
class Base2{
    public:
        void greet(){
            cout << "Good Night" <<endl;
        }  
};
class Derived : public Base1, public Base2{
    int a;
    public:
        void greet(){
            Base1::greet(); //ambiguity resolution using scope resolution operator
            Base2::greet();
        }
};

class B{
    public:
        void say(){
            cout << "Hello CPP" <<endl;
        }
};
class D:public B{
    public:
        void say(){ //if derived class has its onw say() then this will execute otherwise base class's say() will be executed. So this is how ambiguity is resolved in this example.  
            cout << "Hello C" <<endl;
        }
        // WHAT'S HAPPNING HERE?? --> D's say() will override B's say()
};
int main()
{
    Derived obj;
    obj.greet();
    
    D d;
    d.say();
    return 0;
}