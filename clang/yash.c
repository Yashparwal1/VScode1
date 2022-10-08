#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
/*int main()
{
    float r,area,cir;
    const float pi = 3.14;
    printf("enter the value of radious=");
    scanf("%f",&r);
    area=pi*r*r;
    cir=2*pi*r;
    printf("area of circle is = %f\n",area);
    printf("circumfrence of circle is = %f",cir);
    getch();
}
*/

// int main()
// {
//     char name[] = {'y', 'a', '\0'};
//     printf("Enter your name: ");
//     scanf("%s", name);
//     printf("Your name is %s", name);

//     return 0;
// }

// int main()
// {
//     char name[20];
//     printf("Enter your name:");
//     scanf("%c",name);
//     printf("your name is");
//     return 0;
// }

// 5 -- To Multiply, divide & find modulus of two integer numbers

// int main()
// {
//     int a,b,product,div,mod;
//     printf("enter the values of a and b : ");
//     scanf("%d%d",&a,&b);
//     product=a*b;
//     div=a/b;
//     mod=a%b;
//     printf("the product of a and b is=%d\nthe division of a and b is=%d\nthe modulus of a and b is=%d",product,div,mod);

// }

// 6 -- To calculate area and circumfrence of the circle

// int main()
// {
//     float r,ar,cf;
//     const float pi=3.14;
//     printf("enter the radius= ");
//     scanf("%f",&r);
//     ar=pi*r*r;
//     cf=2*pi*r;
//     printf("Area of circle is=%f\nCircumfrence of circle is=%f",ar,cf);
//     return 0;
// }

// 7 -- To swap two numbers using 3rd variable

// int main()
// {
//     int a,b,c;
//     printf("the the value of a and b = ");
//     scanf("%d%d",&a,&b);
//     c=a;
//     a=b;
//     b=c;
//     printf("now values of a and b is=%d and %d respectively",a,b);

// }

// 8 -- To calculate simple interest

// int main()
// {
//     float p, r, t, SI;
//     printf("enter principle value=");
//     scanf("%f",&p);
//     printf("enter rate value=");
//     scanf("%f",&r);
//     printf("enter time=");
//     scanf("%f",&t);
//     SI=(p*r*t)/100;
//     printf("Simple interest is=%f",SI);
//     return 0;
// }

// 9 -- To convert a given temp. from centigrade to fahrenhiet

// int main()
// {
//     float celsius,fahrenheit;
//     printf("Enter the temperature in celsius");
//     scanf("%f",&celsius);
//     fahrenheit=(celsius* 9/5) + 32;
//     printf("celsius into fahrenheit is = %f",fahrenheit);
//     return 0;
// }

// 10 -- To find the area of right angle triangle

// int main()
// {
//     float b,h,area;
//     printf("Enter value of base = ");
//     scanf("%f",&b);
//     printf("Enter value of height = ");
//     scanf("%f",&h);
//     area=(b*h)/2;
//     printf("The area of a right angle triangle is = %f",area);
//     return 0;
// }

// 11 -- To swap two variables without usig third variable

/*int main()
{
    int a,b; //15,9
    printf("Enter the values of a and b: ");
    scanf("%d%d",&a,&b);
    a = a-b; //15-9=6
    b = a+b; //6+9=15
    a = b-a; //15-6=9

    // OR

    // a = a+b; //15 + 9 = 24
    // b = a-b; //24-9=15
    // a = a-b; //24-15=9

    printf("After swapping:\na=%d and b=%d",a,b);
    return 0;
}*/

// 12 -- To find value and address of a character, integer and float value.

/* int main()
{
    char ch;
    int i;
    float f;
    printf("Enter any character: ");
    scanf("%c",&ch);
    printf("For characters: \nValue = %c \t Address = %p\n",ch,&ch);

    printf("Enter any integer: ");
    scanf("%d",&i);
    printf("For Integers: \nValue = %d \t Address = %p\n",i,&i);

    printf("Enter any Float no.: ");
    scanf("%f",&i);
    printf("For Float no.: \nValue = %f \t Address = %p\n",f,&f);
    return 0;

} */

// 13 -- To display the ASCII vlaue of any character.
//  int main()
//  {
//      char c;
//      printf("enter any character: ");
//      scanf("%c",&c);
//      printf("ASCII value of the character is: %d",c);
//      return 0;
//  }

// 14 -- to find if the no. is positive.
//  int main()
//  {
//      int num;
//      printf("Enter any number: ");
//      scanf("%d",&num);
//      if(num>0)
//      printf("The entered number is POSITIVE");
//      return 0;
//  }

// 15 -- To print the season name corrosponding to given month number

// int main()
// {
//     int m;

//     printf("Enter the month number: ");
//     scanf("%d",&m);

//     // if(m==1 || m==2 || m==10 || m==11 || m==12)
//     //     printf("The season in this month is WINTER SEASON",m);
//     // else if(m==3 || m==4 || m==5 || m==6)
//     //     printf("The season in this month is SUMMER SEASON",m);
//     // else if(m==7 || m==8 || m==9)
//     //     printf("The season in this month is RAINY SEASON",m);
//     // else
//     //     printf("Please enter the correct month number between 1 to 12");

// //     if(m>2 && m<7)
// //     printf("The season is SUMMER SEASON");
// //     else if(m>6 && m<10)
// //     printf("The season is RAINY SEASON");
// //     else if(m>0 && m<3 || m>9 && m<13)
// //     // else if(m>12 && m<1)
// //     printf("The season is WINTER SEASON");
// //     else
// //     printf("Pleaee enter the correct month number between 1 and 12");

//     // switch (m)
//     // {
//     // case 1:
//     // case 2:
//     // case 10:
//     // case 11:
//     // case 12:
//     //     printf("This is WINTER SEASON going on.");
//     //     break;
//     // case 3:
//     // case 4:
//     // case 5:
//     // case 6:
//     //     printf("This is SUMMER SEASON going on.");
//     //     break;
//     // case 7:
//     // case 8:
//     // case 9:
//     //     printf("This is RAINY SEASON going on.");
//     //     break;
//     // default:
//     //     printf("Please enter number between 1 to 12");
//     //     break;
//     // }
//     return 0;
// }

// 16 -- TO check whether a no is even or odd

/*
int main()
{
    int n;
    printf("Enter any number: ");
    scanf("%d",&n);
    if(n%2==0)
        printf("The number is EVEN");
    else
        printf("The number is ODD");
    return 0;
}*/

// 17 -- To display the smallest no. amongst two
/*
int main()
{
    int i,j;
    printf("Enter 1st no. as i: ");
    scanf("%d",&i);
    printf("Enter 2nd no. as j: ");
    scanf("%d",&j);

    if(i<j)
    {
        printf("i i.e. %d is smaller",i);
    }
    else{
        printf("j i.e. %d is smaller",j);
    }
    return 0;

} */

// 18 -- To check whether a person is eligible to vote or not.

// int main()
// {
//     int age;
//     printf("Enter your age: ");
//     scanf("%d",&age);

//     if (age>=18)
//     {
//         printf("You are eligible to give vote");
//     }
//     else
//     {
//         printf("You are not eligible to give vote");
//     }
//     return 0;
// }

// 19 -- To make simple calculator using switch case

/* int main()
{
    int num1,num2;
    char o;
    printf("Enter operator (+,-,*,/):");
    scanf(" %c",&o);
    printf("Enter 1st no.: ");
    scanf("%d",&num1);
    printf("Enter 2nd no.: ");
    scanf("%d",&num2);

    switch (o)
    {
    case '+':
        printf("%d + %d = %d",num1,num2,num1+num2);
        break;
    case '-':
        printf("%d - %d = %d",num1,num2,num1-num2);
        break;
    case '*':
        printf("%d * %d = %d",num1,num2,num1*num2);
        break;
    case '/':
        printf("%d / %d = %d",num1,num2,num1/num2);
        break;
    default:
        printf("Please enter correct operator given above !!!");
        break;
    }
    return 0;
} */

// 20 -- To check whether a given alphabet is in uppercase or not

/*int main()
{
    char c;
    printf("Enter the alphabet: ");
    scanf("%c",&c);

    if(c>='A' && c<='Z') //or if (c>=65 && c<=90)
    // char value of A=65,a=97 and Z=90,z=122 AND 0=48,9=57
        printf("The given alphabet is in Uppercase");
    else if (c>='a' && c<='z') //or if(c>=97 && c<=122)
    {
        printf("The given alphabet is NOT in Uppercase");
    }
    else
        printf("*** Please enter alphabet only ***");

    return 0;
} */

// 21 -- To display the 1st 10 natural numbers.

// int main()
// {
//     int i=1;
//     printf("The first 10 natural numbers are:\n");
//     while (i<=10)
//     {
//         printf("%d\t",i);
//         i++;
//     }
//     return 0;
// }

// 22 -- To display the gretest no. amongst three.

/*int main()
{
    int a,b,c;
    printf("Enter the values of a , b , c : ");
    scanf("%d %d %d",&a,&b,&c);
    printf("You entered:\na=%d\tb=%d\tc=%d\n",a,b,c);

    if(a>b)
    {
        if (a>c)
            printf("a i.e. %d is gretest",a);
        else
            printf("c i.e. %d is greatest",c);
    }
    else
        if (b>c)
            printf("b i.e. %d is greatest",b);
        else
            printf("c i.e. %d is greatest",c);

    return 0;

}
*/

// 23 -- To find whether a no. is positive or negative

// int main()
// {
//     int n;
//     printf("Enter the no.: ");
//     scanf("%d",&n);

