/* 
Is strings a Datatype in C? -- NO
Strings is not a supported datatype in C but it is very useful concept to model the real world entities like name, city etc.
We express strings using an array of characters terminated by a null character ('\0'). 

What are Strings in C ? 
* String is an array of characters terminated by NULL character.
* Inshort, Strings are null terminated arrays.
* String in C is created by creating an array of characters.
* We need extra character ('\0' or null character) to tell the compiler that the string ends here.    
 */

#include <stdio.h>
#include <conio.h>


int printStr(char str[])
{
    int i = 0;   
    while (str[i]!='\0')
    {
        printf("%c",str[i]);
        i++;
    }
    printf("\n");
}
int main()
{
    // char str[] = {'y','a','s','h','\0'};
    // char str[] = "yash";
    char str[25];
    printf("Enter any string: ");
    gets(str);
    // scanf("%s",&str); //scanf will only take first word till space i.e. we can't give sentence as input
    printf("Using a function: ");
    printStr(str);
    printf("üsing print function: ");
    printf("%s",str);
    printf("\nUsing puts function: ");
    puts(str);
    return 0;
}