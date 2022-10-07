// A set of numbers that starts with 0 and 1 proceeds in such a way that the next number is the sum of preceeding two nubers. i.e. 0,1,1,2,3,5,8,13......

// Using this program we can find the element in the series at given position.
#include<stdio.h>
#include<conio.h>

int fib_recursive(int n)
{
    if (n == 1 || n == 2)
    {
        return n-1;
    }    
    else
    {
        return fib_recursive(n-1) + fib_recursive(n-2);
    }       
}

int fib_iterative(int n)
{
    int a=0,b=1;
    for (int i = 0; i < n-1; i++)
    {
        b = a+b;
        a = b-a;
    }
    return a;
}

int main()
{
    int terms;
    printf("Enter the index no of the fiboncci series: ");
    scanf("%d", &terms);
    printf("The value of fibonacii number at position %d is %d: \n",terms,fib_recursive(terms));
    printf("The value of fibonacii number at position %d is %d: \n",terms,fib_iterative(terms));


    return 0;
}