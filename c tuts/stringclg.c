#include <stdio.h>
#include <strings.h>
#include <stdlib.h>

// identical or not without using strcmp() function.
/* int main()
{

    char A[10], B[10];
    int i = 0, m, n, f = 0;
    printf("enter the string A: ");
    gets(A);
    printf("Enter string B: ");
    gets(B);
    m = strlen(A);
    n = strlen(B);
    if (m > n)
    {
        while (i < m)
        {
            if (A[i] != B[i])
            {
                f = 1;
                break;
            }
            i++;
        }
    }
    else
    {
        while (i < n)
        {
            if (A[i] != B[i])
            {
                f = 1;
                break;
            }
            i++;
        }   
    }
        if (f == 0)
        {
            printf("identical");
        }
        else
        {
            printf("not identical");
        }
return 0;    
} */

// palindrome or not withouut using library function

int main()
{
    char str[10], revstr[10];
    int i, j, l, f=0;
    printf("Enter string: ");
    gets(str);

    for (i = 0; str[i] != '\0'; i++)
    {
        l++;
    }
    // printf("The length of string is: %s",l);
    
for (i = l-1; i >= 0; i--)
    {
        revstr[l-1-i] = str[i];
    } 
    
    for (i = 0; i < l; i++)
    {
        if (revstr[i] != str[i])
        {
            f = 1;
        }
    }
    if (f == 0)
    {
        printf("Palindrome");
    }
    else{
        printf("NOT palindrome");
    }
    return 0;
}