//     if(n>0)
//     printf("The no. %d is Positive",n);
//     else
//     printf("The no %d is Negative",n);
//     return 0;
// }

// 24 -- To check whether a given character is alphabet or digit or special symbol.

// int main()
// {
//     char ch;
//     printf("Enter the character: ");
//     scanf("%c",&ch);
//     // char value of A=65,a=97 and Z=90,z=122 AND 0=48,9=57

//     if ((ch>=97 && ch<=122) || (ch>=65 && ch<=90))
//     {
//         printf("The given character is Alphabet");
//     }
//     else if (ch>=48 && ch<=57)
//     {
//         printf("The given character is digit");
//     }
//     else
//         printf("The given character is a special symbol");

//     return 0;
// }

// 25 -- To check whether a triangle is isoceles or equilateral or scalene

// int main()
// {
//     /*
//     Equilateral triangle: All three sides are equal.
//     Isosceles triangle: Any two sides are equal.
//     Scalene triangle: No sides are equal.
//     */
//     int s1, s2, s3;
//     printf("Enter the 3 sides (s1, s2, s3): ");
//     scanf("%d%d%d",&s1,&s2,&s3);

//     if (s1==s2 && s2==s3)
//     {
//         printf("The triangle is Equileteral Triangle");
//     }
//     else if (s1==s2 || s2==s3 || s3==s1)
//     {
//         printf("The triangle is Isosceles Triangle");
//     }
//     else
//         printf("The triangle is Scalene triangle");

//     return 0;
// }

// 26 -- To calculate the grade of student acc. to the specified marks.

// int main()
// {
//     float marks;
//     printf("Enter your percent marks out of 100: ");
//     scanf("%f",&marks);

//     if (marks>=90 && marks<=100)
//     {
//         printf("Your grade is A");
//     }
//     else if (marks>=80 && marks<90)
//     {
//         printf("Your grade is B");
//     }
//     else if (marks>=70 && marks<80)
//     {
//         printf("Your grade is C");
//     }
//     else if (marks>=60 && marks<70)
//     {
//         printf("Your grade is D");
//     }
//     else if (marks>=0 && marks<50)
//     {
//         printf("Your grade is E");
//     }
//     else
//         printf("Run the program again and please enter marks between 0 to 100");
//     return 0;
// }

// 27 -- To check whether a given character is consonant, vowel or special symbol.
/*
int main()
{
    char ch;
    printf("Enter the character: ");
    scanf("%c",&ch);

    if ((ch>='a' && ch<='z') || (ch>='A' && ch<='Z'))
    {
        if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U')
            {
                printf("The character is Vowel");
            }
        else
            printf("The character is Consonant");
    }
    else
        printf("The character is Special Symbol");

    return 0;
} */

// 28 -- To subtract two numbers in such a manner that it will always give the positive result.

// int main()
// {
//     int a,b,sub;
//     printf("Enter no. a and b: ");
//     scanf("%d%d",&a,&b);

//     sub = a-b;

//     if (sub<0)
//     {
//         sub=sub*(-1);
//         printf("|%d - %d| = %d",a,b,sub);
//     }
//     else
//         printf("%d - %d = %d",a,b,sub);

//     return 0;
// }

// 29 -- To Enter the digits of decimal no. system and display their corrosponding names.

/* int main()
{
    int num, r=0;
    printf("Enter the number: ");
    scanf("%d",&num);

    while (num!=0)
    {
        r=(r*10)+(num%10);
        num=num/10;
    }
        // printf("Reversed no. = %d\n\n",r);

    while (r!=0)
    {
        switch (r%10)
        {
        case 0:
            printf("Zero ");
            break;
        case 1:
            printf("One ");
            break;
        case 2:
            printf("Two ");
            break;
        case 3:
            printf("Three ");
            break;
        case 4:
            printf("Four ");
            break;
        case 5:
            printf("Five ");
            break;
        case 6:
            printf("Six ");
            break;
        case 7:
            printf("Seven ");
            break;
        case 8:
            printf("Eight ");
            break;
        case 9:
            printf("Nine ");
            break;
        }
    r = r/10;
    }
    return 0;

} */

// 30 -- To check whether an alphabet is consonant or vowel .

/* int main()
{
    char al;
    printf("Enter any letter: ");
    scanf("%c", &al);

    if (al == 'a' || al == 'e' || al == 'i' || al == 'o' || al == 'u' || al == 'A' || al == 'E' || al == 'I' || al == 'O' || al == 'U')
    {
        printf("The character is Vowel");
    }
    else
        printf("The character is Consonant");

    return 0;
} */

// 31 -- To check whether a given year is leap or not
/* exactlay divisible by 4
   excluding century years (1800, 1900 etc)
   => centuary years to be leap year -- perfectly divisible by 400
*/

// int main()
// {
//     int year;
//     printf("Enter the year: ");
//     scanf("%d", &year);

//     // //using if-else...
//     //     if ((year%4==0 && year%100!=0) || (year%400==0))
//     //     {
//     //         printf("The year %d is a leap year",year);
//     //     }
//     //     else
//     //     {
//     //         printf("The year %d is NOT a leap year",year);
//     //     }

//     // // using if-else-if...
//     // if (year % 400 == 0)
//     // {
//     //     printf("The year %d is a leap year", year);
//     // }
//     // else if (year % 100 == 0)
//     // {
//     //     printf("The year %d is NOT a leap year", year);
//     // }
//     // else if (year % 4 == 0)
//     // {
//     //     printf("The year %d is a leap year", year);
//     // }
//     // else
//     // {
//     //     printf("The year %d is NOT a leap year", year);
//     // }

//     // //using nested if
//     // if (year%4==0)
//     // {
//     //     if (year%100==0)
//     //     {
//     //         if (year%400==0)
//     //         {
//     //             printf("The year %d is a leap year",year);
//     //         }
//     //         else
//     //         {
//     //             printf("The year %d is NOT a leap year",year);
//     //         }
//     //     }
//     //     else
//     //     {
//     //         //divisible by 4 but not 100, then no need to check for 400, direct come to this else 
//     //         printf("The year %d is a leap year",year);
//     //     }
//     // }
//     // else
//     // {
//     //     printf("The year %d is NOT a leap year",year);
//     // }

//     return 0;
// }

// 32 -- To display a month name corresponding to given month no.

/* int main()
{
    int m;
    printf("Enter the month no. ");
    scanf("%d",&m);

    switch (m)
    {
    case 1:
        printf("This is January going on.");
        break;
    case 2:
        printf("This is february going on.");
        break;
    case 3:
        printf("This is March going on.");
        break;
    case 4:
        printf("This is April going on.");
        break;
    case 5:
        printf("This is May going on.");
        break;
    case 6:
        printf("This is June going on.");
        break;
    case 7:
        printf("This is July going on.");
        break;
    case 8:
        printf("This is August going on.");
        break;
    case 9:
        printf("This is September going on.");
        break;
    case 10:
        printf("This is October going on.");
        break;
    case 11:
        printf("This is November going on.");
        break;
    case 12:
        printf("This is December going on.");
        break;

    default:
        printf("Please enter number between 1 to 12");
        break;
    }

    return 0;
}
 */

// 33 -- To display first 10 whole no. in reverse order

// int main()
// {
//     int i=9;
//     printf("First 10 whole no. in reverse order are: \n");

//     // for (i=9; i>=0; i--)
//     // {
//     //     printf("%d\t",i);
//     // }

//     // while (i>=0)
//     // {
//     //    printf("%d\t",i);
//     //    i=i-1;
//     // }

//     // do
//     // {
//     //     printf("%d\t",i);
//     //     i--;
//     // } while (i>=0);

//     return 0;
// }

// 34 -- To print HELLO five times

// int main()
// {
//     int i=1;
//     while (i<=5)
//     {
//         printf("HELLO\n");
//         i++;
//     }
// }

// 35 -- To print first 10 odd number

// int main()
// {
//     // int n=0,i=1;
//     // printf("First 10 odd numbers are:\n");
//     // while (i<=19)
//     // {
//     //     n++;
//     //     printf("%d. %d\n",n,i);
//     //     i=i+2;
//     // }
// //or
//     // int n=0,i=0;
//     // printf("First 10 odd numbers are:\n");
//     // while (i<20)
//     // {
//     //     i++;
//     //     if (i%2==0)
//     //     {
//     //         continue;
//     //     }
//     //     else
//     //     {
//     //         n++;
//     //         printf("%d. %d\n",n,i);
//     //     }

//     // }

//     return 0;
// }

// 36 -- To demonstrate that do while loop executes atleast once

// int main()
// {
//     int i=10;
//     do
//     {
//         i++;
//         printf("Hello World");
//     } while (i<5);

//     printf("\nhere the condition is false but still printf() executed once which is in loop");

//     return 0;
// }

// 37 -- To code a menu driven program

// int main()
// {
//     int choice,ai,ds,n;
//     printf("[1.] - AI \n[2.] - Data Science \n[3.] - Networking \n\n");
//     start:
//     printf("In which field you want to do job: ");
//     scanf("%d",&choice);

//     switch (choice)
//     {
//     case 1:
//         printf("YOU CHOOSE Artificial Intelegence Field !\n");
//         printf("These are some jobs as which you can do jobs: \n");
//         x:
//         printf("[1.] - AI Engineer \n[2.] - Data Analytics \n[3.] - Research Scientist \nChoose an option: ");
//         scanf("%d",&ai);

