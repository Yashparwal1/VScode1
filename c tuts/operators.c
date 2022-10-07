#include<stdio.h>

int main(int argc, char const *argv[])
{
    int a,b;
    a=3;
    b=2;

    // printf("a + b=%d\n", a+b);
    // printf("a - b=%d\n", a-b);
    // printf("a * b=%d\n", a*b);
    // printf("a / b=%d\n", a/b);
    
    // printf("a + b=%d\n", a==b); //a+b=0 becoz a is not equal to b
    
   // BITWISE AND (&)
    // 0 - 00       0 & 0 = 0
    // 1 - 01       0 & 1 = 0
    // 2 - 10       1 & 1 = 1
    // 3 - 11  

    printf("a || b = %d\n",a&b);

    return 0;
}
