#include <stdio.h>
#include<stdlib.h>
#include <signal.h>

// int main()
// {
//     char i;
//     for(i=0x41; i<= 0x5a; i++)
//     {   printf("%c",i);}
//     printf("\n");
//     for(i=0x61; i<= 0x7a; i++)
//     {   printf("%c",i);}
// }

// int main()
// {
//     char *x = "USER";
//     printf("%s",getenv(x));
//     return 0;
// }

// void segvHandler( int s ) 
// {
//   printf( "Segmentation Fault\n" );
//   exit( EXIT_FAILURE );
// }
int main()
{
    // signal(SIGSEGV,segvHandler);
    char test[10];
    printf("Enter a string: ");
    scanf("%s",&test);
    printf("ok.. string is: %s",test);
}