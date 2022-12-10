#include <stdio.h>
#include <stdlib.h>

// ====================================== INSRTION =============================================

// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void Traversing(struct Node *ptr)
// {
//     while (ptr != NULL)
//     {
//         printf("Element: %d\n", ptr->data);
//         ptr = ptr->next;
//     }
//     // while (ptr->next != NULL)
//     // {
//     //     printf("%d->",ptr->data);
//     //     ptr = ptr->next;
//     // }
//     // printf("%d\n",ptr->data);

// }

// // Case 1 -- Insert at beginning
// struct Node* insertAtFirst(struct Node* head, int data)
// {
//     struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
//     ptr->data = data;
//     ptr->next = head;
//     head = ptr;
//     return head;
// }

// // Case 2 Insert at end
// struct Node * insertAtEnd(struct Node *head, int data){
//     struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
//     ptr->data = data;
//     struct Node * p = head;

//     while(p->next!=NULL){
//         p = p->next;
//     }
//     p->next = ptr;
//     ptr->next = NULL;
//     return head;
// }

// // Case 3 Insert in between/at any position/index
// struct Node * insertAtIndex(struct Node *head, int data, int index){
//     struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
//     struct Node * p = head;
//     int i = 0;

//     while (i!=index-1)
//     {
//         p = p->next;
//         i++;
//     }
//     ptr->data = data;
//     ptr->next = p->next;
//     p->next = ptr;
//     return head;
// }

// int main()
// {
//     struct Node *head;
//     struct Node *second;
//     struct Node *third;
//     struct Node *fourth;

//     // Allocate memory for nodes in the linked list in Heap
//     head = (struct Node *)malloc(sizeof(struct Node));
//     second = (struct Node *)malloc(sizeof(struct Node));
//     third = (struct Node *)malloc(sizeof(struct Node));
//     fourth = (struct Node *)malloc(sizeof(struct Node));

//     head->data = 7;
//     head->next = second; // Link first and second nodes
//     second->data = 11;
//     second->next = third; // Link second and third nodes
//     third->data = 41;
//     third->next = fourth; // Link third and fourth nodes
//     fourth->data = 66;
//     fourth->next = NULL; // Terminate the list at the third node

//     printf("Linked list before insertion\n");
//     Traversing(head);

//     head = insertAtFirst(head, 1);
//     printf("Linked list after insertion at beginning\n");
//     Traversing(head);

//     head = insertAtEnd(head, 100);
//     printf("Linked list after insertion at end\n");
//     Traversing(head);

//     head = insertAtIndex(head, 50, 3);
//     printf("Linked list after insertion in between/at any position/index\n");
//     Traversing(head);
//     return 0;
// }

// ====================================== DELETION =============================================
// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void linkedListTraversal(struct Node *ptr)
// {
//     while (ptr != NULL)
//     {
//         printf("Element: %d\n", ptr->data);
//         ptr = ptr->next;
//     }
// }

// // Case 1: Deleting the first element from the linked list
// struct Node * deleteFirst(struct Node * head){
//     struct Node * ptr = head;
//     head = head->next;
//     free(ptr);
//     return head;
// }

// // Case 2: Deleting the element at a given index from the linked list
// struct Node * deleteAtIndex(struct Node * head, int index){
//     struct Node *p = head;
//     struct Node *q = head->next;
// int i = 0;
// while (i != index-1)
// {
//     p = p->next;
//     q = q->next;
//     i++;
// }
//     p->next = q->next;
//     free(q);
//     return head;
// }

// // Case 3: Deleting the last element
// struct Node * deleteAtLast(struct Node * head){
//     struct Node *p = head;
//     // struct Node *q = head->next;
//     // while(q->next !=NULL)
//     // {
//     //     p = p->next;
//     //     q = q->next;
//     // }
//     // p->next = NULL;
//     // free(q);
//     while (p->next->next != NULL)
//     {
//         p = p->next;
//     }
//     struct Node *q = p->next;
//     p->next = NULL;
//     free(q);

//     return head;
// }

