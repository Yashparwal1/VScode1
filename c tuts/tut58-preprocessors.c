/* 
* Compiler converts textual form of a C program into an executable
* There are four phases for a C program to become an executable.
    PreProcessing > Compilation > Assembly > Linking

PreProcessing --> 
    >Removal of Comments
    >Expansion of macros
    >Expansion of include files.
Compilation -->
    >Assembly level instructions are generated which are understood by assembler.
Assembly -->
    >.0, .exe files are generated.
    >but functions like printf are not resolved yet 
    >Assembly level instructions are converted into machine code
Linking -->
    >links the function implementations i.e links all object files

# WHAT IS C PREPROCESSOR ?
* C preprocessor comes under action before the actual compilation process.
* C preprocessor is not a part of the C compiler.
* It is a text substitution tool.
* All preprocessor commands begins with a hash (#) symbol.

PREPORCESSOR COMMAND EXAMPLES:
    > #define
    > #unded
    > #include3
    > #if
    > #indef
    > #inndef
    > #elif
    > #else
    > #endif
    > ## -- it wotks as an operator. It is used with the #sefine macro. It is used for concatination of what before ## with what after ## is.

    #define usage(a,b) a##b+a*b
    main(){printf("%d, usage(2,5)")}

    OUTPUT:
        a##b+a*b ==== 2##5+2*5 === 25+2*5 == 25+10 = 35
 */

#include<stdio.h>
#include<stdlib.h>
// #define print(x) "hello" //1.
// #define yp(x) printf("hello")
#define yp(x) printf(#x)

int main()
{
    // printf("%s",print(x)); //1.
    // yp(x);
    // yp();
    yp(hello);
    return 0;
}