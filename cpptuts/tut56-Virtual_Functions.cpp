#include <iostream>
using namespace std;
/* 
RUN TIME POLYMORPHISM:-
    one name -- difftime forms
    (display) -- in 2 classes
 WHICH DISPLAY TO EXECUTE??
    Desicion at run time by seeing virtual keyword --> means binding is at run time --> function ke address se object ko associate krta h vo run time pe krta h --> konsa display h jo object se bind hua h
*/
class BaseClass
{
    public:
        int var_base = 1;
        // void display(){
        //     cout << "B - Dispalying Base class variable var_base " << var_base << endl;
        // }
        virtual void display() //default behaviour ko override krne ke lie 
        {
            cout << "B - Dispalying Base class variable var_base " << var_base << endl;
        }
};

class DerivedClass : public BaseClass
{
    public:
        int var_derived = 2;
        void display()
        {
            cout << "D - Dispalying Base class variable var_base " << var_base << endl;
            cout << "D - Dispalying Derived class variable var_derived " << var_derived << endl;
        }
};

int main()
{
    BaseClass *base_class_pointer;

    BaseClass obj_base;
    DerivedClass obj_derived;
    
    base_class_pointer = &obj_derived; // Pointing base class pointer to derived class

    // base_class_pointer->display(); //display of baseclass without virtual function
    base_class_pointer->display(); //display of derived class with virtual function

    return 0;
}