//         switch (ai)
//         {
//         case 1:
//             printf("Programming languages to learn for AI Engineer:\n");
//             printf("Python\nJava\nR\nProlog\nLisp\n");
//             break;
//         case 2:
//             printf("Programming language to learn for Data analytics:\n");
//             printf("Python\nJavaScript\nR\nC/C++\nSQL\nMatlab\nScala\nJulia\nSAS\n");
//             break;
//         case 3:
//             printf("Programming langyages to learn for Research Scientist\n");
//             printf("Python\nALGOL\nR\nJ\nMAPLE\nMatlab\nFortran\nJulia\nAPL\n");
//             break;

//         default:
//             printf("***Please choose from 1 to 3...\n");
//             goto x;
//             break;
//         }
//         break;

//     case 2:
//         printf("YOU CHOOSE Data Science Field !\n");
//         printf("These are some jobs as which you can do jobs: \n");
//         y:
//         printf("[1.] - Data Scientist \n[2.] - ML Engineer \n[3.] - Application Architect \nChoose an option: ");
//         scanf("%d",&ds);

//         switch (ds)
//         {
//         case 1:
//             printf("Programming languages to learn for Data Scientist:\n");
//             printf("Python\nJava\nProlog\nLisp\nJavascript\nSQL\nMatlab\nScala\nJulia\nSAS\n");
//             break;
//         case 2:
//             printf("Programming language to learn for ML Engineer:\n");
//             printf("Python\nJavaScript\nR\nC/C++\nSQL\nMatlab\nScala\nJulia\nSAS\n");
//             break;
//         case 3:
//             printf("Programming langyages to learn for Application Architect\n");
//             printf("C/C++/C#\nPython\nJava\nALGOL\nMAPLE\nMatlab\nFortran\nJulia\nAPL\n");
//             break;

//         default:
//             printf("***Please choose from 1 to 3...\n");
//             goto y;
//             break;
//         }
//         break;

//     case 3:
//         printf("YOU CHOOSE Networking Field !\n");
//         printf("These are some jobs as which you can do jobs: \n");
//         z:
//         printf("[1.] - Network Administrator \n[2.] - Database Administrator \n[3.] - Telecommunication Specialists \nChoose an option: ");
//         scanf("%d",&ds);

//         switch (n)
//         {
//         case 1:
//             printf("Programming languages to learn for Network Administrator:\n");
//             printf("Python\nPerl\nBASH\nTCL\nGO\nJavascript\n");
//             break;
//         case 2:
//             printf("Programming language to learn for Database Administrator:\n");
//             printf("Python\nSQL\nR\nPHP\nC#\n");
//             break;
//         case 3:
//             printf("Programming langyages to learn for Telecommunication Specialist\n");
//             printf("C#\nPython\nJava\nErlang\nGO\n");
//             break;

//         default:
//             printf("***Please choose from 1 to 3...\n");
//             goto z;
//             break;
//         }
//         break;
//     default:
//         printf("***Please select from 1 to 3...\n");
//         goto start;
//         break;
//     }
//     return 0;

// }

// OR

/*
This program asks used to convers numbers from one unit to another
1.kms to miles
2.inches to foot
3.cms to inches
4.pounds to kgs
5.inches to meters
 */

/*
float kmstomiles(float kms)
{
    return (kms * 0.621371);
}
float inchestofoot(float inches)
{
    return (inches * 0.0833333);
}
float cmstoinches(float cms)
{
    return (cms * 0.393701);
}
float poundstokgs(float pounds)
{
    return (pounds * 0.453592);
}
float inchestometers(float inches)
{
    return (inches * 0.0254);
}

int main()
{
    int conv;
    float unit, result;
    char anyKey;

    choose:

    while (2)
    {
        start:
        printf("Select the conversion: \n[1.] kms to miles \n[2.] Inches to foot \n[3.] cms to inches \n[4.] pounds to kgs \n[5]. inches to meters \n\n[0]. To quit the program \n ");
        scanf("%d", &conv);
        switch (conv)
        {
        case 0:
            printf("Quiting the program...");
            goto end;
            break;
        case 1:
            printf("You have chosen KMS to MILES\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f kms = %f miles\n", unit, kmstomiles(unit));
            printf("------------------------------------------------------------------\n");
            // printf("Press any key to continue....\n");
            // scanf(" %c", &anyKey);
            // goto start;
            break;
        case 2:
            printf("You have chosen INCHES to FOOT\n");
            printf("Enter the number in inches: ");
            scanf("%f", &unit);
            printf("%f inches = %f foot\n", unit, inchestofoot(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 3:
            printf("You have chosen CMS to INCHES\n");
            printf("Enter the number in CMS: ");
            scanf("%f", &unit);
            printf("%f cms = %f inches\n", unit, cmstoinches(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 4:
            printf("You have chosen POUNDS to KGS\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f pounds = %f kgs\n", unit, poundstokgs(unit));
            printf("------------------------------------------------------------------\n");
            break;
        case 5:
            printf("You have chosen INCHES to METERS\n");
            printf("Enter the number in kms: ");
            scanf("%f", &unit);
            printf("%f inches = %f meters\n", unit, inchestometers(unit));
            printf("------------------------------------------------------------------\n");
            break;
        default:
            printf("*** Plese choose from 1 to 5 ***\n");
            goto choose;
            break;
        }
    }
    end:
    getch();
    return 0;
}
 */

// 38 -- To display alphabet in reverse order

// int main()
// {
//     char i='Z';
//     printf("Alphabets in reverse order are:\n");
//     while (i>='A' && i<='Z')
//     {
//         printf("%c\t",i);
//         i--;
//     }
//     return 0;
// }

// 39 -- To display table of a number

// int main()
// {
//     int i=1,n;
//     printf("Enter the number: ");
//     scanf("%d",&n);

//     for (i=1; i<=10; i++)
//     {
//         printf("%d x %d = %d\n",n,i,n*i);
//     }

//     // while (i<=10)
//     // {
//     //     printf("%d x %d = %d\n",n,i,n*i);
//     //     i++;
//     // }

//     // do
//     // {
//     //     printf("%d x %d = %d\n",n,i,n*i);
//     //     i++;
//     // } while (i<=10);

//     return 0;
// }

// 40 -- To check whether a given number is palindrome or not
// a no. which is same after reverse.

// int main()
// {
//     int n,i,rev=0;
//     printf("Enter any number: ");
//     scanf("%d",&n);
//     i=n;
//     while (i>0)
//     {
//         rev=(rev*10)+(i%10);
//         i=i/10;
//     }
//     // printf("rev = %d\n",rev);
//     if (n==rev)
//     {
//         printf("The no. %d is Palindrome no.",n);
//     }
//     else
//         printf("The no %d is NOT a palindrome no.",n);

//     return 0;
// }

// 41 -- To determine whether a no is armstrong of not
// A no. that is equal to the sum of cube of its digits. i.e. 153 (1^3 + 5^3 + 3^3 = 153), 370,371,407,1634,8208 etc

// int main()
// {
//     int n,final,rem,sum=0,num,len=0,dig;
//     char arr[33];
//     printf("Enter any number: ");
//     scanf("%d",&n);

    // final=n;
    // while(final!=0)
    // {
    //     rem=final%10;
    //     sum=sum+(rem*rem*rem);
    //     final=final/10;
    // }

    //first convert into string, then iterate over each digit as a character of string, converting them back into digits to calculate their cube and adding them together. then equating the sum to original number taken from user as integer. 
//     sprintf(arr,"%d",n); //to convert int to str
//     // printf("%s\n",arr);
//     for (int i = 0; arr[i] != '\0'; i++)
//     {
//         if (isdigit(arr[i]))
//         {
//             dig = arr[i] - '0';
//             // printf("%d\n",dig);
//             sum = sum + pow(dig,3);
//         }
//     }
//     if (n==sum)
//     {
//         printf("The no %d is an Armstrong no.",n);
//     }
//     else
//         printf("The no. %d is NOT an Armstrong no.",n);
//     return 0;
// }

// 42 -- To calculate the sum of digits of a no.

// int main()
// {
//     int n,final,rem,digits=0;
//     printf("Enter the no.: ");
//     scanf("%d",&n);

//     final=n;
//     while (final!=0)
//     {
//         rem=final%10;
//         digits=digits+rem;
//         final=final/10;
//     }
//     printf("Sum of digits of %d = %d",n,digits);
//     return 0;
// }

// 43 -- To find A to the power b (A^b)

// int main()
// {
//     int A,b,result=1;
//     printf("Enter the no.: ");
//     scanf("%d",&A);
//     printf("Enter the power: ");
//     scanf("%d",&b);

//     while (b!=0)
//     {
//         result=result*A;  //A=2 and b=3 then, result=1x2=2 then 2x2=4 then 4x2=8, final result=8
//         b--;
//     }
//     printf("A to the power b = %d",result);
//     return 0;

// }

// 44 -- To find the factorial of a number

// int fact(int num)
// {
//     int i=1,f=1;
//     while (i<=num)
//     {
//         f = f * i;
//         i++;
//     }
//     return f;
// }

// int main()
// {
//     int n;
//     printf("Enter the no.: ");
//     scanf("%d",&n);
//     printf("Factorial of %d is %d",n,fact(n));
//     return 0;
// }

// 45 -- To display the fibonacci series

// int main()
// {
//     int n,i=1,n1=0,n2=1,next;
//     printf("Enter the no. of terms: ");
//     scanf("%d",&n);
//     printf("Fibonacci series upto %d terms is: \n\n",n);
//     while (i<=n)
//     {
//         printf("%d\t",next);
//         n1=n2;
//         n2=next;
//         next=n1+n2;
//         i++;
//     }
//     return 0;
// }

