/* * Functions are used to devide a large c program into smaller pieces
* A Function can be called multiple times to provide reusability and modularity to C program.
* Aka procedure or sunroutine

SYNTAX:
return_type function_name(datatype parameter1,datatype parameter2,... )
{
    code to be executed;
}

ADVANTAGES:
1. We can avoid rewriting same logic through functions
2. We can devide work among fellow programmers using functions.
3. We can easily debug a program using function.

DECLARATION , DEFINATION AND CALL:
1. A function is declared to tell a compiler about its existence 
2. A function is defined to get some task done
3, A function is called in order to be used.

TYPES OF FUNCTION:
1. Library function - Functions included in C header files.
2. User-defined function - Functions created by programmer to reduce complexicity of the program.

FUNCTION CODE EXAMPLES:
* Without arguments and without return value
* Without arguments and with return value
* With argument and without return value
* With argument and with return value.
 */

#include<stdio.h>
#include<conio.h>

// with argument and with return value
int sum(int a, float b)
{
    return a+b;
}

// with argument and without return value
void printstar(int n)
{
    int i = 0;
    while (i<n)
    {
    printf("%c",'*');
    i++;
    }
}

// Without any arguments and with return vale
int takenumber(/*no argument here*/)
{   
    int i;
    printf("Enter a number: ");
    scanf("%d",&i);
    return i;
}

// Without argument without return value
void hello()
{
    int i=1;
    while (i<=5)
    {
        printf("Hello\n");
        i++;
    }
} 

int main()
{
    int a,b;
    float c;
    a=10;
    b=5.5;
    c=sum(a,b);
    printf("The sum is %f\n",c);
    // printstar(7);
    // c = takenumber();
    // printf("The entered no. is: %d",c);
    // hello();
    return 0;
}

