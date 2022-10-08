#include<stdio.h>
#include"add.c"

// extern float pi = 3.14;

int main()
{
    int  j;
    // float r=4, area;
    // area = pi*r*r;
    // printf("Area is %f",area);
    
    // int x = 5, y = 1;
    // printf("Sum is %d",add(x,y));
    
    for (int i = 0; i < 5; i++)
    {
        j = 0;
        while (j<=i)
        {
            printf("*");
            j++;
        }
        printf("\n");
    }
    

    return 0;
}