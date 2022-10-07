#include<stdio.h>

int main(int argc, char const *argv[])
{
    //int num, i=0;
    // printf("Enter a number: ");
    // scanf("%d",&num);

    // do
    // {
    //     i+=1;
    //     printf("%d\n",i);
    // }
    // while(i<num);
    
    // while (i<30)
    // {
    //     printf("%d\n",i);
    //     i+=1;
    // }

    /* > For loop is used to iterate the statements or a part of the program several times.
       > It is used to traverse the data structures like the Arrays and linked lists.
       > It has a little different syntax from while and do while loops.
    */

    int i,j=0;
    for (i=0; i<5, j<7; ) //Actually all the exp are optionla here, we can initialise var. above; we may not have to give conditions but then it will go in infnite loop, so... and we can use exp3 below also.
    {
        printf("%d %d\n",i,j);
        // j++;
        i++;j++; //we can use exp3 here also coz optional in for()
    }
    // here i<5 but still it is going to 7... becoz the last condition in exp2 will be considered and the rest conditions will be treated as statements
    
    return 0;
}
