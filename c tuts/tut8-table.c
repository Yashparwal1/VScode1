#include<stdio.h>

int main(int argc, char const *argv[])
{
    int t,i;
    printf("Enter a no: ");
    scanf("%d",&t);

    printf("Table of given no. is:\n");
    for(i=1; i<=10; i++)
    {
        printf("%d * %d = %d\n",t,i,t*i);
    }
    return 0;
}
