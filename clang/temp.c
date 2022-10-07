#include<stdio.h>
#include"add.c"

// extern float pi = 3.14;

int main()
{
    // float r=4, area;
    // area = pi*r*r;
    // printf("Area is %f",area);
    
    int x = 5, y = 1;
    printf("Sum is %d",add(x,y));
    
    return 0;
}