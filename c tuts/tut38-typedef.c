// typedef is used to give alternative names to existing datatypes
// syntax: typedef <previous_name> <alias_name>

??=include<stdio.h>
#include<stdlib.h>

int main()
??<
    typedef unsigned long ul;
    typedef int i;
    ul a, b, c;    
    i yash = 25;
    printf("%d",yash);
    return 0;
??>