// 46 -- To display the AP series
// AP is a sequence of terms in which next term is obtained by adding common difference to previous term. FORMULA: (n+1)th = tn + D, where D is the comm. diff., tn is the nth term.
// int main()
// {
//     int terms,n1,d,i,ap;
//     printf("Enter the First no.: ");
//     scanf("%d",&n1);
//     printf("Enter the Common Difference (d): ");
//     scanf("%d",&d);
//     printf("Enter the no. of terms: ");
//     scanf("%d",&terms);

//     ap=n1;
//     for (i = 0; i < terms; i++)
//     {
//         printf("%d, ",ap);
//         ap=ap+d;

//         /*for sum of numbers in AP
//         printf("%d +",ap);
//         sum=sum+ap;
//         ap=ap+d; */
//     }
//     return 0;
// }

// 47 -- To check whether a no. is prime or not
// if we can find one more no. which is divisible by num, then it is not prime.
// int main()
// {
//     int n,i=2,value=0;
//     printf("Enter the no.: ");
//     scanf("%d",&n);
//     while (i<n)
//     {
//         if (n%i==0)  //check if n is divisible by any value of i between 2 and n.
//         {
//             value = value+1; //if yes, then increase the value by 1.
//         }
//         i++;
//     }

//     if (value==0)
//     {
//         printf("The no. %d is a Prime No.",n);
//     }
//     else
//     {
//         printf("The no. %d is NOT a Prime No.",n);
//     }
//     return 0;
// }

// 48 --To find the area of triagle using heron's formula
// FORMAULS: Area = √[s(s-a)(s-b)(s-c)]

// int main()
// {
//     int Area, peri, s, a, b, c;
//     printf("Enter the 3 sides of triangle: ");
//     scanf("%d %d %d",&a,&b,&c);

//     peri = a+b+c;
//     s=peri/2; //s is semiperimeter
//     Area = sqrt(s*(s-a)*(s-b)*(s-c));

//     // printf("perimeter is %d",peri);
//     // printf("s is %d",s);
//     printf("Area is %d",Area);

//     return 0;
// }

// 49 -- To print tables upto n numbers

// int main()
// {
//     int n,terms,i=1;
//     printf("Which number's table you want? ");
//     scanf("%d",&n);
//     printf("Upto how many terms you want to print the table? ");
//     scanf("%d",&terms);
//     while (i<=terms)
//     {
//         printf("%d x %d = %d\n",n,i,n*i);
//         i++;
//     }
//     return 0;
// }

// 50 -- To display right triangular star pattern

// int main()
// {
//     int i,j;
//     for (i = 1; i <= 5; i++)
//     {
//         for (j = 1; j <= i; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

// 51 -- To display pascal's triangle
/*
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1

. */

// int main()
// {
//     int rows,i,j;
//     printf("Upto how many rows you want to print the triangle? ");
//     scanf("%d",&rows);
//     for (i = 0; i < rows; i++)
//     {

//     }
//     return 0;
// }

// 52 -- To add 10 positibe numbers

// int main()
// {
//     int i,sum=0;
//     printf("Sum of 1st 10 positives numbers is: \n");
//     for (i = 1; i <= 10; i++)
//     {
//         sum=sum+i;
//     }
//     printf("%d",sum);
//     return 0;

// }

// 53 -- To add numbers until a negative number encounters

// int main()
// {
//     int n, sum=0;
//     printf("NOTE:- If you enter any negative number the program will end !!! \n");
//     do
//     {
//     printf("Enter the number: ");
//     scanf("%d",&n);
//         if (n>=0)
//         {
//             sum=sum+n;
//         }
//         else
//             goto end;
//     } while (1);
//     end:
//     printf("The sum of all numbers you entered (except negative no.) is %d",sum);
//     return 0;
// }

// 54 -- To find the square of a number using function

// int square(int num)
// {
//     return num*num;
// }

// int main()
// {
//     int n;
//     printf("Enter the number of which you want the square: ");
//     scanf("%d",&n);
//     printf("Square of %d is %d",n,square(n));
//     return 0;
// }

// 55 -- To convert the given height from cm to feet using functions

// float cmsTofeet(float h)
// {
//     return (h * 0.0328084);
// }

// int main()
// {
//     float height;
//     printf("Enter the height in CM: ");
//     scanf("%f",&height);
//     printf("%f CM = %f feet",height,cmsTofeet(height));
//     return 0;
// }

// 56 -- To find the area of circle using function

// float area(float r)
// {
//     return (3.14*r*r);
// }

// int main()
// {
//     int r;
//     printf("Enter the radious: ");
//     scanf("%d",&r);
//     printf("Area of circle is %f",(area(r)));
//     return 0;
// }

// int main()
// {
//     float expr = 2.0; // switch only takes int and char expresions
//     switch (expr)
//     {
//     case 1: printf("One");
//     case 2: printf("Two");
//     default: printf("default");
//     }
//     return 0;
// }

// int main()
// {
//     int a = 10, b = 20;
//     if (a=b)
//     {
//         printf("a is equal to b");
//     }
//     else
//         printf("a is not equal to b");
//     return 0;
// }

// prime factor

// int main()
// {
//     int n,i=2,value;
//     printf("Enter the number: ");
//     scanf("%d",&n);

//     printf("Factors of %d are:\n1 ",n);
//     while (i<=n)
//     {
//         if (n%i==0)
//         {
//             printf("%d ",i);
//             i++;
//         }
//         else
//         {
//             i++;
//             continue;
//         }
//     }
//     return 0;

// }

// int main()
// {
//     int avg, sum=0;
//     int marks[5];
//     for (int i = 0; i < 5; i++)
//     {
//         printf("Enter marks: ");
//         scanf("%d",&marks[i]);
//     }

//     for (int i = 0; i < 5; i++)
//     {
//         sum = sum + marks[i];
//     }
//     avg = sum/5;
//     printf("Average marks = %d",avg);
//     return 0;
// }

// int main()
// {
//     int i, A[10], n, beg, end, mid;
//     for (i = 0; i < 10; i++)
//     {
//         printf("Enter the number in the increasing order: ");
//         scanf("%d",&A[i]);
//     }
//     for (i = 0; i < 10; i++)
//     {
//         printf("No. in array are: %d \n", A[i]);
//     }

//     printf("Enter the umber that you want to search: ");
//     scanf("%d",&n);
//     beg=0;
//     end=9;
//     mid=(beg+end)/2;
//     while (beg <= end && A[mid] != n)
//     {
//         if (A[mid] < n)
//         {
//             beg = mid + 1;

//         }
//         else
//         {
//             end = mid -1;
//         }
//         mid = (beg + end)/2;
//     }
// (n == A[mid]) ? printf("No. found: %d",n) : printf("No. not found");
// if (n == A[mid])
// {
//     printf("No. found: %d",n);
// }
// else
// {
//     printf("No. not found");
// }

// return 0;
// }

// QUESTION -- WAP to find the smallest and largest no. in an array
// int main()
// {
//     int i,j,A[10],l,s;
//     for (int i = 0; i < 10; i++)
//     {
//         printf("Enter the no in array: ");
//         scanf("%d",&A[i]);
//     }
//     printf("Elements of array are: \n");
//     for(i = 0; i < 10; i++)
//     {
//         printf("%d, ",A[i]);
//     }

// l = A[0];
// for (int i = 0; i < 10; i++)
// {
//     if (l < A[i])
//     {
//         l = A[i];
//     }
// }
// printf("\nThe largest no. in array is: %d",l);

//     s = A[0];
//     for (int i = 0; i < 10; i++)
//     {
//         if (s > A[i])
//         {
//             s = A[i];
//         }
//     }
//     printf("\nThe smallest no. in array is: %d",s);
//     return 0;
// }

// wap to write details of a student and print it on screen as well as write into a file.
// #include<stdlib.h>
// int main()
// {
//     int roll;
//     char name[33];
//     float marks;
//     FILE *student;
//     student = fopen("student.txt", "a");

//     if (student == NULL)
//     {
//         printf("ERROR: File couldn't open");
//         exit(0);
//     }
//     else
//     {
//         printf("Enter Details of Studdent\n");
//         printf("Student Roll No.: ");
//         scanf("%d",&roll);
//         printf("Student Name: ");
//         scanf("%s",&name);
//         printf("Student Marks: ");
//         scanf("%f",&marks);

//         printf("Student's Roll No.:%d\nStudent's Name:%s\nStudent's Marks:%f",roll,name,marks);

//         fprintf(student,"\n\nStudent's Roll No.:%d\nStudent's Name:%s\nStudent's Marks:%f",roll,name,marks);
//     }
//     return 0;
// }

// WAP to write data into a file named input.txt. Again open the same file input.txt and display it on screen.
// #include <stdlib.h>
// int main()
// {
//     char str[100];
//     char ch;
//     FILE *fp;

//     fp = fopen("input", "a");

//     if (fp == NULL)
//     {
//         printf("ERROR: File couldn't open");
//         exit(0);
//     }
//     else
//     {
//         printf("Enter any String: \n");
//         gets(str);
//         fprintf(fp, "\n%s", str);
//         printf("String Successfully written into the file...");
//         fclose(fp);
//     }
//     fp = fopen("input", "r");
//     // wrong
//     while (ch = fgetc(fp) != EOF)
//     {
//         printf("%c", ch);
//     }
//     return 0;
// }
//-----------------------------------------------------------------------------
// struct student
// {
//     int roll;
//     char name[33];
//     float marks;
// }st[100];

