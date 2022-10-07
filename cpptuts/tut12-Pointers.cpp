/* 
Pointers in C++
A pointer is a variable which holds the address of other variable. The “&” operator is called “address off" operator, and the "*” operator is called “value at” dereference operator. 
 */
#include<iostream>
using namespace std;

int main(){
    // What is a pointer? ----> Variable which holds the address of other variable
    int a=3;
    int* b;
    b = &a;

    // & ---> (Address of) Operator
    cout<<"The address of a is "<<&a<<endl;
    cout<<"The address of a is "<<b<<endl;

    // * ---> (value at) Dereference operator
    cout<<"The value at address of b is "<<*b<<endl;

    // ** ---> Pointer to pointer
    // double pointer var stores the address or another pointer var
    // above b stores the addr of a, here b also have some addr, so c can store IT'S addr, so c will be double pointer  
    
    // int* c = &b; //will give error: cannot convert 'int**' to 'int*' in initialization
    int** c = &b; ///this is correct
    cout<<"The address of b is "<<&b<<endl;
    cout<<"The address of b is "<<c<<endl; 
    cout<<"The value at address of c is "<<*c<<endl; //value at addr c is the addr of b, so it'll print an address
    cout<<"The value at address value_at(value_at(c)) is "<<**c<<endl; //value at addr of addr of c
    // c ke addr pe ek or addr h, us addr pe ky value h

    return 0;
}