// // Case 4: Deleting the element with a given value from the linked list
// // struct Node * deleteAtIndex(struct Node * head, int value){
// //     struct Node *p = head;
// //     struct Node *q = head->next;
// //     while(q->data!=value && q->next!= NULL)
// //     {
// //         p = p->next;
// //         q = q->next;
// //     }

// //     if(q->data == value){
// //         p->next = q->next;
// //         free(q);
// //     }
// //     return head;
// // }
// int main()
// {
//     struct Node *head;
//     struct Node *second;
//     struct Node *third;
//     struct Node *fourth;

//     // Allocate memory for nodes in the linked list in Heap
//     head = (struct Node *)malloc(sizeof(struct Node));
//     second = (struct Node *)malloc(sizeof(struct Node));
//     third = (struct Node *)malloc(sizeof(struct Node));
//     fourth = (struct Node *)malloc(sizeof(struct Node));

//     // Link first and second nodes
//     head->data = 4;
//     head->next = second;

//     // Link second and third nodes
//     second->data = 3;
//     second->next = third;

//     // Link third and fourth nodes
//     third->data = 8;
//     third->next = fourth;

//     // Terminate the list at the third node
//     fourth->data = 1;
//     fourth->next = NULL;

//     printf("Linked list before deletion \n");
//     linkedListTraversal(head);

//     head = deleteFirst(head); // For deleting first element of the linked list
//     printf("Linked list after deleting first node \n");
//     linkedListTraversal(head);

//     head = deleteAtLast(head);
//     printf("Linked list after deleting the last node \n");
//     linkedListTraversal(head);

//     head = deleteAtIndex(head, 1);
//     printf("Linked list after deleting node at any index/in between \n");
//     linkedListTraversal(head);

//     return 0;
// }

// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CIRCULAR LINKED LIST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

// ==================================== INSERTION =========================================
// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void traversing(struct Node *head){
//     struct Node *ptr = head;
//     do{
//         printf("Element is %d\n", ptr->data);
//         ptr = ptr->next;
//     }while(ptr != head);
// }
// // Case 1
// struct Node * insertAtFirst(struct Node *head, int data){
//     struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
//     ptr->data = data;
//     struct Node * p = head->next;
//     while(p->next != head){
//         p = p->next;
//     }
//     p->next = ptr;
//     ptr->next = head;
//     head = ptr;
//     // mine
//     // head = ptr;
//     // ptr->next = head;
//     return head;
// }

// // Case 2
// struct Node* insertAtLast(struct Node* head, int data)
// {
//     struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
//     ptr->data = data;
//     struct Node *p = head;
//     while (p->next != head)
//     {
//         p = p->next;
//     }
//     p->next = ptr;
//     ptr->next = head;
//     return head;
// }

// // Case 3
// struct Node* insertAtIndex(struct Node* head, int data, int index)
// {
//     struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
//     struct Node *p = head;
//     int i = 0;
//     while (i != index-1)
//     {
//         p = p->next;
//         i++;
//     }
//     ptr->data = data;
//     ptr->next = p->next;
//     p->next = ptr;
//     return head;
// }

// int main(){
//     struct Node *head;
//     struct Node *second;
//     struct Node *third;
//     struct Node *fourth;

//     head = (struct Node *)malloc(sizeof(struct Node));
//     second = (struct Node *)malloc(sizeof(struct Node));
//     third = (struct Node *)malloc(sizeof(struct Node));
//     fourth = (struct Node *)malloc(sizeof(struct Node));

//     head->data = 4;
//     head->next = second;
//     second->data = 3;
//     second->next = third;
//     third->data = 6;
//     third->next = fourth;
//     fourth->data = 2;
//     fourth->next = head;

//     printf("Circular Linked list before insertion\n");
//     traversing(head);

//     head = insertAtFirst(head, 1);
//     printf("Circular Linked list after insertion at beginning\n");
//     traversing(head);

//     head = insertAtLast(head, 100);
//     printf("Circular Linked list after insertion at end\n");
//     traversing(head);