// int main()
// {
//     int n,i;
//     printf("Enter the no of students: ");
//     scanf("%d",&n);
//     FILE *fp;
//     fp = fopen("student.md", "a");
//     if (fp == NULL)
//     {
//         printf("ERROR: File couldn't open");
//     }
//     else
//     {
//         for(i = 0; i < n; i++)
//         {
//             printf("DETAILS OF STUDENT #%d \n",(i+1));
//             printf("Enter Roll no.: ");
//             scanf("%d",&st[i].roll);
//             printf("Enter Name: ");
//             scanf("%s",&st[i].name);
//             printf("Enter Marks: ");
//             scanf("%f",&st[i].marks);
//         }
//         for (i = 0; i < n; i++)
//         {
//             printf("\nStudent #%d details are: \n",(i+1));
//             printf("Roll No.: %d\n",st[i].roll);
//             printf("Name: %s\n",st[i].name);
//             printf("Marks: %f\n",st[i].marks);
//         }
//         for (i = 0; i < n; i++)
//         {
//             fprintf(fp,"\n\nStudent #%d details are: \nRoll No.: %d\nName: %s\nMarks: %f\n",(i+1),st[i].roll,st[i].name,st[i].marks);
//         }
//     }
//     fclose(fp);
//     return 0;
// }

// int main()
// {
//     char arr[100]
//     int n;
//     FILE *fp;
//     fp = fopen("student.md", "r");
//     if (fp == NULL)
//     {
//         printf("ERROR: File couldn't open");
//     }
//     else
//     {
//         while (n=fread())
//         {
//             fscanf(fp, "%s", &arr);
//             printf("%s",arr);
//         }

//     }
// }
//------------------------------------------------------------------------------

// int main()
// {
//     int n;
//     FILE *fp, *fpe, *fpo;
//     fp = fopen("data.txt", "w");
//     if (fp == NULL)
//     {
//         printf("*******ERROR******");
//         exit(0);
//     }
//     else
//     {
//         printf("Enter numbers:\n");
//         for (int i = 0; i < 5; i++)
//         {
//             scanf("%d", &n);
//             putw(n, fp); // creates binary file
//             // fprintf(fp,"%5d", n); //creates text file
//         }
//     }
//     fclose(fp);
//     fp = fopen("data.txt", "r");
//     fpe = fopen("even.txt", "w+");
//     fpo = fopen("odd.txt", "w+");

//     while ((n = getw(fp)) != EOF)
//     {
//         if (n % 2 == 0)
//             // fprintf(fpe,"%5d",n);
//             putw(n, fpe);
//         else
//             // fprintf(fpo,"%5d",n);
//             putw(n, fpo);
//     }
//     fclose(fp);
//     fclose(fpe);
//     fclose(fpo);

//     fpe = fopen("even.txt", "r");
//     printf("\nEven numbers are:\n");
//     while ((n = getw(fpe)) != EOF)
//     {
//         printf("%5d", n);
//     }
//     fpo = fopen("odd.txt", "r");
//     printf("\nOdd numbers are:\n");
//     while ((n = getw(fpo)) != EOF)
//     {
//         printf("%5d", n);
//     }

//     fclose(fp);
//     fclose(fpe);
//     fclose(fpo);

//     return 0;
// }

//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------

// 2nd sem.

// 1. to take 5 values from the user and store them in an array.
// int main()
// {
//     int arr[5],i,n;
//     for (i = 0,n = 1; i < 5, n<=5; i++,n++)
//     {
//         printf("Enter value #%d : ",n);
//         scanf("%d",&arr[i]);
//     }
//     printf("Values stored in arr[5] are:\n");
//     for (i = 0; i < 5; i++)
//     {
//         printf("%5d",arr[i]);
//     }
//     return 0;
// }

// 2. program to display 5 values which are already initialized.
// int main()
// {
//     int arr[]={2,4,6,8,10},i;
//     printf("Values stored in arr[] are:\n");
//     for (i = 0; i < 5; i++)
//     {
//         printf("%5d",arr[i]);
//     }
//     return 0;
// }

// 3. program to find the average of n numbers using arrays
// int main()
// {
//     int n, arr[33], i;
//     float sum=0, av;
//     printf("Average of how many no. do you want to find: ");
//     scanf("%d",&n);
//     for (i = 0; i < n; i++)
//     {
//         printf("Enter the no.: ");
//         scanf("%d",&arr[i]);
//     }
//     for (i = 0; i < n; i++)
//     {
//         sum = sum + arr[i];
//     }
//     av = sum/n;
//     printf("The average of your %d no. is: %f ",n,av);
//     return 0;
// }

// 4. program to find the largest and smallest element of an array
// int main()
// {
//     int arr[100],i,s,l;
//     for (i = 0; i < 10; i++)
//     {
//         printf("enter no.: ");
//         scanf("%d",&arr[i]);
//     }
//     l = arr[0];
//     for (i = 0; i < 10; i++)
//     {
//         if (l < arr[i])
//         {
//             l = arr[i];
//         }
//     }
//     s = arr[0];
//     for (i = 0; i < 10; i++)
//     {
//         if (s > arr[i])
//         {
//             s = arr[i];
//         }
//     }
//     printf("Largest no = %d\nSmallest no. = %d",l,s);
//     return 0;
// }

// 5. program to sort array in ascending order
// int main()
// {
//     int arr[10],i,j,temp;
//     for (i = 0; i < 10; i++)
//     {
//         printf("Enter no.: ");
//         scanf("%d",&arr[i]);
//     }
//     for (i = 0; i < 10; i++)
//     {
//         for (j = i+1; j < 10; j++)
//         {
//             if (arr[i] > arr[j])
//             {
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//             }
//         }
//     }
//     printf("elements sorted in ascending order are: \n");
//     for (i = 0; i < 10; i++)
//     {
//         printf("%5d",arr[i]);
//     }
//     return 0;
// }

// 6. program to sort array in descending order
// int main()
// {
//     int arr[10],i,j,temp;
//     for (i = 0; i < 10; i++)
//     {
//         printf("Enter no.: ");
//         scanf("%d",&arr[i]);
//     }
//     for (i = 0; i < 10; i++)
//     {
//         for (j = i+1; j < 10; j++)
//         {
//             if (arr[i] < arr[j])
//             {
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//             }
//         }
//     }
//     printf("elements sorted in descending order are: \n");
//     for (i = 0; i < 10; i++)
//     {
//         printf("%5d",arr[i]);
//     }
//     return 0;
// }

// 7. Program to find size of an array
// int main()
// {
//     char arr[] = "My name is Yash Parwal";
//     int n;
//     n = sizeof(arr);
//     printf("Array is arr[] = %s",arr);
//     printf("\nSize of this array is %d",n);
// }

// 8. Program to find sum of array using function.
// int ArraySum(int *arr)
// {
//     int sum = 0
//     for (int i = 0; i < 6; i++)
//     {
//         sum = sum + arr[i];
//     }
//     printf("\nThe sum of elements of array is %d",sum);
// }
// int main()
// {
//     int arr[10];
//     printf("Enter elements: \n");
//     for (int i = 0; i < 6; i++)
//     {
//         scanf("%d",&arr[i]);
//     }
//     printf("Elements are: \n");
//     for (int i = 0; i < 6; i++)
//     {
//         printf("%5d",arr[i]);
//     }
//     ArraySum(&arr);
//     return 0;
// }

// program to merge two arrays
//  int main()
//  {
//      int A[5],B[5],C[10];
//      printf("Enter the elements in array A: ");
//      for (int i = 0; i < 5; i++)
//      {
//          scanf("%d",&A[i]);
//      }
//      printf("Enter the elements in array B: ");
//      for (int i = 0; i < 5; i++)
//      {
//          scanf("%d",&B[i]);
//      }

//     for (int i = 0; i < 5; i++)
//     {
//         C[i] = A[i];
//     }
//     for (int i = 0, j = 5; i < 5, j < 10; i++, j++)
//     {
//         C[j] = B[i];
//     }

//     printf("After merging the elements of array C are: \n");
//     for (int i = 0; i < 10; i++)
//     {
//         printf("%5d",C[i]);
//     }
//     return 0;
// }

// 9. program to access array elemets using pointers
// int main()
// {
//     int n;
//     printf("Enter the size of array: ");
//     scanf("%d",&n);
//     int arr[n];
//     printf("Enter the string in array: \n");

//***********************************************************************************************
//     // gets(arr);          
    //    not able to use gets after scanf, it takes "enter" of scanf as input and skips the gets function
    //    scanf() reads an integer and leaves a newline character in the buffer. So gets() only reads newline and the string in gets() is ignored by the program.
    
    // ------------------------------------------------------------------------------------------
    
    // when scanf() is used in loop
    // because every scanf() leaves a newline character in a buffer that is read by the next scanf.

    // ------------------------------------------------------------------------------------------

    // How to Solve the Above Problem?  
    /* 
    We can make scanf() to read a new line by using an extra \n, i.e., scanf(“%d\n”, &x) . In fact scanf(“%d “, &x) also works (Note the extra space).
    We can add a getchar() after scanf() to read an extra newline.

    LINKS:-
    1. https://www.quora.com/Why-is-the-gets-function-not-used-after-scanf
    2. https://stackoverflow.com/questions/2366509/input-in-c-scanf-before-gets-problem#comment54196331_2366509
    3. https://www.geeksforgeeks.org/problem-with-using-fgets-gets-scanf-after-scanf-in-c/
    */ 

    // ------------------------------------------------------------------------------------------
    /* 
    gets(3): "The gets() function cannot be used securely. Because of its lack of bounds checking, and the inability for the calling program to reliably determine the length of the next incoming line, the use of this function enables malicious users to arbitrarily change a running program's func- tionality through a buffer overflow attack. It is strongly suggested that the fgets() function be used in all cases. (See the FSA.)" Don't use it.
     */

