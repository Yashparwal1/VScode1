#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>

/* int main()
{
    int i=400*400/400;
    if (i==400)
    {
        printf("good");
    }
    else
        printf("bad");

    return 0;
} */

// int main()
// {
// int a=3, b;
// b = a++ + ++a + ++a;
// printf("%d %d",a,b);

// int x, y=5;
// x = ++y + y++ - y++;
// printf("%d %d",x,y);

// int a=3,b;
// b = a++ + a++;
// printf("%d %d",a,b);

// return 0;
// }

// int main()
// {
//     int i,j;
//     for(i=1; i<=5; i++)
//     {
//         for(j=1; j<=i; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
// return 0;
// }

// int main()
// {
//     int i=2,n,c=0;
//     printf("Enter the no.: ");
//     scanf("%d",&n);

//     while (i<n)
//     {
//         if (n%i==0)
//         {
//             c=c+1;
//         }
//         else
//         {
//             i++;
//         }
//     }
//     if(c==0)
//     printf("The no. is a prime no.");
//     else
//     printf("The no. is NOT a prime no.");
// return 0;
// }


// int main()
// {
//     int i,terms,n1=0,n2=1,next;
//     printf("Enter the no. of terms: ");
//     scanf("%d",&terms);
//     printf("Fibonacii series upto %d terms is: \n",terms);
//     // for (i = 0; i < terms; i++)
//     // {
//     //     printf("%d\t",n1);
//     //     next = n1 + n2;
//     //     n1 = n2;
//     //     n2 = next;
//     // }

//     for (i = 0; i <= terms; i++)
//     {
//         if (i <= 1)
//         {
//             next = i;
//         }
//         else
//         {
//             next = n1 + n2;
//             n1 = n2;
//             n2 = next;
//         }
//         printf("%d\t",next);   
//     }
//     return 0;
    
// }

// ****logic told by Bijendra Sir***** 
// void main()
// {
//     for (int i = 0; i < 5; i++)
//     {
//         for (int j = 0; j < 5; j++)
//         {
//             // if (i<j)
//             if (i+j<5)
//             { 
//                 printf(" ");
//             }
//             // if (i>=j)
//             if (i+j>=5)
//             {
//                 // printf("%d%d ",i,j);
//                 printf("* ");
//             }
//         }
//         printf("\n");
//     }
    
// }