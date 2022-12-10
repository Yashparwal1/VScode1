#include<stdio.h>

int main()
{
    int arr[3][3] = {0,2,3,4,5,6,7,8,9};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    printf("\nprocessing...\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (arr[i][j] == 0)
            {
                while (i<3)
                {
                    arr[i][j] = 0;
                    i++;
                }
                while (j<3)
                {
                    arr[i][j] = 0;
                    j++;
                }
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}