// program to evaluate postfix arithmatic expression
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// ========================================================================================
// #define exp_size 33
// #define stack_size 33
// int top = -1;
// int stack[stack_size];
// void evaluate(char exp[exp_size]);
// int push(int num);
// int pop();
// int display();

// int main()
// {
//     char exp[exp_size];
//     printf("Enter the expression in postflix: ");
//     for (int i = 0; i < exp_size; i++)
//     {
//         scanf("%c", &exp[i]);
//         if (exp[i] == ')')
//         {
//             break;
//         }
//     }
    
//     evaluate(exp);
//     // display();
//     return 0;
// }

// void evaluate(char exp[])
// {
//     char ch;
//     int a, b, value;
//     // traverse all items of stack
//     for (int i = 0; exp[i] != ')'; i++)
//     {
//         ch = exp[i];
//         if (isdigit(ch))
//         {
//             push(ch - '0');
//         }
//         // if (ch >= 48 && ch <= 57)
//         //     {
//         //         push(ch - '0');
//         //     }
//         else
//         {
//             if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
//             {
//                 a = pop(); // pop the top value from stack and put it in a
//                 b = pop(); // pop the next top value fro stack and put it in b
//                 printf("%d%d",a,b);
//                 switch (ch)
//                 {
//                 case '+':
//                     value = b + a;
//                     break;
//                 case '-':
//                     value = b - a;
//                     break;
//                 case '*':
//                     value = b * a;
//                     break;
//                 case '/':
//                     value = b / a;
//                     break;
//                 }
//                 push(value);
//             }
//         }
//     }
//     printf("%d",pop());
//     // display();
// }

// int push(int num)
// {
//     if (top == (stack_size-1))
//         printf("Stack is already is full !!!");
//     else
//     {
//         // top += 1;
//         // stack[top] = num; //put the digit on top (here our top will be 0 first time incremented from -1 and so on...)
//         // or 
//         return(stack[++top] = num); 
//     }
// }

// int pop()
// {
//     int final;
//     if (top == -1)
//         printf("Stack is empty, Nothing to pop !!!");
//     else
//     {   
//         final = stack[top];
//         top -= 1;
//         return(final);
//         // or 
//         // return(stack[top--]);
//     }
//     //we have returned the final above already, tf execution is not coming to this printf
//     // printf("%d",final); //WE CANNOT DO THIS here, we have to return the final
// }
// //we have got the end result in final, so there's no need of display func.
// int display()
// {
//     for (int i = top; i >= 0; i--)
//     {
//         printf("%c", stack[i]);
//         // return(stack[i]);
//     }
// }

// ============================ IMPLEMENTATION OF QUEUE ======================================

// #define size 33
// // #define limit 6
// int queue[size];
// int front = -1;
// int rear = -1;
// int insert();
// int delete();
// int display();
// int main()
// {
//     int choice;
//     printf("Enter the elements in Quesue: ");
//     for (int i = 0; i < 6; i++)
//     {
//         scanf("%d",&queue[i]);
//         front = 0;
//         rear++;
//     }
//     while (1)
//     {            
//         printf("[ 1 ] For Inserting the element: ");
//         printf("[ 2 ] For Deleting the element: ");
//         printf("[ 3 ] For Displaying the elements: ");
//         printf("[ 0 ] To Exit: ");
    
//         scanf("%d",&choice);

//         switch (choice)
//         {
//         case 1:
//             insert();
//             break;
//         case 2:
//             delete();
//             break;
//         case 3:
//             display();
//             break;
//         case 0:
//             exit(0);
//         default:
//             printf("Please choose correct option...");
//             break;
//         }
//     }
//     return 0;
// }

//     int insert()
//     {
//         int m;
//         if (front==0 && rear==(size-1) || rear==(size-1))
//         {
//             printf("Queue Overflow !!");
//         }
//         else
//         {
//             if (front==-1 && rear==-1) //or simply (front == -1)
//             {
//                 printf("Enter the element to insert: ");
//                 scanf("%d",&m);
//                 front = 0;
//                 rear = 0;
//                 queue[rear] = m;
//             }
//             else
//             {
//                 printf("Enter the element to insert: ");
//                 scanf("%d",&m);
//                 rear++;
//                 queue[rear] = m;
//             }
//         }
//         return 0;
//     }    

//     int delete()
//     {
//         int m;
//         if (front==-1 && rear==-1)
//         {
//             printf("Quesue Underflow !!!");
//         }
//         else
//         {
//             printf("Deleted element is %d",queue[front]);
//             front++;
//         }
//         return 0;
//     }

