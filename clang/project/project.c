#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>

struct books
{
    int sno;
    int bookid;
    char bookname[33];
    char authername[33];
    int edition;
    char date[33];
}bk;
struct student
{
    int sRoll;
    char sName[33];
    char sClass[33];
    char issuedate[33];
    char bookname[33];
}st;
FILE *fp;

int addbook();
int delbook();
int seebooklist();
int issuebook();
int seeissuedbooklist();
int main()
{
    int choice;
    system("cls");
    while (1)
    {
        printf("\n\n************* LIBRARY MANAGEMET SYSTEM ***************\n\n");
        printf("(press 1) - To Add New Book\n");
        printf("(press 2) - To Delete Books");
        printf("(press 3) - To See Books List\n");
        printf("(press 4) - To Issue Books\n");
        printf("(press 5) - To See Issued Books list\n");
        printf("(press 0) - To Close the program\n");
        printf("**********************************************************\n");
        printf("Enter Your Choice: ");
        scanf("%d",&choice);

        switch (choice)
        {
        case '1':
            addbook();
            break;
        
        case '2':
            delbook();
            break;
        
        case '3':
            seebooklist();
            break;
        
        case '4':
            issuebook();
            break;
        
        case '5':
            seeissuedbooklist();
            break;
        
        case '0':
            exit(0);
            break;
        
        case '1':
            addbook();
            break;
        
        default:
            printf("*********Please choose correct option********");
        }
    }
    printf("Closing the program.......");
    getch();
    return 0;
}

int addbook()
{
    // char date[33];
    // time_t t = time(NULL);
    // struct tm tm = *localtime(&t);
    // sprintf(date, "%02d/%02d/%d",  tm.tm_day, tm.tm_month+1, tm.tm_year+1900);
    // strcpy(bk.date,date);
    
    fp = fopen("books.txt", "a");
    printf("Enter Book ID: ");
    scanf("%d",&bk.bookid);
    printf("Enter Book Name: ");
    scanf("%s",&bk.bookname);
    printf("Enter Auther Name: ");
    scanf("%s",&bk.authername);
    printf("Enter Book Edition: ");
    scanf("%s",&bk.edition);

    fprintf(fp, "Book")
}   