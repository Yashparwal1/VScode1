#include<stdio.h>

/*int main()
{
    int n;
    printf("Enter your age: ");
    scanf("%d",&n);

    printf("You have entered your age: %d\n",n);

    if(n>=18)
    {
        printf("You are eligible to vote");
    }
    else
    {
        printf("You are not eligible to vote");
    }
    return 0;
 
}*/

int main()
{
    int p,sub;

    printf("How many exams have you passed (1 or 2): ");
    scanf("%d",&p);
    
    if(p==2)
    {
        printf("You have passed both exams \n You will get a trimax pen worth Rs.50");
    }
    else if(p==1)
    {
        printf("Which exam have you passed? \n1-Maths \n2-Science\n(1 or 2): ");
        scanf("%d",&sub);
        if(sub==1)
        {
            printf("You have passed Maths exam. \nYou will get a Pen worth Rs.20");
        }
        else
        {
            printf("You have passed Science exam. \nYou will get a Pen worth Rs.20");
        }   
            
    }
    return 0;
}