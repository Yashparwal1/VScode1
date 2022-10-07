#include<stdio.h>
#include<math.h>

int main()
{
    int num; float root;
    printf("Enter the no.: ");
    scanf("%d",&num);
    root=sqrt(num);
    printf("Squre root of %d = %f",num,root);
    return 0;
}