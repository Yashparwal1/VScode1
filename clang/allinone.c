#include<stdio.h>
#include<conio.h>

const float pi=3.14;
void first()
{
    printf("Hello, I am Yash Parwal\n\n");
}
void second(int a, int b)
{
    printf("Enter two numbers: ");
    scanf("%d%d\n\n",&a,&b);
}
float third(float a, float b)
{
    return (a+b);
}
float fourth(float a, float b)
{
    return (a-b);
}
int fifth(int a, int b)
{
    printf("Enter two numbers: ");
    scanf("%d%d",&a,&b);
    printf("%d x %d = %d \n%d / %d = %d \n%d mod %d = %d\n\n",a,b,a*b,a,b,a/b,a,b,a%b);
}
int sixth(int r)
{
    int area,cir;
    printf("Enter the radious: ");
    scanf("%d",&r);
    area = pi*r*r;
    cir = 2*pi*r;
    printf("Area = %d and Circumfrence = %d\n\n",area,cir);
}
int seventh(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
    return(*a,*b);
}
int eighth()
{
    int si,p,r,t;
    si=(p*r*t)/100;
    printf("Simple interest = %d\n\n",si);
}


int main()
{
    int choose,a,b,c;
    float A,B;
    while(1)
    {
        printf("1. To print something \n2. To Accept any two integers \n3. To add two float numbers \n4. To Subtract two float numbers \n5. To Multiply, divide & find modulus of two integer numbers \n 6. To calculate area & Circumference of circle \n7. Two swap 2 values using 3rd variable \n8. To calculate simple interest \n*** PRESS 0 TO QUIT ***\n\n");
        start:
        printf("CHOOSE: ");
        scanf("%d",&choose);
        switch (choose)
        {
        case 0:
            printf("\n *** Quiting the program !!! *** \n");
            goto end;
            break;
        case 1:
            first();
            break;
        case 2:
            second(a,b);
            break;
        case 3:
            printf("Enter two numbers: ");
            scanf("%f%f",&A,&B);
            printf("Sum of %f and %f is %f\n\n",A,B,third(A,B));
            break;
        case 4:
            printf("Enter two numbers: ");
            scanf("%f%f",&A,&B);
            printf("Subtraction of %f from %f is %f\n\n",A,B,fourth(A,B));
            break;
        case 5:
            fifth(a,b);
            break;
        case 6:
            sixth(a);
            break;
        case 7:
            printf("Enter the values of a and b respectively: ");
            scanf("%d%d",&a,&b);
            seventh(&a,&b);
            printf("After swapping a = %d and b = %d\n\n",a,b);
            break;
        case 8:
            printf("Enter principle amount, rate and time: ");
            scanf("%d%d%d",&a,&b,&c);
            // printf("Simple interest = %d",)
            eighth();
            break;

        default:
            printf("** Please select from 1 to 8 ***\n\n");
            goto start;
            break;
        }
    }
    end:
    // getch();
    return 0;
}
