// a set of no. that starts with a one or zero, followed by a one, and proceeds based on the rule that each no. is equal to the sum of the preceding two numbers. i.e 0,1,1,2,3,5,8......

#include<stdio.h>
#include<conio.h>

// int main()
// {
//     int i, n, t1=0, t2=1, next;
//     printf("No. of terms: ");
//     scanf("%d",&n);

//     for(i=1; i<=n; i++)
//     {
//         printf("%d\t",next);
//         t1=t2;
//         t2=next;
//         next=t1+t2;
//     }
//     return 0;
// }

int main()
{
    int terms,i=0,t1=0,t2=1,next=0;
    printf("Enter the no. of terms: ");
    scanf("%d", &terms);

    while(i<terms)
    {
        if (i <= 1)
        {
            next=i;
            i++;
        }
        else
        {
            next=t1 + t2;
            t1 = t2;
            t2 = next;
            i++;
        }
    printf("%d\t",next);
    }

    return 0;
}

// int fib(int n)
// {
//     int i=1, t1=0, t2=1, next;
//     while (i<n)
//     {
//         printf("%d\t",t1);
//         next = t1 + t2;
//         t1 = t2;
//         t2 = next;
//         i++;
//     }
    
// }
// int main()
// {
//     int terms;
//     printf("Enter the no. of terms: ");
//     scanf("%d",&terms);
//     printf("Fibonacci series upto %d terms is: \n",terms);
//     fib(terms);
//     return 0;
// }