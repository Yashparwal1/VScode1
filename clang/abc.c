#include <stdio.h>
#include <conio.h>

int main()
{
    for (int n = 1; n <= 10; n++)
    {
        printf("%d\n", n);
    }
    return 0;
}

//= > TO PRINT EVEN NO.FROM 1 TO 100

// int main()
// {
//     int even;

//     if (even % 2 == 0)

//         printf("Even numbers from 1 to 100 are:\n");

//     for (even = 2; even <= 100;)
//     {
//         printf("%d\t", even);
//         even = even + 2;
//     }
    
//     //OR 
    
//     for (even = 1; even <= 100; even++)
//     {
//         if (even % 2 == 0)
//         {
//             printf("%d\t", even);
//         }
//     }

//     return 0;
// }

// // = > TO FIND CUBES

// int main()
// {
//     int i, n;
//     printf("Enter the no upto which you want cubes: ");
//     scanf("%d", &n);
//     for (i = 1; i <= n; i++)
//     {
//         // n=i*i*i;
//         printf("cube of %d is %d\n", i, (i * i * i));
//     }
//     return 0;
// }

// int main()
// {
//     int n, rem, sum = 1, result;
//     printf("enter a no: ");
//     scanf("%d", &n);

//     for (result = n; n != 0; n = n / 10)
//     {
//         rem = n % 10;
//         sum = sum + (rem * rem * rem);
//     }
//     if (sum == result)
//         printf("%d is an armstrong no.", result);
//     else
//         printf("%d is not an armstrong no.", result);

//     return 0;
// }