//**********************************************************************************************

// for (int i = 0; i < n; i++)
//     {
//         // scanf("%d",(arr+i));
//         // or
//         scanf("%d",&arr[i]);
//     }
//     printf("The elements accessed using pointers are: \n");
//     for (int i = 0; i < n; i++)
//     {
//         // printf("%5d",*(arr+i));
//         // or
//         printf("%5d",*(&arr[i]));

// // v.v.v.v. IMP.    // printf("%5d",*(arr)); //this will give value of 1st place and if we add i like first case then it will give all values till n
//     }
//     return 0;
// }

// 10. Program to sort array using function.
// int arraySort(int *A)
// {
//     int temp;
//     for (int i = 0; i < 10; i++)
//     {
//         for (int j = (i+1); j < 10; j++)
//         {
//             if (A[i]>A[j])
//             {
//                 temp = A[i];
//                 A[i] = A[j];
//                 A[j] = temp;
//             }
//         }
//     }
//     printf("After sorting elements are: \n");
//     for (int i = 0; i < 10; i++)
//     {
//         printf("%5d", A[i]);
//     }
// }
// int main()
// {
//     int arr[33], temp;
//     printf("Enter elements in array: \n");
//     for (int i = 0; i < 10; i++)
//     {
//         scanf("%d",&arr[i]);
//     }
//     arraySort(&arr);
//     return 0;
// }

// 11. program to display 5 values in 2-D array which is already initialised.
// int main()
// {
//     int A[3][3] = {2,3,5,7,11,13,17,19,23};
//     printf("Elements in array are: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%5d",A[i][j]);
//         }
//     }
//     printf("\nFirst 6 values from the above array are: \n");
//     for (int i = 0; i < 2; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%5d",A[i][j]);
//         }
//     }
//     // while (A[i][j] != A[1][2])
//     // {
//     //     printf("%5d",A[i][j]);
//     // }
//     return 0;
// }

// 12. program to display 5 values from the user and store in 2D array
// int main()
// {
//     int A[3][2];
//     printf("Enter the elements of array: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 2; j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     printf("Elements stored in array are: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 2; j++)
//         {
//             printf("%5d",A[i][j]);
//         }
//         printf("\n");
//     }
//      return 0;
// }

// 13. Program to find addition of 2 matrices
// int main()
// {
//     int r,c,A[2][2], B[2][2], sum[2][2];
//     printf("Enter the no. of rows and coloumns: ");
//     scanf("%d%d",&r,&c);
//     printf("Enter elements of matrix A: \n");
//     for (int i = 0; i < r; i++)
//     {
//         for (int j = 0; j < c; j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     printf("Enter elements of matrix B: \n");
//     for (int i = 0; i < r; i++)
//     {
//         for (int j = 0; j < c; j++)
//         {
//             scanf("%d",&B[i][j]);
//         }
//     }
//     printf("Sum of matrix A and B is: \n");
//     for (int i = 0; i < r; i++)
//     {
//         for (int j = 0; j < c; j++)
//         {
//             sum[i][j] = A[i][j] + B[i][j];
//             printf("%5d",sum[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// 14. program to find multiplication of two matrices.
// int main()
// {
//     int A[3][3], B[3][3], mul[3][3],i,j,k;
//     printf("Enter elements in array A:\n");
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     printf("Enter elements in array B:\n");
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             scanf("%d",&B[i][j]);
//         }
//     }
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             mul[i][j]=0;
//             for (k = 0; k < 3; k++)
//             {
//                 mul[i][j] = mul[i][j] + (A[i][k] * B[k][j]);
//             }
//         }
//     }
//     printf("Multiplication of matrix A and B is:\n");
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             printf("%5d",mul[i][j]);
//         }
//         printf("\n");
//     }

//     return 0;

// }

// 15. Program to find transpose of a matrix
// int main()
// {
//     int A[3][3], trans[3][3],i,j;
//     printf("Enter elements in array A: \n");
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             scanf("%d",&A[i][j]);
//         }
//     }
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             trans[i][j] = A[j][i];
//         }
//     }
//     printf("Transpose of matrix A is:\n");
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 3; j++)
//         {
//             printf("%5d",trans[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// 16. Program to demonstrate multi-dimentional array
// int main()
// {
//     int multiDim[2][2][2],i,j,k;
//     printf("Enter 8 elements in array: \n");
//     for (i = 0; i < 2; i++)
//     {
//         for (j = 0; j < 2; j++)
//         {
//             for (k = 0; k < 2; k++)
//             {
//                 scanf("%d",&multiDim[i][j][k]);
//             }
//         }
//     }
//     printf("Elements stored are: \n");
//     for (i = 0; i < 2; i++)
//     {
//         for (j = 0; j < 2; j++)
//         {
//             for (k = 0; k < 2; k++)
//             {
//                 printf("multiDim[%d][%d][%d] = %d\n",i,j,k,multiDim[i][j][k]);
//             }
//         }
//     }
//     return 0;
// }

// 17. program to print address of a variable and a pointer variable
// int main()
// {
//     int a=12, *ptr;
//     ptr = &a;
//     printf("Address of variable 'a' is: %p\n",&a);
//     printf("Address of pointer variable *ptr is: %p\n",&ptr);
//     return 0;
// }

// 18. Program to swap two numbers using pointer variables (without using 3rd variable).
// int Swap(int *x, int *y)
// {
//     *x = *x + *y;
//     *y = *x - *y;
//     *x = *x - *y;
// }
// int main()
// {
//     int a=5, b=10;
//     printf("Before swapping:\na=%d\nb=%d\n",a,b);
//     Swap(&a,&b);
//     printf("After swapping:\na=%d\nb=%d",a,b);
//     return 0;
// }

// 19. program to swap two numbers using pointer variable (using 3rd variable).
// int Swap(int *x, int *y)
// {
//     int temp;
//     temp = *x;
//     *x = *y;
//     *y = temp;
// }
// int main()
// {
//     int a=6,b=8;
//     printf("Before swapping:\na=%d\nb=%d\n",a,b);
//     Swap(&a,&b);
//     printf("After swapping:\na=%d\nb=%d",a,b);
//     return 0;
// }

// 20. Program to demonstrate double pointer or pointer to pointer.
/*
A pointer is used to store the address of variables. So, when we define a pointer to pointer, the first pointer is used to store the address of the second pointer. Thus it is known as double pointers. */
// int main()
// {
//     int var = 100;
//     int *ptr1;
//     int **ptr2;
//     ptr1 = &var; //value at address of var
//     ptr2 = &ptr1; //value at address of ptr1 and ptr1 holds the value at address of var
//     printf("value of var: %d",var);
//     printf("\nvalue of var unsing *ptr1: %d",*ptr1);
//     printf("\nvalue of var usning **ptr2: %d",**ptr2);
//     return 0;
// }

// 21. program to increment pointer variable
// int main()
// {
//     int a = 10, *p;
//     p = &a;
//     printf("Value of 'a' is: %d",a);
//     printf("\nPost increment in a using pointer: %d",(*p)++);
//     printf("\nPost increment in a using pointer: %d",(*p)++);
//     printf("\n");
//     printf("\nPre increment in a using pointer: %d",++(*p));
//     printf("\nPre increment in a using pointer: %d",++(*p));

// }
// 22. program to decrement pointer variable
// int main()
// {
//     int a = 10, *p;
//     p = &a;
//     printf("Value of 'a' is: %d",a);
//     printf("\nPost decrement in a using pointer: %d",(*p)--);
//     printf("\nPost decrement in a using pointer: %d",(*p)--);
//     printf("\n");
//     printf("\nPre decrement in a using pointer: %d",--(*p));
//     printf("\nPre decrement in a using pointer: %d",--(*p));
//     return 0;
// }

// 23. program to find largest of 3 numbers using pointer
// int main()
// {
//     int a=10, b=7, c=11, *p1, *p2, *p3;
//     p1 = &a;
//     p2 = &b;
//     p3 = &c;
//     printf("a=%d\tb=%d\tc=%d\n",*p1,*p2,*p3);
//     if (*p1 > *p2)
//     {
//         if (*p1 > *p3)
//             printf("no. a i.e. %d is largest\n",*p1);
//         else
//             printf("no. c i.e. %d is largest\n",*p3);
//     }
//     else
//     {
//         printf("no. b i.e. %d is largest\n",*p2);
//     }
//     return 0;
// }

// 24. program to create, access and initialize a pointer.
// int main()
// {
//     char ch='Y';
//     char *ptr; //creating pointer variable of char type.
//     ptr = &ch; // innitializing pointer with the address of variable ch.
//     //accessing the pointer variable and printing its value and address.
//     printf("Value of variable ch using pointer is: %c\n",*ptr);
//     printf("Address of variable ch using pointer is: %p\n",ptr);

// }

// 25. program to print any given string
// int main()
// {
//     char str1[]="This is a sting", str2[]="Strings are always enclosed in double quotes";
//     printf("%s\n",str1);
//     printf("%s",str2);
// }

