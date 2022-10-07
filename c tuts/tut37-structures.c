/* What is Structures in C?

* Strectures are user defined data types in C.
* Using Structures allows us to combine different data types together.
* It is used to create complex data types which contains diverse information.
* They are very similar to arrays but structures can store data of any types, which is practically more useful.

eg. suppose we want to store the 10k emaplyee's data (id, name, address, email), then we can either create 40k variables for them or we can create structure.
-------------------------------------------------
SYNTAX:
struct[structure_name]
{
    datatype var1
    datatype var2
    datatype var3 ...
}
[structure_variables];
-------------------------------------------------
EG:
struct student{
    int id;
    char name[70];
    float marks;
}s1, s2, s3
------OR---------
struct student{
    int id;
    char name[70];
    float marks;
};

struct student s1, s2, s3;
-------------------------------------------------
#Declaring and initializing a Structure... (done just like function).
-------------------------------------------------
#Accessing Structure members

* Array variables are accessed using the subscript variables.
* in a similar fashion, structure members are accessed using .(dot) operator.
* '.'is called the "Structure member operator".
* To access the member of the structure, we use this operator in between "Structure name" and "member name"
. 
STRUCTURE PADDING ->
* Processor doesn't read 1 byte at a time from memory, it reads 1 word at a time.
WHAT IS ITS MEAN???????
If we have a 32 bit processor, it means it can access 4 bytes of at a time which mean sword size if 4 bytes. AND...
If we have a 64 bit processor, it means it can access 8 bytes of at a time which mean sword size if 8 bytes.
eg.
struct abc{
    char a;
    char b;
    int c;
}
    ************ IN 32-BIT ARCH.*************   
                |_|_|_|_||_|_|_|_|
                 / / /      / 
                 a b {   c  }

So. total [should be] = 1byte + 1byes + 4bytes = 6bytes  
BUT.............

here, memory is allocated in contigous blocks in memory.
In 1 CPU cycle, chara, charb and 2 bytes of intc can be accessed. There is no problem in chara and charb. BUT....
Whenever we want the value stored in var c, 2 cycles are required to access the contents of variable c. In first cycle 2 bytes can be accessed nd in 2nd cycle other 2 bytes.
*************ITS AN UNNECESSARY WASTAGE OF CPU CYCLES.*****************
We can save the no. cycles by using the concept called padding.

                    empty
                    {   }
                |_|_|_ _||_|_|_|_|
                 / /      /     / 
                 a b      {  c  }
                 
with the help of padding, an empty room is created in 1st cycle and variable c will be allocated in 2nd cycle.
So if we want to access contents of only variable c, now it can be accessed in only 1 cycle. Although memory is getting wasted but memory c is accessed in only CPU cycle.

So. total = 1byte + 1byes + 2bytes + 4bytes = 8bytes

struct abc{
    char a;
    int c;
    char b;
}

                   empty
                  {     }
                |_|_ _ _||_|_|_|_||_|_|_|_|
                 /        /     /  /
                 a        {  c  }  b
So. total[should be] = 1byte + 3byes + 4bytes + 1bytes = 9bytes
BUT.........
total= 1byte + 3byes + 4bytes + 4bytes = 12bytes (because 1 word is accessed not byte)
In 3rd cycle,we only have charb but it will access full cycle of 4 bytes due to the word not just 1 byte


STRUCTURE PACKING:
In padding, a lot of memory is wasted. So to avoid it using STRUCTURE PACKING.
We can do so by just writing #pragma pack(1)
------------------------------------------------------------------------------------------
Pragma is a special purpose directive used to turn on or off certain features.
------------------------------------------------------------------------------------------

struct abc{
    char a;
    int c;
    char b;
}
So in this case the size will be:
1byte + 4bytes + 1byte = 6bytes.
But CPU cycles will get wasted.

SO, IF YOU ARE READY TO WASTE MEMORY, USE PADDING
AND, IF YOU ARE READY TO WASTE CPU CYCLES, USE PACKING

*/

#include <stdio.h>
#include <stdlib.h>
#include<string.h>
// struct student
// {
//     int id;
//     int marks;
//     char fav;
//     char name[100];
// };

// struct student yash, tanmay, aman; // global variables
// int main()
// {
//     // struct student yash, tanmay, aman; // local variables
//     yash.id = 1;
//     tanmay.id = 2;
//     aman.id = 3;
//     yash.marks = 500;
//     tanmay.marks = 501;
//     aman.marks = 502;
//     yash.fav = 'a';
//     tanmay.fav = 'b';
//     aman.fav = 'c';
//     strcpy(yash.name, "Yash Parwal");
//     printf("yash got %d marks\n", yash.marks);
//     printf("Yash's full name is %s", yash.name);
//     return 0;
// }

/* struct padding
{
    char a; //1 byte
    char b; //1 byte
    int c;  //4 bytes
            //total = 6 bytes....... BUT NO...... [see concept in above lines].
    //char a; //1 byte
    //int c;  //4 bytes
    //char b; //1 byte
            //total = 6 bytes....... BUT NO...... [see concept in above lines].
}var;
int main()
{
    printf("%d", sizeof(var));
}
 */

/* struct question
{
    char x,y,z;
};
int main()
{
    struct question p={'1', '0', 'a'+2}; // address: 1000, 1001, 1002..... 'a'+2='c'
    struct question *q=&p;
    //q contains address 1000 which is address of 1st block but q as a pointer will take 1000 as address of the whole structured array variable p.
    printf("%c, %c", *((char*)q+1),*((char*)q+2));
    //here, q was the pointer to the whole stucture. Now it is pointer to a character as we typed cast it to point to the 1st character using (char*)q and +1 and +2 will behave normally.  
}
 */
/* 
struct node
{
    int i;
    float j;
}*s[10];

// Question: Define s to be:
// Answer: An array, whose each element is a pointer to the structure of type node.
 */
