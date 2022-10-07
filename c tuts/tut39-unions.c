/* 
* Union is a user-defined datatype (very similar to structures)
* The difference b/w them lies in the fact that in structure, each member has its own storage location whereas members of a Union uses a single shared memory location or union members share same memory location.
STRUCTURE
   ____
|_|    }
|_|    }int a;
|_|    }
|_|____
|_|    }char b;
|_|
|_|
|_|

UNION
   ____
|_|    }      }char b;
|_|    }int a;
|_|    }
|_|____
|_|    
|_|
|_|
|_|

* This single shared memory location is equal to the size of its largest data number.

DECLARING AND ACCESSING UNION MEMBERS:
* Like structures, we access any member by using the member access operator(.) in union.
* We use keyword 'union' to definal a union.
* Syntax is very similar to that of structure.

#NOTE: Union can't handle all members at once. i.e. shared maemory

union test{
    int a;
    float b;
    char c;
}un;

question: memory occupied in union = max(int,flaot,char)
            if structure then memory = (int+float+char)
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*
union abc
{
    int a;
    char b;
}var;
int main()
{
    var.a=65;
    printf("a = %d\n",var.a);
    printf("b = %c\n",var.b);
    printf("b = %d\n",(int)var.b); // here we are type casting b from char to int
}
*/
/* 
OUTPUT: 
a = 65
b = A
As we know union members share same memory location, we print a=65, so 65 is also shared by b and b will take 65 as ascii code and will print the normal value for ascii code 65 that is A.  
 */
// #pragma pack(1)
union student
{
    int id;
    int marks;
    char fav_char;
    char name[50];   
};

int main()
{
    union student s1;
    strcpy(s1.name, "yash");
    s1.id = 2;
    s1.marks = 45;
    s1.fav_char = 'y';  //values will be shared acc. to the var inicialized at last like fav_char here.. 
    
    printf("this is marks %d \n",s1.marks);
    printf("this is id %d \n",s1.id);
    printf("this is fav_char %c \n",s1.fav_char);
    printf("this is name %s \n",s1.name);
    printf("Size of union:%d",sizeof(union student));//for size, keep structure padding concept in mind
    return 0;
}