//     head = insertAtIndex(head, 50, 3);
//     printf("Circular Linked list after insertion at any index/in between\n");
//     traversing(head);

//     return 0;
// }

// ======================================= DELETION ==============================================
// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void traversing(struct Node *head){
//     struct Node *ptr = head;
//     do{
//         printf("Element is %d\n", ptr->data);
//         ptr = ptr->next;
//     }while(ptr != head);
// }

// // Case 1
// struct Node * deleteAtFirst(struct Node *head){
//     struct Node * ptr = head;
//     struct Node * p = head->next;
//     while(p->next != head){
//         p = p->next;
//     }
//     head = head->next;
//     p->next = head;
//     free(ptr);
//     return head;
// }

// // Case 2
// struct Node * deleteAtLast(struct Node *head){
//     struct Node * p = head;
//     struct Node * q = head->next;
//     while(q->next != head){
//         p = p->next;
//         q = q->next;
//     }
//     p->next = head;
//     free(q);
//     return head;
// }

// // Case 3
// struct Node * deleteAtIndex(struct Node *head, int index){
//     struct Node * p = head;
//     struct Node * q = head->next;
//     int i = 0;
//     while(i != index-1){
//         p = p->next;
//         q = q->next;
//         i++;
//     }
//     p->next = q->next;
//     free(q);
//     return head;
// }

// int main(){

//     struct Node *head;
//     struct Node *second;
//     struct Node *third;
//     struct Node *fourth;

//     head = (struct Node *)malloc(sizeof(struct Node));
//     second = (struct Node *)malloc(sizeof(struct Node));
//     third = (struct Node *)malloc(sizeof(struct Node));
//     fourth = (struct Node *)malloc(sizeof(struct Node));

//     head->data = 4;
//     head->next = second;
//     second->data = 3;
//     second->next = third;
//     third->data = 6;
//     third->next = fourth;
//     fourth->data = 2;
//     fourth->next = head;

//     printf("Circular Linked list before deletion \n");
//     traversing(head);

//     head = deleteAtFirst(head);
//     printf("Circular Linked list after deletion at beginning\n");
//     traversing(head);

//     head = deleteAtLast(head);
//     printf("Circular Linked list after deleting last node\n");
//     traversing(head);

//     head = deleteAtIndex(head, 3);
//     printf("Circular Linked list after deleting node at any index/in between\n");
//     traversing(head);

//     return 0;
// }

// ===================================================================================================
// ==================================== DOUBLY LINKED LIST ===========================================

struct Node
{
        int data;
        struct Node *next;
        struct Node *prev;
};

void traverse(struct Node *head)
{
        struct Node *p = head;
        printf("Printing List in Right order...\n");
        do
        {       
                printf("%d ",p->data);
                p = p->next;
        }while (p->next != NULL);
        printf("%d ",p->data);
        printf("\nPrinting List in Reverse order...\n");
        do
        {       
                printf("%d ",p->data);
                p = p->prev;
        }while (p != NULL);
}

int main()
{
        struct Node *head;
        struct Node *second;
        struct Node *third;
        struct Node *fourth;
        struct Node *fifth;

        head = (struct Node *)malloc(sizeof(struct Node));
        second = (struct Node *)malloc(sizeof(struct Node));
        third = (struct Node *)malloc(sizeof(struct Node));
        fourth = (struct Node *)malloc(sizeof(struct Node));
        fifth = (struct Node *)malloc(sizeof(struct Node));

        head->prev = NULL;
        head->data = 4;
        head->next = second;
        second->prev = head;
        second->data = 3;
        second->next = third;
        third->prev = second;
        third->data = 6;
        third->next = fourth;
        fourth->prev = third;
        fourth->data = 2;
        fourth->next = fifth;
        fifth->prev = fourth;
        fifth->data = 7;
        fifth->next = NULL;

        printf("Simple Traversing Linked list\n");
        traverse(head);
        // printf("Reverse Traversing Linked list\n");
        // rev_traverse(head);
        return 0;
}