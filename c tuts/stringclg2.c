#include <stdio.h>
#include <strings.h>
#include <stdlib.h>

// palindrome or not withouut using library function

// int main()
// {
//     char A[10], B[10];
//     int i, j, l=0, f=0;
//     printf("Enter string: ");
//     gets(A);

//     while (A[i] != '\0')
//     {
//         l++;
//         i++;
//     }
//     j=l-i;
//     i=0;

//     while (j>=0)
//     {
//         B[i] = A[j];
//         j--;
//         i++;
//     }

//     while (i<l)
//     {
//         if (A[i] != B[i])
//         {
//             f=1;
//             break;
//         }
//         i++;
//     }

//     if (f == 0)
//     {
//         printf("Palindrome");
//     }
//     else{
//         printf("NOT palindrome");
//     }
//     return 0;
// }

void main()
{
    int a =5;
    int *ptr;
    ptr = *a;
    printf("%d %d", *&ptr, &*ptr);    

}