/* 
Variables are nothing but containers to store our data.
Variables can be of various types:
    int, float, double, char, boolean
Based on scope, variables can be of 2 types:
    1. Local variable: are declared inside the braces of any function and can be accessed only from there.
    2. Global Variable: are declared outside any function and can be accessed from anywhere.

NOTE: local and globlal variabeles can have save name.

Datatypes define the type of data a variable can hold.
    eg. an integer variable can store data of integer type
    In C++ datatypes are categorised into 3 groups:
        1. Build-in -- int, char, float, double, boolean
        2. User-defined -- struuct, union, enum 
        3. Derived -- array, functions, pointers

Comments are putted in code to provode some aditional information within the code.
 */

#include<iostream>
using namespace std;
int glo=25; //global function

void temp()
{
    cout<<"global variable is: "<< glo;
}
int main()
{
    int glo=5; 
    //local var has more precedence over global varial in the present function(the function in which we are working)
    glo = 10; //local glo variabe is updated not globale glo variable.
    int a=4, b=5, r=6;
    float pi=3.14;
    float ar;
    // std::cout << "hello world";
    cout << "The value of a is:"<<a<<"\nThe value of b is:"<<b;
    ar = pi*r*r;
    cout<<"\nArea of circle is: "<<ar<<"\n";
    temp();
    cout << "\nlocal variable with same name as gloable variable: "<<glo;
    
    return 0;
}
