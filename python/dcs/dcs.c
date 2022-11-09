#include "stdio.h"
int main()
{
    char i;
    for(i=0x41; i<= 0x5a; i++)
    {   printf("%c",i);}
    printf("\n");
    for(i=0x61; i<= 0x7a; i++)
    {   printf("%c",i);}
}