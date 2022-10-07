// A no. that is equal to the sum of cube of its digits. i.e. 153 (1^3 + 5^3 + 3^3 = 153)

#include<stdio.h>
#include<conio.h>

int main()
{
    int n, rem, sum=0, result;
    printf("enter any no.: ");
    scanf("%d",&n);

    for(result=n; n!=0; n=n/10)
    {
        rem=n%10;
        sum=sum+(rem*rem*rem);
    }
    if(sum==result)
        printf("%d is an Armstrong no.",result);
    else
        printf("%d is NOT an Armtrong no.",result);
    return 0;
}