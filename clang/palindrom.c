// A no. which is same after reverse

#include<conio.h>
#include<stdio.h>

int main()
{
    int n, i, dig, j=0;
    printf("Enter any no.: ");
    scanf("%d",&n);

    for(i=n; i>0; i=i/10)
    {
        dig=i%10;
        j=j*10+dig;
    }

    if(j==n)
        printf("The %d is a palindrom no.",n);
    else
        printf("The %d is NOT a palindrom no.",n);
    
    return 0;
}