/* # What is recursive function?
Recursive function or Recursion is a process when a function calls a copy of itself to work on a smaller problem.

* Any function which calls itself is called recursive function.

A termination condition is imposed on such functions to stop them executing copies of themselves forever.

* Any problem that can be solved recursively can also be solved iteratively.

NOTES:
* the case at which the function doesn't recur is called the base case.
* The instance where the function keeps calling itself to perform a subtask, is called the recursive case.
* For factorial calculation the base case occurs at the parameter value of 0 and 1.
 
 */

#include<stdio.h>
#include<conio.h>

//FACTORIAL using recursion

// 5! = 5 * 4! (factorial = num * fact(num-1))
// int fact(int num)
// {
//     if (num == 0 || num == 1)
//     {
//         return 1;
//     }
//     else
//     {
//         return (num * fact(num-1)); // here we called fact() again within the fact() 
//     }
    
// }

// FIBONACCI series: 0,1,1,2,3,5,8,13... 
int fibonacci(int n)
{
    int n1=0, n2=1,next;
    if (n==0 && n==1)
    {
        return n;
    }
    else
    {
        return fibonacci();
    }
    
}

int main()
{
    // int n,f;
    // printf("Enter the no.: ");
    // scanf("%d",&n);
    // f = fact(n);
    // printf("Factorial of %d is %d",n,f);
    // // // printf("Factorial of %d is %d",n,fact(n));

    int num;
    printf("Enter the no of terms: ");
    scanf("%d",&num);
    printf("%d, %d, ",0,1);
    fibonacci(num);
    // printf("%d, ",f); we dont need to print here as we already did in function
    return 0;

}