// 26. Program to count the no. of vowels, Consonent, and so on.
// int main()
// {
//     char str[100];
//     int v=0, c=0, d=0, s=0, i;
//     printf("Enter any sentence: \n");
//     gets(str);
//     for (i = 0; str[i] != '\0'; i++)
//     {
//         if (str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' || str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U' )
//         {
//             v++;
//         }
//         else if (str[i]>='a' && str[i]<='z' || str[i]>='A' && str[i]<='Z')
//         {
//             c++;
//         }
//         else if (str[i]>='0' && str[i]<='9')
//         {
//             d++;
//         }
//         else if (str[i]==' ')
//         {
//             s++;
//         }
//     }
//     printf("No. of vowels are: %d",v);
//     printf("\nNo. of consonent are: %d",c);
//     printf("\nNo. of digits are: %d",d);
//     printf("\nNo. of white spaces are: %d",s);
//     return 0;
// }

// 27. program tto find length of a given string
// int main()
// {
//     char str[100];
//     int len;
//     printf("Enter the string: ");
//     gets(str);
//     len = strlen(str);
//     printf("Length of string is: %d",len);
//     return 0;
// }

// 28. program to concatinate 2 string.
// int main()
// {
//     char str1[3], str2[15];
//     printf("Enter something in str1: ");
//     gets(str1);
//     printf("Enter something in str2: ");
//     gets(str2);
//     strcat(str1, str2);
//     printf("Concatinated string is: \n");
//     puts(str1);
// }

// 29. program to copy string without using strcpy().
// int main()
// {
//     char str1[100], cpstr[100];
//     int i;
//     printf("Enter the string: ");
//     gets(str1);
//     for (i = 0; str1[i] != '\0'; i++)
//     {
//         cpstr[i] = str1[i];
//     }
//     printf("Copied string cpstr[] is: \n");
//     puts(cpstr);
//     return 0;
// }

// 30. program to copy string using strcpy()
// int main()
// {
//     char str1[100], cpstr[100];
//     int i;
//     printf("Enter the string: ");
//     gets(str1);
//     strcpy(cpstr, str1);
//     printf("Copied string is: \n");
//     puts(cpstr);
//     return 0;
// }

// 31. program to reverse a string using recursion
// void revStr();
// void swap();

// int main()
// {
//     char str[100];
//     int f=0, l;
//     printf("Enter any sentence: ");
//     gets(str);
//     l = strlen(str);
//     revStr(str, f, l-1);
//     // revStr(str, 0, l-1);
//     printf("Reversed string is:\n %s",str);
//     return 0;
// }
// void swap(char *x, char *y)
// {
//     char temp;
//     temp = *x;
//     *x = *y;
//     *y = temp;
// }
// void revStr(char str[], int f, int l)
// {
//     // f = 0;
//     if (f < l)
//     {
//         swap(&str[f], &str[l]);
//         revStr(str, f+1, l-1);
//     }
// }

// 32. Program to store info. of a student using structure
// struct student
// {
//     int roll;
//     char name[33];
//     char addr[33];
//     float marks;
// }s1;
// int main()
// {
//     printf("Enter Student's Roll no: ");
//     scanf("%d",&s1.roll);
//     printf("Enter Student's Name: ");
//     scanf("%s",&s1.name);
//     // gets(s1.name);
//     printf("Enter Student's Address: ");
//     scanf("%s",&s1.addr);
//     // gets(s1.addr);

// //not able to use 2 gets one after another, it skips 1st gets and get to the 2nd gets

//     printf("Enter Student's Marks: ");
//     scanf("%f",&s1.marks);
//     printf("\n-----Info. Stored-----\n");
//     printf("Student's Roll no is: %d\n",s1.roll);
//     printf("Student's Name is: %s\n",s1.name);
//     printf("Student's Address is: %s\n",s1.addr);
//     printf("Student's Marks are: %f\n",s1.marks);

//     return 0;
// }

// 33. Program to add two distances (in inch-feet system) using structures
// struct distance
// {
//     float feet;
//     float inch;
// }d1,d2,sum;
// int main()
// {
//     printf("Enter 1st distance in feet: ");
//     scanf("%f",&d1.feet);
//     printf("Enter 2nd distance in feet: ");
//     scanf("%f",&d2.feet);
//     sum.feet = d1.feet + d2.feet;
//     printf("Enter 1st distance in inch: ");
//     scanf("%f",&d1.inch);
//     printf("Enter 2nd distance in inch: ");
//     scanf("%f",&d2.inch);
//     sum.inch = d1.inch + d2.inch;
//     printf("Sum of distances:\n%f feet\n%f inchs",sum.feet,sum.inch);
// }

// 34. program to add two complex no. by passing structure to a function
//-----------------------------------------------------------------------------------
// typedef struct complex{
//     float  real;
//     float imag;
// }COMPLEX;
/* This is a struct complex which has been typedef'ed to COMPLEX. You can now use both struct complex c1; and COMPLEX c1;. */
// v.v.v.v IMP
//-------------------------------------------------------------------------------------
// struct complex
// {
//     int real;
//     int img;
// }n1, n2, sum;
// struct complex addition(struct complex n1, struct complex n2)
// {
//     struct complex sum;
//     sum.real = n1.real + n2.real;
//     sum.img = n1.img + n2.img;
//     return(sum);
// }
// int main()
// {
//     // complex n1, n2, sum;
//     printf("For 1st complex no.\nEnter real no. and imaginary. no: ");
//     scanf("%d%d",&n1.real, &n1.img);
//     printf("For 2nd complex no.\nEnter real no. and imaginary. no: ");
//     scanf("%d%d",&n2.real, &n2.img);
//     sum = addition(n1, n2);
//     printf("Sum = %d+%di",sum.real,sum.img);
//     return 0;
// }

// 35. program to find difference between two time periods.
// struct time
// {
//     int h;
//     int m;
//     int s;
// }start, stop, diff;
// struct time timePeriod(struct time start, struct time stop)
// {
//     if (stop.s > start.s)
//         diff.s = stop.s - start.s;
//     else
//         diff.s = start.s - stop.s;

//     if (stop.m > start.m)
//         diff.m = stop.m - start.m;
//     else
//         diff.m = start.m - stop.m;

//     if (stop.h > start.h)
//         diff.h = stop.h - start.h;
//     else
//         diff.h = start.h - stop.h;

//     return(diff);
// }
// int main()
// {
// printf("Enter Start time in h:m:s: \n");
// scanf("%d%d%d", &start.h, &start.m, &start.s);
// printf("Enter Stop time in h:m:s: \n");
// scanf("%d%d%d", &stop.h, &stop.m, &stop.s);
//     diff = timePeriod(start, stop);
//     printf("Difference between time periods is:\n%d:%d:%d - %d:%d:%d = %d:%d:%d", start.h,start.m,start.s,stop.h,stop.m,stop.s,diff.h,diff.m,diff.s);
// }

// #include <stdio.h>
// struct TIME
// {
//     int seconds;
//     int minutes;
//     int hours;
// };
/*
void TimePeriod(struct TIME t1, struct TIME t2, struct TIME *diff);
int main()
{
    struct TIME startTime, stopTime, diff;
    printf("Enter Start time in h:m:s: \n");
    scanf("%d %d %d", &startTime.hours, &startTime.minutes, &startTime.seconds);
    printf("Enter Stop time in h:m:s: \n");
    scanf("%d %d %d", &stopTime.hours, &stopTime.minutes, &stopTime.seconds);
    // Calculate the difference between the start and stop time period.
    TimePeriod(startTime, stopTime, &diff);
    printf("\nTIME DIFFERENCE: %d:%d:%d - ", startTime.hours, startTime.minutes, startTime.seconds);
    printf("%d:%d:%d ", stopTime.hours, stopTime.minutes, stopTime.seconds);
    printf("= %d:%d:%d\n", diff.hours, diff.minutes, diff.seconds);
    return 0;
}
void TimePeriod(struct TIME start, struct TIME stop, struct TIME *diff)
{
    if (stop.seconds > start.seconds)
    {
        --start.minutes;
        start.seconds += 60;
    }
    diff->seconds = start.seconds - stop.seconds;
    if (stop.minutes > start.minutes)
    {
        --start.hours;
        start.minutes += 60;
    }
    diff->minutes = start.minutes - stop.minutes;
    diff->hours = start.hours - stop.hours;
}
 */
// 36. program to demonstrate malloc() using function.
// int mallocUsage();
// int main()
// {
//     int *ptr;
//     ptr = (int*)malloc(5 * sizeof(ptr));
//     mallocUsage(&ptr);
//     free(ptr);
//     return 0;
// }
// int mallocUsage(int *ptr)
// {
//     for (int i = 0; i < 5; i++)
//     {
//         printf("Enter element #%d: ",(i+1));
//         scanf("%d",&ptr[i]);
//     }
//     printf("The values are stored in *ptr using malloc() function: \n");
//     for (int i = 0; i < 5; i++)
//     {
//         printf("%5d",ptr[i]);
//     }
// }

// 37. program to demonstrate calloc() using function.
// int callocUsage();
// int main()
// {
//     int *ptr;
//     ptr = (int*)calloc(5, sizeof(ptr));
//     callocUsage(&ptr);
//     free(ptr);
//     return 0;
// }
// int callocUsage(int *ptr)
// {
//     for (int i = 0; i < 5; i++)
//     {
//         printf("Enter element #%d: ",(i+1));
//         scanf("%d",&ptr[i]);
//     }
//     printf("The values are stored in *ptr using calloc() function: \n");
//     for (int i = 0; i < 5; i++)
//     {
//         printf("%5d",ptr[i]);
//     }

