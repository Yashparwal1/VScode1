#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// program to evaluate postfix arithmatic expression

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
//                 // printf("a and b are: %d and %d espectively\n",a,b);
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
//         // printf("a + b: %d\n",pop());  
//         }
//     }
//     printf("Result of given expression is: %d",pop());
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
//we have got the end result in final, so there's no need of display func.
// int display()
// {
//     for (int i = top; i >= 0; i--)
//     {
//         printf("\n%c", stack[i]);
//         // return(stack[i]);
//     }
//     return 0;
// }

// ========================================================================================

// program to sort array in assending order 
// int main()
// {
//     int arr[] = {6,7,1,3,4,0,9,10};
//     printf("\nArray before sorting:\n");
//     int size = sizeof(arr)/sizeof(arr[0]);
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     for (int i = 0; i < size; i++)
//     {
//         for (int j = i+1; j < size; j++)
//         {
//             if (arr[i]>arr[j])
//             {
//                 int temp;
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//             }
            
//         }
        
//     }
//     printf("\nArray after sorting:\n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     return 0;
    
// }

// ========================================================================================
// prohram ot traversing the elements of an array

// int main()
// {
//     int arr[] = {6,7,1,3,4,0,9,10};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     printf("Array is: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     printf("\nTraversing each elements of an array....\n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("element traversed -- %d\n",arr[i]);
//     }
    
// }
// ========================================================================================
// program to find whetehr a matrix is sparce matirix or not.

// int main()
// {
//     int arr[3][3] = {1,2,3,0,0,0,0,0,9}, count = 0;
//     printf("Matrix is: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d",arr[i][j]);
//         }
//         printf("\n");
//     }
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
            
//             if (arr[i][j] == 0)
//                 count++;
//             else
//                 continue;
//         }
//     }
//     if (count >= (9/2)+1) //OR (m*n/2)+1
//         printf("The matrix is a Sparse matrix");
//     else
//         printf("The matrix is NOT a Sparse matrix");
//     return 0;
// }
// ========================================================================================
// program to .......................

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

// struct Node 
// {
//     int data;
//     struct Node *next;
// };
// void Create_node(int);
// struct Node *head=NULL;
// struct Node InsertEnd(struct Node*, int);
// void display();

// void main()
// {
//     Create_node(10);
//     Create_node(20);
//     Create_node(30);
//     Create_node(40);
//     // InsertEnd(100);
//     display();
// }
// void Create_node(int n)
// {
//     struct Node *temp;
//     // printf("first time value of p: %p\n",p); //(just to test the address of p)
//     if (head == NULL){
//         temp = (struct Node*)malloc(sizeof(struct Node));
//         temp->data = n;
//         temp->next = NULL;
//         head = temp;
//         // printf("temp in if: %p\n",temp); //(just to test the address )
//         // printf("p in if: %p\n",p); //(just to test the address)
//     }
//     else
//     {
//         struct Node *temp2;
//         // printf("in else part: %p\n",p); //(just to test the address)
//         temp = head;
//         // printf("in while loop: %p\n",temp->next); 
//         //temp->next is already NULL here (in case of 2nd node only), this while loop will not execute
//         // here while loop is upgrading the node; if not used then the next node will always connect to 1st node and only 1st and last node will be printed and inbetween nodes will get overwritten by the next followinf nodes each time.  
//         while (temp->next != NULL)
//         {
//             temp = temp->next;
//         }
//         temp2 = (struct Node*)malloc(sizeof(struct Node));
//         temp2->data = n;
//         temp2->next = NULL;
//         temp->next = temp2;
//     }
//     return temp2;
// }

// void display()
// {
//     struct Node *temp;
//     temp = head;
//     // printf("in display: %p\n",temp); //(just to test the address)
//     while (temp->next != NULL)
//     {
//         // if (temp->next != NULL)
//         // {
//         //     printf("%d->",temp->data);
//         // }
//         printf("%d->",temp->data);
//         temp = temp->next;
//     }
//     printf("%d ",temp->data);

// }


// --------------------------------INSERTION AT BEGINING----------------------------------

// struct Node* InsertBeg(struct Node* head, int data)
// {
//     struct Node* new;
//     new = (struct Node*)malloc(sizeof(struct Node));
//     new->data = data;
//     new->next = head;
//     head = new;
//     return head;
// };

// --------------------------------INSERTION AT END----------------------------------

// struct Node* InsertEnd(struct Node* head, int data)
// {
//     struct Node* new;
//     struct Node* temp;
//     new = (struct Node*)malloc(sizeof(struct Node));
//     new->data = data;
//     new->next = NULL;
//     temp = head;
//     while (temp->next != NULL)
//     {
//         temp = temp->next;
//     }
//     temp->next = new;
//     return temp;
// };
// ==========================INSERT AT MID===============================================

// struct Node* InsertMid(strut Node* head, int data, int index)
// {
//     struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
//     new->data = data;
//     struct Node* temp = head;
//     int i = 0;
//     while (i != index-1)
//     {
//         temp = temp->next;
//         i++;
//     }
// }

// ============================== DELETION AT BEG================================
// struct Node* DeleteBeg(struct Node* head)
// {
//     struct Node* temp = head;
//     head = head->next;
//     free (temp);
//     return head;
// }
// ============================== DELETION AT END ================================
// struct Node* DeleteEnd(struct Node* head)
// {
//     struct Node* temp = head;
//     struct Node* temp2 = head->next;
//     while (temp2->next != NULL)
//     {
//         temp = temp->next;
//         temp2 = temp2->next;
//     }
//     temp->next = NULL;
//     free (temp2);
//     return head;
// }



/* 
// ----- from here ----------

struct Node 
{
    int data;
    struct Node *next;
};
struct Node Create_node(int);
struct Node *head=NULL;
void InsertEnd( int);
void display();

void main()
{
    Create_node(10);
    InsertEnd(20);
    InsertEnd(30);
    InsertEnd(40);
    // InsertEnd(100);
    display();
}
struct Node* Create_node(int n)
{
    struct Node *temp;
    temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = n;
    temp->next = NULL;
    if (head == NULL){
        
        head = temp;
        return head;
    }
    else
    {
    //    struct Node *temp2;
      //  temp2 =
        // printf("in else part: %p\n",p); //(just to test the address)
        //temp = head;
        // printf("in while loop: %p\n",temp->next); 
        //temp->next is already NULL here (in case of 2nd node only), this while loop will not execute
        // here while loop is upgrading the node; if not used then the next node will always connect to 1st node and only 1st and last node will be printed and inbetween nodes will get overwritten by the next followinf nodes each time.  
    //     while (temp->next != NULL)
    //     {
    //         temp = temp->next;
    //     }
    //     temp2 = (struct Node*)malloc(sizeof(struct Node));
    //     temp2->data = n;
    //     temp2->next = NULL;
    //     temp->next = temp2;
    // }
    return temp;
}

void display()
{
    struct Node *temp;
    temp = head;
    // printf("in display: %p\n",temp); //(just to test the address)
    while (temp->next != NULL)
    {
        // if (temp->next != NULL)
        // {
        //     printf("%d->",temp->data);
        // }
        printf("%d->",temp->data);
        temp = temp->next;
    }
    printf("%d ",temp->data);

}

struct node* InsertEnd(int data)
{
   struct Node* temp2 = Create_node(data);
   struct node* temp;
    
//     new = (struct Node*)malloc(sizeof(struct Node));
    // new->data = data; 
    // new->next = NULL;
    temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = temp2;
    return temp;
}

// ----- till here --------------
. */

// ==================================== FILE WORK ======================================

// 1. program to traversing or printing value of array

