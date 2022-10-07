/* 
What is a pointer ?
* Variable which stores the address of another variable.
* Can be of type int, char, array, function, or any other pointer.
* Size depends on the architecture. Ex. 2 bytes for bits.
* They can be declared using asterisk symbol (*).

'&' and '*' operators ?
* The address of operator & returs the address of a variable
* (*) is the dereference operator (aka indirection operator) used to get the value at a given address.
   
   dereference - Obtainig the data item held at another location from pointer

#NULL POINTER
* A pointer that is not assigned any value but null is known as NULL pointer.
* A NULL pointer does not point to any object or function.
* We can use it to initialise a pounter variable when the pointer variable isn't assigned any valid memory address yet.
* int *ptr = NULL;

USES OF POINTER
* Dynamic memory allocation
* Arrays , functions and structures 
* Return multiple values from a function
* Pointer reduces the code and improves the performance
*/

#include <stdio.h>
#include <conio.h>

/* int main()
{
    int a = 25;
    int *ptra = &a; // ptra will store the address of 'a'

    // printf("The address of a is %p\n", &a); //for getting address of a in the memory 
    // printf("The address of pointer to a is %p\n", ptra); //for address of ptra in the memory 

    printf("The address of pointer to a is %p\n", &ptra); //for address of ptra variable
    printf("The address of a is %p\n", *ptra); //for address of pointed variable
    
    // printf("The value of a is %d\n",a); //for value stored at that address
    // printf("The value of a is %d\n", *ptra); //dereferencing ptra i.e. obtaining the value stored at address of 'a'

    // int *ptr2; //it will return garbage vale
    int *ptr2 = NULL; //it will give null value i.e. 00000000
    printf("The address of ptr2 pointer is %p\n", ptr2);  

    return 0;
} */

/* 
int main()
{
    int a, *b;
    a = 5;
    // b = a;
    b = &a;
    // printf("%d",*b);
    printf("%d, %d",b,*b);
} 
*/

/* 
int main()
{
    int x=5,y,*z;
    y = ++x;
    z = &y;
    printf("%d, %d, %d",&z,z,*z);

    // 1- address of z
    // 2- address of y
    // 3- value at address of y, i.e. 6
}
 */

// int main()
// {
//     int x=5, y, *z;
//     y = ++x + x++;
//     printf("%d",y); printf("%d",x);
//     // z = &y;
//     // printf("%d, %d, %d",&z,*(&z),*z);
// }


// FIND FACTORIAL USING POINTER
// METHOD 1: 

// int main()
// {
//     int n, f=1;
//     int *num, *fact;
//     num = &n;
//     fact = &f;

//     printf("Enter the number whose factoial you want to find: ");
//     scanf("%d",&n);
//     printf("\nFactorial of %d is =\n",n);
//     for (int i = n; i >= 1; i--)
//     {
//         *fact = *fact * i;
//         printf("%5d",i);
//     }

//     printf(" = %d",*fact);

//     return 0;
// }

// METHOD 2: 
// int factorial(int n, int *fact)
// {
//     *fact = 1;
//     for (int i = n; i >= 1 ; i--)
//     {
//         *fact = *fact * i;
//     }
// }

// int main()
// {
//     int n, fact;
//     printf("Enter the number whose factorial you want to find: ");
//     scanf("%d",&n);

//     factorial(n,&fact);
//     printf("The factorial of %d is %d",n,fact);
//     return 0;
// }