// }

// 38. program to demonstrate realloc() using functions.
// ----------------- THIS MAY BE WRONG---------------------
// int reallocUsage();
// int main()
// {
//     int *ptr;
//     // printf("Enter the size of array: ");
//     // scanf("%d",&n);
//     ptr = (int*)malloc(5 * sizeof(ptr));
//     for (int i = 0; i < 5; i++)
//     {
//         printf("Enter value #%d: ",(i+1));
//         scanf("%d",&ptr[i]);
//     }
//     printf("Values stored using calloc() function:\n");
//     for (int i = 0; i < 5; i++)
//     {
//         printf("%5d",ptr[i]);
//     }
//     printf("\n");
//     ptr = (int*)realloc(ptr, 8 * sizeof(ptr));
//     reallocUsage(&ptr);
//     free(ptr);
//     return 0;
// }
// int reallocUsage(int *ptr)
// {
//     // int n;
//     // printf("Enter the NEW size of array: ");
//     // scanf("%d",&n);
//     for (int i = 0; i < 8; i++)
//     {
//         printf("Enter element #%d: ",(i+1));
//         scanf("%d",&ptr[i]);
//     }
//     printf("The values are stored in *ptr using calloc() function: \n");
//     for (int i = 0; i < 8; i++)
//     {
//         printf("%5d",ptr[i]);
//     }
// }
// -----------------------THIS IS CORRECT ----------------------------
// int reallocUsage();
// int main()
// {
//     int *ptr,n;
//     printf("Enter the size of array: ");
//     scanf("%d",&n);
//     ptr = (int*)malloc(n * sizeof(ptr));
//     for (int i = 0; i < n; i++)
//     {
//         printf("Enter value #%d: ",(i+1));
//         scanf("%d",&ptr[i]);
//     }
//     printf("Values stored using calloc() function:\n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%5d",ptr[i]);
//     }
//     printf("\n");
//     reallocUsage(&ptr,n);
//     free(ptr);
//     return 0;
// }
// int reallocUsage(int **p, int n) //double pointer mean:- pointer p stores the address of pointer ptr
// {
//     printf("Enter the NEW size of array: ");
//     scanf("%d",&n);
//     *p = realloc(*p, n * sizeof(int));
//     for (int i = 0; i < n; i++)
//     {
//         printf("Enter element #%d: ",(i+1));
//         scanf("%d",&p[i]);
//     }
//     printf("The NEW values are stored in *ptr using realloc() function: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%5d",p[i]);
//     }
// }

// 39. program to demonstrate free() using funnction
// int freeUsage();
// int main()
// {
//     int *ptr;
//     ptr = (int *)calloc(7, sizeof(ptr));
//     freeUsage(&ptr);
//     free(*ptr);
//     printf("\nValues of ptr after using free() function=\n");
//     for (int i = 0; i < 7; i++)
//     {
//         printf("%5d", ptr[i]);
//     }
// }
// int freeUsage(int *ptr)
// {
//     if (ptr != NULL)
//     {
//         *(ptr + 5) = 25;
//         printf("The 5th element in array is: %d\n", *(ptr + 5));
//     }
//     printf("\nValues of ptr before using free() function=\n");
//     for (int i = 0; i < 7; i++)
//     {
//         printf("%5d", ptr[i]);
//     }
// }

// 40. prrogram to store employee's info as entered by user from console. 
// struct employee
// {
//     int id;
//     char name[33];
//     int salary;
// };
// int main()
// {
//     int n;
//     printf("Enter the no. of employees: ");
//     scanf("%d",&n);
//     struct employee emp[n];
//     for (int i = 0; i < n; i++)
//     {
//         printf("--------INFO. OF EMPLOYEE #%d---------\n",(i+1));
//         printf("Enter Id: ");
//         scanf("%d",&emp[i].id);
//         printf("Enter Name: ");
//         scanf("%s",&emp[i].name);
//         printf("Enter Salary: ");
//         scanf("%d",&emp[i].salary);
//     }
//     for (int i = 0; i < n; i++)
//     {
//         printf("\n--------INFO. OF EMPLOYEE #%d STORED---------\n",(i+1));
//         printf("ID: %d\n",emp[i].id);
//         printf("Name: %s\n",emp[i].name);
//         printf("Salary: %d\n",emp[i].salary);
//     }
    
//     return 0;
// }

// 41. Program to demonstrate the working of array of structure
// struct books
// {
//     int id;
//     char name[33];
//     int shelfno;
// };
// int main()
// {
//     int n;
//     printf("Enter the no. of books: ");
//     scanf("%d",&n);
//     struct books b[n];
//     for (int i = 0; i < n; i++)
//     {
//         printf("--------INFO. OF BOOK #%d---------\n",(i+1));
//         printf("Enter Book Id: ");
//         scanf("%d%*c",&b[i].id);
//         /*
//         The %*c term causes scanf to read in one character (the newline) but the asterisk causes the value to be discarded. This will make scanf eat the newline without requiring a separate function call. 
//         LINK:- https://stackoverflow.com/questions/2366509/input-in-c-scanf-before-gets-problem#comment54196331_2366509
//         OR use fflush() function to eat the newline character stored in buffer by scanf
//         */

//         // scanf("%d",&b[i].id);
//         // fflush(stdin); //because scanf leaves a newline character in the buffer that is read by next scanf of gets or or any other input function and skips it
//         printf("Enter Book Name: ");
//         gets(b[i].name);
//         printf("Enter Book Shelf No.: ");
//         scanf("%d",&b[i].shelfno);
//     }
//     for (int i = 0; i < n; i++)
//     {
//         printf("\n--------INFO. OF BOOK #%d STORED---------\n",(i+1));
//         printf("ID: %d\n",b[i].id);
//         printf("Name: %s\n",b[i].name);
//         printf("Salary: %d\n",b[i].shelfno);
//     }   
//     return 0;
// }

// 42. Program to demonstrate the working of pointers of structure
// struct passenger
// {
//     char name[33];
//     int id;
//     int seat;
// };
// int main()
// {
//     struct passenger *ptr;
//     int n;
//     printf("Enter the no. of passengers: ");
//     scanf("%d",&n);
//     fflush(stdin);
//     ptr = (struct passenger*) malloc(n * sizeof(struct passenger));
//     for (int i = 0; i < n; i++)
//     {
//         printf("\n-----FOR PASSENGER #%d-----\n",(i+1));
//         printf("Enter name: ");
//         gets((ptr+i)->name);
//         // fgets((ptr+i)->name,n,stdin); //only takes first character of any string
//         // scanf("%s",&(ptr+i)->name); //only takes first string till a white space chracter
//         fflush(stdin);
//         printf("Enter Id: ");
//         scanf("%d",&(ptr+i)->id);
//         fflush(stdin);
//         printf("Enter Seat no.: ");
//         scanf("%d",&(ptr+i)->seat);
//         fflush(stdin);
//     }
//     for (int i = 0; i < n; i++)
//     {
//         printf("\n-----INFO. OF PASSENGER #%d STORED-----\n",(i+1));
//         printf("ID: %d\n",(ptr+i)->id);
//         printf("Name: %s\n",(ptr+i)->name);
//         // fputs((ptr+i)->name,stdin);
//         // puts((ptr+i)->name);
//         printf("Seat no.: %d\n",(ptr+i)->seat);
//     }
//     return 0;   
// }

// 43. Program to demonstrate the working of unions 
// union students
// {
//     int a;
//     char b;
// }var;
// int main()
// {
//     printf("|--------------------------------------------------------|\n");
//     printf("This is a program to demonstrate Union\n");
//     printf("|--------------------------------------------------------|\n");
//     printf("As we know members of union share same memoory location, So when we assign 65 to a, \nthis '65' is also shared by b and b will take 65 as ascii code because of its char type \nand will print the normal value for ASCII code 65 that is 'A'.\n");
//     printf("|--------------------------------------------------------|\n");
//     var.a=65;
//     printf("a (assigned value)= %d\n",var.a);
//     printf("b (ASCII value of 65)= %c",var.b);
//     return 0;
// }

// 44. Program to demonstrate working of nested structure
// struct train    
// {
//     int PNR;
//     int trainNO;
//     char trainNAME[33];
//     struct passenger
//     {
//         int id;
//         char name[33];
//         int seat;
//     }pass;
// }t;

// int main()
// {
//     printf("Enter PNR no.: ");
//     scanf("%d",&t.PNR);
//     printf("Enter Train no.: ");
//     scanf("%d",&t.trainNO);
//     fflush(stdin);
//     printf("Enter Train Name: ");
//     fgets(t.trainNAME,sizeof(t.trainNAME),stdin);
//     fflush(stdin);
//     printf("-------------------------------------------------\n");
//     printf("Enter passenger ID: ");
//     scanf("%d",&t.pass.id);
//     fflush(stdin);
//     printf("Enter passenger Name: ");
//     fgets(t.pass.name,sizeof(t.pass.name),stdin);
//     fflush(stdin);
//     printf("Enter passenger Seat No.: ");
//     scanf("%d",&t.pass.seat);
//     printf("\n\n ***************INFORMATION STORED***************\n");
//     printf("PNR no.: %d\n",t.PNR);
//     printf("Train no.: %d\n",t.trainNO);
//     printf("Train Name.: %s\n",t.trainNAME);
//     printf("Passenger ID: %d\n",t.pass.id);
//     printf("Passenger Name.: %s",t.pass.name);
//     printf("Passenger Seat No.: %d\n",t.pass.seat);
// }



