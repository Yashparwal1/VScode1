#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include<string.h>

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
// int main()
// {
//     // signal(SIGSEGV,segvHandler);
//     char test[10];
//     printf("Enter a string: ");
//     scanf("%s",&test);
//     printf("ok.. string is: %s",test);
// }

// ====================== STRUCTURE IN C===========================
// struct Car
// {
//     char color[20];
//     char engine[20];
//     int seat;
// };

// int main()
// {
//     struct Car maruti;
//     /*
//     maruti.color = "white";

//     because, in the LHS, you're using an array type, which is not assignable.
//     -----assignment operator shall have a modifiable lvalue as its left operand.
//     and, regarding the modifiable lvalue, from chapter §6.3.2.1
//     -----A modifiable lvalue is an lvalue that does not have array type, [...]
//      */
//     // for (int i = 0; i < 20; i++)
//     // {
//     //     maruti.color[i] = "White"; //error
//     // }
//     // maruti.color[] = "white"; //error
//     strcpy(maruti.color, "White"); // works fine
//     printf("%s",maruti.color);
//     return 0;
// }
// ===================================================================================

struct microFields
{
	unsigned int addr:3;
	unsigned int cond:2;
	unsigned int alu:9;
	unsigned int wr:1;
	unsigned int rd:1;
	unsigned int mar:1;
	unsigned int b:5;
	unsigned int a:5;
	unsigned int c:5;
};
union micro
{
	unsigned int microCode;
	struct microFields code;
};

int main(int argc, char* argv[])
{
	union micro test;
    // test.microCode = 101;
    int x;
    x = test.code.alu;
    printf("%d",x);
	return 0;
} 