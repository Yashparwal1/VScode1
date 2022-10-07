/*
EXERCISE:

input: <h1> This is a heading </h1>
output: This is a heading
 */

#include<stdio.h>
#include<stdlib.h>

void parser(char *string)
{
    int in = 0;
    int index = 0;
    for (int i = 0; i < strlen(string); i++)
    {
        if (string[i] == '<')
        {
            in = 1;
            continue;
        }
        else if (string[i] == '>')
        {
            in = 0;
            continue;
        }
        if (in == 0)
        {
            
        }
        
        
    }
    
}
int main()
{
    char string[] = "<h1>5This is a heading tag22</h1>27"
    parser(string);
    printf("the parsed string is ~~%s~~ ",string);    
    return 0;
}