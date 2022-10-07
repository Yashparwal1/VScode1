#include <stdio.h>
#include <conio.h>

int main()
{
    int a,b,sum,sub,product,div,mod;
    printf("enter the value of a=");
    scanf("%d",&a);
    printf("enter the value of b=");
    scanf("%d",&b);
    sum=a+b;
    sub=a-b;
    product=a*b;
    div=a/b;
    mod=a%b;
    printf("The sum is=%d\nThe subtraction is=%d\nThe product is=%d\nThe division is=%d\nThe modulus is=%d",sum,sub,product,div,mod);
    
}
