// program to evaluate postfix arithmatic expression
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define exp_size 33
#define stack_size 33
int top = -1;
int stack[stack_size];
void evaluate(char exp[exp_size]);
int push(int num);
int pop();
int display();

int main()
{
    char exp[exp_size];
    printf("Enter the expression in postflix: ");
    for (int i = 0; i < exp_size; i++)
    {
        scanf("%c", &exp[i]);
        if (exp[i] == ')')
        {
            break;
        }
    }
    
    evaluate(exp);
    // display();
    return 0;
}

void evaluate(char exp[])
{
    char ch;
    int a, b, value;
    // traverse all items of stack
    for (int i = 0; exp[i] != ')'; i++)
    {
        ch = exp[i];
        if (isdigit(ch))
        {
            push(ch - '0');
        }
        // if (ch >= 48 && ch <= 57)
        //     {
        //         push(ch - '0');
        //     }
        else
        {
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
            {
                a = pop(); // pop the top value from stack and put it in a
                b = pop(); // pop the next top value fro stack and put it in b
                printf("%d%d",a,b);
                switch (ch)
                {
                case '+':
                    value = b + a;
                    break;
                case '-':
                    value = b - a;
                    break;
                case '*':
                    value = b * a;
                    break;
                case '/':
                    value = b / a;
                    break;
                }
                push(value);
            }
        }
    }
    printf("%d",pop());
    // display();
}

int push(int num)
{
    if (top == (stack_size-1))
        printf("Stack is already is full !!!");
    else
    {
        // top += 1;
        // stack[top] = num; //put the digit on top (here our top will be 0 first time incremented from -1 and so on...)
        // or 
        return(stack[++top] = num); 
    }
}

int pop()
{
    int final;
    if (top == -1)
        printf("Stack is empty, Nothing to pop !!!");
    else
    {   
        final = stack[top];
        top -= 1;
        return(final);
        // or 
        // return(stack[top--]);
    }
    //we have returned the final above already, tf execution is not coming to this printf
    // printf("%d",final); //WE CANNOT DO THIS here, we have to return the final
}
//we have got the end result in final, so there's no need of display func.
int display()
{
    for (int i = top; i >= 0; i--)
    {
        printf("%c", stack[i]);
        // return(stack[i]);
    }
}
