#include<stdio.h>
#include<conio.h>

int main()
{
    int choice,ai,ds,n;
    printf("[1.] - AI \n[2.] - Data Science \n[3.] - Networking \n\n");
    start:
    printf("In which field you want to do job: ");
    scanf("%d",&choice);

    switch (choice)
    {
    case 1:
        printf("YOU CHOOSE Artificial Intelegence Field !\n");
        printf("These are some posts as which you can do jobs: \n");
        x:
        printf("[1.] - AI Engineer \n[2.] - Data Analytics \n[3.] - Research Scientist \nChoose an option: ");
        scanf("%d",&ai);

        switch (ai)
        {
        case 1:
            printf("Programming languages to learn for AI Engineer:\n\n");
            printf("Python\nJava\nR\nProlog\nLisp\n");
            break;
        case 2:
            printf("Programming language to learn for Data analytics:\n\n");
            printf("Python\nJavaScript\nR\nC/C++\nSQL\nMatlab\nScala\nJulia\nSAS\n");
            break;
        case 3:
            printf("Programming langyages to learn for Research Scientist\n\n");
            printf("Python\nALGOL\nR\nJ\nMAPLE\nMatlab\nFortran\nJulia\nAPL\n");
            break;

        default:
            printf("***Please choose from 1 to 3...\n");
            goto x;
            break;
        }
        break;
    
    case 2:
        printf("YOU CHOOSE Data Science Field !\n");
        printf("These are some posts as which you can do jobs: \n");
        y:
        printf("[1.] - Data Scientist \n[2.] - ML Engineer \n[3.] - Application Architect \nChoose an option: ");
        scanf("%d",&ds);

        switch (ds)
        {
        case 1:
            printf("Programming languages to learn for Data Scientist:\n\n");
            printf("Python\nJava\nProlog\nLisp\nJavascript\nSQL\nMatlab\nScala\nJulia\nSAS\n");
            break;
        case 2:
            printf("Programming language to learn for ML Engineer:\n\n");
            printf("Python\nJavaScript\nR\nC/C++\nSQL\nMatlab\nScala\nJulia\nSAS\n");
            break;
        case 3:
            printf("Programming langyages to learn for Application Architect\n\n");
            printf("C/C++/C#\nPython\nJava\nALGOL\nMAPLE\nMatlab\nFortran\nJulia\nAPL\n");
            break;

        default:
            printf("***Please choose from 1 to 3...\n");
            goto y;
            break;
        }
        break;
    
    case 3:
        printf("YOU CHOOSE Networking Field !\n");
        printf("These are some posts as which you can do jobs: \n");
        z:
        printf("[1.] - Network Administrator \n[2.] - Database Administrator \n[3.] - Telecommunication Specialists \nChoose an option: ");
        scanf("%d",&ds);

        switch (n)
        {
        case 1:
            printf("Programming languages to learn for Network Administrator:\n\n");
            printf("Python\nPerl\nBASH\nTCL\nGO\nJavascript\n");
            break;
        case 2:
            printf("Programming language to learn for Database Administrator:\n\n");
            printf("Python\nSQL\nR\nPHP\nC#\n");
            break;
        case 3:
            printf("Programming langyages to learn for Telecommunication Specialist\n\n");
            printf("C#\nPython\nJava\nErlang\nGO\n");
            break;

        default:
            printf("***Please choose from 1 to 3...\n");
            goto z;
            break;
        }
        break;
    default: 
        printf("***Please select from 1 to 3...\n");
        goto start;
        break;
    }
    return 0;

}