//     int display()
//     {
//         for (int i = front; i <= rear; i++)
//         {
//             printf("%d",queue[i]);
//         }
//         return 0;
//     }

// ============================ IMPLEMENTATION OF CIRCULAR QUEUE ==============================

// #define size 7
// // #define limit 6
// int queue[size];
// int front = -1;
// int rear = -1;
// int insert();
// int delete();
// int display();
// int main()
// {
//     int choice;
//     printf("Enter the elements in Quesue: ");
//     for (int i = 0; i < 6; i++)
//     {
//         scanf("%d",&queue[i]);
//         front = 0;
//         rear++;
//     }
//     while (1)
//     {            
//         printf("[ 1 ] For Inserting the element: ");
//         printf("[ 2 ] For Deleting the element: ");
//         printf("[ 3 ] For Displaying the elements: ");
//         printf("[ 0 ] To Exit: ");
    
//         scanf("%d",&choice);

//         switch (choice)
//         {
//         case 1:
//             insert();
//             break;
//         case 2:
//             delete();
//             break;
//         case 3:
//             display();
//             break;
//         case 0:
//             exit(0);
//         default:
//             printf("Please choose correct option...");
//             break;
//         }
//     }
//     return 0;
// }

//     int insert()
//     {
//         int m;
//         if (front==0 && rear==(size-1))
//         {
//             printf("Queue Overflow !!");
//         }
//         else
//         {
//             if (front==-1 && rear==-1)
//             {
//                 printf("Enter the element to insert: ");
//                 scanf("%d",&m);
//                 front = 0;
//                 rear = 0;
//                 queue[rear] = m;
//             }
//             else if (rear==(size-1) && front != 0)
//             {
//                 printf("Enter the element to insert: ");
//                 scanf("%d",&m);
//                 rear = 0;
//                 queue[rear] = m;
//             }
//             else
//             {
//                 printf("Enter the element to insert: ");
//                 scanf("%d",&m);
//                 rear++;
//                 queue[rear] = m;
//             }
//         }
//         return 0;
//     }    

//     int delete()
//     {
//         int m;
//         if (front==-1 && rear==-1)
//         {
//             printf("Quesue Underflow !!!");
//         }
//         else if (front == (size-1))
//         {
//             printf("Deleted element is %d",queue[front]);
//             front = 0;
//             rear = 0;    
//         }
//         else
//         {
//             printf("Deleted element is %d",queue[front]);
//             front++;
//         }
//         return 0;
//     }
//     int display()
//     {
//         // if (front <= rear)
//         // {
//         //     for (int i = front; i<=rear; i++)
//         //     {
//         //         printf("%d",queue[i]);
//         //     }
//         // }
//         int i=front;
//         while (i<=rear)
//         {
//             printf("%d",queue[i]);
//             i++;
//         }
//         if (front > rear)
//         {
//             for (int i = front; i >= rear; i--)
//             {
//                 printf("%d",queue[i]);
//             }
//         }
//         return 0;
//     }

// ============================ Linked List ========================================

struct node 
{
    int data;
    struct node *next;
};
void append(int);
struct node *p=NULL;
void display();
void main()
{
    append(10);
    append(20);
    append(30);
    append(40);
    display();
}
void append(int n)
{
    struct node *temp;
    // printf("first time value of p: %p\n",p); //(just to test the address of p)
    if (p == NULL){
        temp = (struct node*)malloc(sizeof(struct node));
        temp->data = n;
        temp->next = NULL;
        p = temp;
        // printf("temp in if: %p\n",temp); //(just to test the address )
        // printf("p in if: %p\n",p); //(just to test the address)
    }
    else
    {
        struct node *temp2;
        // printf("in else part: %p\n",p); //(just to test the address)
        temp = p;
        // printf("in while loop: %p\n",temp->next); 
        //temp->next is already NULL here (in case of 2nd node only), this while loop will not execute
        // here while loop is upgrading the node; if not used then the next node will always connect to 1st node and only 1st and last node will be printed and inbetween nodes will get overwritten by the next followinf nodes each time.  
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp2 = (struct node*)malloc(sizeof(struct node));
        temp2->data = n;
        temp2->next = NULL;
        temp->next = temp2;
    }
}

void display()
{
    struct node *temp;
    temp = p;
    // printf("in display: %p\n",temp); //(just to test the address)
    while (temp != NULL)
    {
        printf("%d\n",temp->data);
        temp = temp->next;
    }
}