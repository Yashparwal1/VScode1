// a no. whose factor's sum is equal to the no. itself

#include<conio.h>
#include<stdio.h>

int main()
{
    int n, i, rem, sum=0;
    printf("Enter a no.: ");
    scanf("%d",&n);
    
    for(i=1; i<n; i++)
    {
        if(n%i==0)
            printf("The factors are %d\n",i);
            sum=sum+1;          
    }
    if(sum==n)
        printf("The no. is a perfect no.");
    else
        printf("The no. is NOT a perfect no.");
    
    return 0;
}