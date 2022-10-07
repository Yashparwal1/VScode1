/*
WHY AND HOW TO PASS ARRAYS ?
* We pass arrays to function when we need to pass a list of values to a given function
* We can pass the arrays to a given function:
    1. By declaring arrray as a parameter in the function.
        int avg(int arr[])

    2. By declaring the pointer in a function to hold the base address of the array.
        int sum(int *ptr)

 */

#include <stdio.h>
#include <conio.h>

int func1(int A[])
{
    for (int i = 0; i < 4; i++)
    {
        printf("the value at %d is %d\n",i,A[i]);
    }
    return 0;
}

int main()
{
    int arr[] = {23,33,43,53};
    func1(arr);
    return 0;
}