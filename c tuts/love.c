#include <stdio.h>
#include <conio.h>

int main(int argc, char const *argv[])
{
    int i, j, k, l, m, n, count;
    //I
    for (i = 1; i < 10; i++)
    {
        printf("\x03");
    }
    printf("\n");
    for (j = 1; j < 5; j++)
    {
        printf("    \x03\n");
    }
    for (i = 1; i < 10; i++)
    {
        printf("\x03");
    }
    printf("\n\n");
    //Love
    for (k = 6 / 2; k <= 6; k += 2)
    {
        for (l = 1; l < 6 - k; l += 2)
        {
            printf(" ");
        }

        for (l = 1; l <= k; l++)
        {
            printf("\x03");
        }

        for (l = 1; l <= 6 - k; l++)
        {
            printf(" ");
        }

        for (l = 1; l <= k; l++)
        {
            printf("\x03");
        }

        printf("\n");
    }

    for (k = 6; k >= 1; k--)
    {
        for (l = k; l < 6; l++)
        {
            printf(" ");
        }

        for (l = 1; l <= (k * 2) - 1; l++)
        {
            printf("\x03");
        }

        printf("\n");
    }
    printf("\n");
    //U
    for (m = 1; m <= 5; m++)
    {
        printf("\x03\t\x03\n");
    }
    for (n = 1; n < 10; n++)
    {
        printf("\x03");
    }
    
    // getch();

    return 0;
}
