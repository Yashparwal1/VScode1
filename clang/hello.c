#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
// void main()
// {
//     printf("You have been hacked....");
//     system("pause");
// }

void create();
void display();

struct node
{
    int info;
    struct node *next;
};
struct node *start=NULL;

int main()
{
    while (1)
    {
        int ch;
        start:
        printf("1. Create\n");
        printf("2. Display\n");
        printf("3. Exit\n");

        printf("Enter your choice: ");
        scanf("%d",&ch);

        switch (ch)
        {
        case 1:
            create();
            break;
        case 2:
            display();
            break;
        case 3:
            exit(0);
        default:
            printf("Please enter choice between 1 & 3");
            goto start;
        }
    }
    return 0;
}
void create()
{
    struct node *temp, *ptr;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter Value: ");
    scanf("%d", &ptr->info);
    temp->next = NULL;
    if (start = NULL)
    {
        start = temp;
    }
    else
    {
        ptr = start;
        while (ptr->next != NULL)
        {
            ptr = ptr->next;
            ptr->next = temp;
        }
    }
}
void display()
{
    struct node *ptr;
    printf("List of elements: ");
    for (ptr=start; ptr!=NULL; ptr=ptr->next)
    {
        printf("%d", ptr->info);
    }
}