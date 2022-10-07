/*
* When a function is called, the values (expression) that are passed in the call are called arguments or actual parameters

* Formal parameters are local variables which are assigned values from the arguments when the function is called.

TYPES OF FUNCTION CALLS:
In C, we can call function in 2 ways based on how we specify the arguments.
1. Call by Value
when we copies values of actual parameters in formal parameters (simple)

=> When we call a function by value. it means thet we are passing the values of thr arguments which are copied into formal parameters of the function.
=>Which means that the original values remain unchanged and only the parameters inside the function changes.


2. Call by Reference1
we give address of the actual parameter (&x).
func1(int *a){ *a }
main(){int x=7; func1(&x);}

=> The call by reference method of passing arguments in a C function copies the address of the arguments into the formal parameters.
=> Addresses of the actual arguments are copied and then assigned to the corrosponding formal arguments

*/

#include<stdio.h>

// void swap(int *x, int *y)
// {
//     int temp;
//     temp = *x; //save the value at address x
//     *x = *y; //put y into x
//     *y = temp;
// }

// int changevalue(int *address)
// {
//     *address = 100;
// }

int addition(int *a, int *b)
{
    int temp;
    *a = *a + *b;
    temp = *a - *b;
    *b = temp - *b;
}

int main()
{
    // int a=34, b=74;
    // printf("Before swapping a=%d, b=%d",a,b);
    // swap(&a, &b);
    // printf("After swapping a=%d, b=%d",a,b);
    
    // int a=10, b=20;
    // printf("The value of a is %d\n",a);
    // changevalue(&a);
    // printf("The value of a now is %d",a);

    int a=4, b=3;
    printf("The values of a and b are %d and %d resp.\n",a,b);
    addition(&a,&b);
    printf("NOW the values of a and b are a+b=%d and a-b=%d resp.",a,b);
    return 0;
}