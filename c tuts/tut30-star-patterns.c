#include <stdio.h>
#include <conio.h>

//0 for triangular start pattern and 1 for reversed triangular start pattern
int main()
{
    int choose;
    start:
    printf("[0] - for Triangular start pattern \n[1] - For reversed triangular star pattern \n CHOOSE: ");
    scanf("%d",&choose);
    switch (choose)
    {
    case 0:
        for(int i=0;i<5;i++)
        {
            for (int j=0; j<=i; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        break;
    case 1:
        for(int i=0;i<5;i++)
        {
            for (int j=5; j>i; j--)
            {
                printf("*");
            }
            printf("\n");
        }
        break;
    
    default:
        printf("Please choose between 0 and 1");
        goto start;
        break;
    }
    
    return 0;
}