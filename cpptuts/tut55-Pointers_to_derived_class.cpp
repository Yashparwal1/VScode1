#include <iostream>
using namespace std;
class BaseClass
{
    public:
        int var_base;
        void display()
        {
            cout << "Dispalying Base class variable var_base " << var_base << endl;
        }
};

class DerivedClass : public BaseClass
{
    public:
        int var_derived;
        void display()
        {
            cout << "Dispalying Base class variable var_base " << var_base << endl;
            cout << "Dispalying Derived class variable var_derived " << var_derived << endl;
        }
};

int main()
{
    BaseClass *base_class_pointer;
    BaseClass obj_base;
    DerivedClass obj_derived;
    base_class_pointer = &obj_derived; // Pointing base class pointer to derived class

    base_class_pointer->var_base = 34;
    // base_class_pointer->var_derived= 134; // Will throw an error BUT CAN BE SOLVED USING VIRTUAL FUNCTION
    base_class_pointer->display(); //display of baseclass

    base_class_pointer->var_base = 3400;
    base_class_pointer->display(); //diplay of baseclass

    DerivedClass *derived_class_pointer;
    derived_class_pointer = &obj_derived; // Pointing derived class pointer to derived class
    derived_class_pointer->var_base = 9448; //derived pointer can access base-var BUt not vice versa
    derived_class_pointer->var_derived = 98;
    derived_class_pointer->display();

    return 0;
}
