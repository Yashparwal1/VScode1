#include <stdio.h>
#include "add.c"
// extern float pi = 3.14;
// int main()
// {
//     int j;
//     // float r=4, area;
//     // area = pi*r*r;
//     // printf("Area is %f",area);
//     // int x = 5, y = 1;
//     // printf("Sum is %d",add(x,y));
//     for (int i = 0; i < 5; i++)
//     {
//         j = 0;
//         while (j <= i)
//         {
//             printf("*");
//             j++;
//         }
//         printf("\n");
//     }
//     return 0;
// }

#include <stdio.h>
int Rprime(int);
int Lprime(int);
int prime(int);
int Lcount = 0;
int Rcount = 0;

int main()
{
    int n = 1899, R;
    printf("Enter the value : ");
    scanf("%d", &n);

    R = prime(n);
    printf("Occurence : %d", R);

    return 0;
}

int prime(int n)
{

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            Lprime(n - 1);
            Rprime(n + 1);
        }
    }
    // printf("%d\n%d\n",Lcount,Rcount);
    printf("Lprime is: %d\nRprime is: %d\n",Lprime(n-1),Rprime(n+1));
    if (Lcount == Rcount && Lcount == 0)
    {
        return 0;
    }
    else if (Lcount == Rcount && Lcount != 0)
    {
        return 2;
    }
    else if (Lcount != Rcount)
    {
        return 1;
    }
}
int Lprime(int x)
{
    Lcount++; // it is 3 for n=10
    // printf("l-%d\n",Lcount);
    for (int i = 2; i < x; i++)
    {
        if (x % i == 0)
        {
            Lprime(x - 1);
        }
    }
    return x;
    // return Lcount;
    // for number 10, n = 7, how to get that 7
}
int Rprime(int y)
{
    Rcount++; //it is 1 for n=10
    // printf("r-%d\n",Rcount);
    for (int i = 2; i < y; i++)
    {
        if (y % i == 0)
        {
            Rprime(y + 1);
        }
    }
    return y;
    // printf("%d",Rcount);
    // for number 10, n = 11, how to get that 11
}