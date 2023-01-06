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

// first convert into string, then iterate over each digit as a character of string, converting them back into digits to calculate their cube and adding them together. then equating the sum to original number taken from user as integer.
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
//------------------------------------------- 2nd SEM --------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------

//

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
//    not able to use gets after scanf, it takes "\n" of scanf as input and skips the gets function
//    scanf() reads an input and leaves a newline character in the buffer. So gets() only reads newline and the string in gets() is ignored by the program.

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
gets(3): "The gets() function cannot be used securely. Because of its lack of bounds checking, and the inability for the calling program to reliably determine the length of the next incoming line, the use of this function enables malicious users to arbitrarily change a running program's func-tionality through a buffer overflow attack. It is strongly suggested that the fgets() function be used in all cases. (See the FSA.)" Don't use it.
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
//     printf("The values are stored in *ptr using recalloc() function: \n");
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
//         printf("Shelf No.: %d\n",b[i].shelfno);
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
//         // fflush(stdin);
//         printf("Enter Id: ");
//         scanf("%d",&(ptr+i)->id);
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

// 45 & 46 -- Program to demonstrate functions fputc() and fgetc()
// void main() {
//     FILE *fp;
//     char ch;

//  //write a character to a file
//     fp = fopen("file.c", "w");
//     fputc('Y', fp);
//     fclose(fp);

//  //read a character from a file
//     fp = fopen("file.c", "r");
//     while((ch = fgetc(fp)) != EOF) {
//         printf("%c", ch);
//     }
//     fclose(fp);
//     printf("\n");
// }

// 47 -- Program to demonstrate functions fputs() and fgets()
// int main()
// {
//     FILE *fptr = fopen("file.txt","w");
//     fputs("Yash Parwal\nAge - 19",fptr);
//     fclose(fptr);

//     fptr = fopen("file.txt","r");
//     char ch[20];
//     while(fgets(ch,20,fptr)!=NULL)
//     {
//         printf("%s",ch);
//     }

//     fclose(fptr);

//     return 0;
// }

// 48 -- Program to demonstrate fseek()
// int main()
// {
//     FILE *fp;
//     int c;
//     fp = fopen("file.txt", "w+");
//     fputs("Visit to my website https://www.fake.com", fp);
//     fseek(fp, 20, SEEK_SET);                       // put the cursor at 7th index
//     fputs("https://www.getintocomputers.com", fp); // from 7th index the pre written statement will get overwritten
//     fclose(fp);

//     //    to see the contents of file, lets open it...
//     fp = fopen("file.txt", "r");
//     while (1)
//     {
//         c = fgetc(fp);
//         if (feof(fp))
//         {
//             break;
//         }
//         printf("%c", c);
//     }
//     fclose(fp);
//     return (0);
// }

// 49 -- program to read the first line from a file
// int main()
// {
//     char arr[50], ch;
//     int i = 0;
//     FILE *fp;
//     fp = fopen("file.txt", "w");
//     fputs("This is the first line of file\nThis is the second line of the file.", fp);
//     fclose(fp);

//     fp = fopen("file.txt", "r");
//     if ((fp = fopen("file.txt", "r")) != NULL)
//     {
//         fscanf(fp, "%[^\n]", arr);
//         printf("%s", arr);
//     }
//     fclose(fp);
//     return 0;
// }

// 50 -- Program to display its own source code
// int main()
// {
//     FILE *fp;
//     char c;
//     fp = fopen(__FILE__,"r");

//     while (c != EOF)
//     {
//         c = getc(fp);
//         printf("%c",c);
//     }

//     fclose(fp);
//     return 0;
// }

// // 51 -- Program to open the file in write mode
// int main()
// {
//     char arr[33],c;
//     FILE *fp;
//     fp = fopen("file.txt","w");
//     if (fp == NULL)
//     {
//         printf("ERROR: Can't open the file");
//         return (-1);
//     }
//     printf("file.txt is opened in write mode.\nYou can give any input.\n");
//     gets(arr);
//     fputs(arr, fp);
//     fclose(fp);
//     printf("Data successfully written into file.txt\nLets open the file.txt and see the content...\n");
//     fp = fopen("file.txt","r");
//     while (c != EOF)
//     {
//         c = getc(fp);
//         printf("%c",c);
//     }
//     fclose(fp);
// }
// 52 -- Program to demonstrate the working of fopen and fclose
// int main()
// {
//     char arr[33],c;
//     FILE *fp;
//     fp = fopen("file.txt","w+");
//     if (fp == NULL)
//     {
//         printf("ERROR: Can't open the file");
//         return (-1);
//     }
//     printf("file.txt is opened in write mode.\nYou can give any input.\n");
//     gets(arr);
//     fputs(arr, fp);
//     fclose(fp);
//     printf("file.txt is closed\nWe now cannot give any input... \nBUT lets try to give any input and see if it is stored in file.txt or not\n");
//     gets(arr);
//     fputs(arr, fp);
//     printf("Data successfully written into file.txt\nLets open the file.txt and see the content...\n");
//     fp = fopen("file.txt","r");
//     while (c != EOF)
//     {
//         c = getc(fp);
//         printf("%c",c);
//     }
//     fclose(fp);
// }

//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//------------------------------------------- 3rd SEM --------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------------------------------------


// --------------------------------------------------------------------------------
// 1. program to traversing or printing value of array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[] = {6,7,1,3,4,0,9,10};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     printf("Array is: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     printf("\nTraversing each element of an array: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("Element %d Traversed...\n",arr[i]);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 2. Program to insert an element at any position in array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[10] = {6,7,1,3,4};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     int n = 5;
//     int data, index;
//     printf("Array is: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     printf("\nEnter the data to be insrted: ");
//     scanf("%d",&data);
//     printf("\nEnter the index no. (between 1 to 10): ");
//     scanf("%d",&index);
//     n++;
//     for (int i = size-1; i >= index ; i--)
//     {
//         arr[i] = arr[i-1];
//     }
//     arr[index] = data;
//     printf("\nArray after insertion is: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 3. Program to search element in an array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[] = {6,7,1,3,4,9};
//     int n = 6;
//     int data, i=0;
//     printf("Array is: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     printf("\nEnter the element you want to search: ");
//     scanf("%d",&data);
//     for (i; i < n; i++)
//     {
//         if (arr[i] == data)
//         {
//             printf("Element %d found on index no. %d",data,i);
//             break;
//         }
//     }
//     if (i == 6)
//         printf("Element not found in above array !!!");
//     return 0;
// }

// --------------------------------------------------------------------------------
// 4. program to reversing the array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[] = {6,7,1,3,4,9};
//     int n = 6;
//     printf("Array is: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ",arr[i]);
//     }
//     printf("\nResersed Array is: \n");
//     for (int i = n-1; i >= 0; i--)
//     {
//         printf("%d ",arr[i]);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 5. Program to merge two sorted array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr1[] = {8, 4, 6, 2, 10};
//     int s1 = 5;
//     int arr2[] = {16, 12, 14, 18};
//     int s2 = 4;
//     int arr3[9];
//     printf("Array 1: \n");
//     for (int i = 0; i < 4; i++)
//     {
//         printf("%d ", arr1[i]);
//     }
//     printf("\nArray 2: \n");
//     for (int i = 0; i < 4; i++)
//     {
//         printf("%d ", arr2[i]);
//     }

//     printf("\nMerging Array1 and Array2...");
//     for (int i = 0; i < s1; i++)
//     {
//         arr3[i] = arr1[i];
//     }
//     int j = s1;
//     for (int i = 0; i < s2; i++)
//     {
//         arr3[j] = arr2[i];
//         j++;
//     }
//     //sorting the array
//     for (int i = 0; i < 9; i++)
//     {
//         int temp;
//         for (int j = i+1; j < 9; j++)
//         {
//             if (arr3[i] > arr3[j])
//             {
//                 temp = arr3[i];
//                 arr3[i] = arr3[j];
//                 arr3[j] = temp;
//             }
//         }
//     }
//     printf("\nSorted array after merging: \n");
//     for (int i = 0; i < 9; i++)
//     {
//         printf("%d ", arr3[i]);
//     }

//     return 0;
// }

// --------------------------------------------------------------------------------
// 6. program to sort array in assending array
// --------------------------------------------------------------------------------

// int swap(int *x, int *y)
// {
//     int temp = *x;
//     *x = *y;
//     *y = temp;
// }
// int main()
// {
//     int arr[] = {7, 2, 1, 9, 8, 3};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     printf("Array is : \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ", arr[i]);
//     }
//     for (int i = 0; i < size-1; i++)
//     {
//         for (int j = i + 1; j < size; j++)
//         {
//             if (arr[i] > arr[j])
//             {
//                 swap(&arr[i],&arr[j]);
//             }
//         }
//     }
//     printf("\nArray sorted in assending order: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ", arr[i]);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 7. program to delete an element in array
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[] = {6,7,1,3,4,9};
//     int size = sizeof(arr)/sizeof(arr[0]);
//     int n,index=0;
//     printf("Array is: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ", arr[i]);
//     }
//     printf("\nEnter the element you want to delete: ");
//     scanf("%d",&n);
//     for (int i = 0; i < size; i++)
//     {
//         if (arr[i] == n)
//         {
//             printf("Element '%d' deleted from arr[%d]",arr[i],i);
//             index = i;
//             break;
//         }
//     }
//     for (int i=index; i < size; i++)
//     {
//         arr[i] = arr[i+1];
//     }
//     size--;
//     printf("\nArray after deleting element: \n");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d ", arr[i]);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 8. Program to addition of two matrix
// --------------------------------------------------------------------------------

// int main()
// {
//     int A[3][3] = {4,8,3,2,9,1,6,9,7};
//     int B[3][3] = {14,18,13,12,19,11,16,19,17};
//     int C[3][3];
//     printf("Matrix A is: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d ",A[i][j]);
//         }
//         printf("\n");
//     }
//     printf("Matrix B is: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d ",B[i][j]);
//         }
//         printf("\n");
//     }
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             C[i][j] = A[i][j]+B[i][j];
//         }
//     }
//     printf("Matrix A + Matrix B = \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d ",C[i][j]);
//         }
//         printf("\n");
//     }

// }

// --------------------------------------------------------------------------------
// 9 Program to multiplication of two matrix
// --------------------------------------------------------------------------------

// int main()
// {
//     int A[3][3] = {4,8,3,2,9,1,6,9,7};
//     int B[3][3] = {9,5,2,1,3,1,4,2,5};
//     int mul[3][3];
//     int i,j,k;
//     printf("Matrix A is: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d ",A[i][j]);
//         }
//         printf("\n");
//     }
//     printf("Matrix B is: \n");
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%d ",B[i][j]);
//         }
//         printf("\n");
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
//             printf("%d ",mul[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 10 program of sparse array or sparse matrix
// --------------------------------------------------------------------------------

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

// --------------------------------------------------------------------------------
// 11 Program to find Lower Triangular Matrix
// --------------------------------------------------------------------------------

// A lower-triangular matrix is a matrix which only has nonzero entries on the downwards-diagonal and below it
// int main()
// {
//  	int arr[3][3] = {2,5,3,9,5,6,1,8,7},i,j;
//  	printf("Matrix is: \n");
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3;j++)
//     	{
//       		printf("%d ", arr[i][j]);
//     	}
//         printf("\n");
//   	}
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3; j++)
//     	{
//     		if(i < j)
//     			arr[i][j] = 0;
//    	 	}
//   	}
//     printf("Matrix is: \n");
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3;j++)
//     	{
//       		printf("%d ", arr[i][j]);
//     	}
//         printf("\n");
//   	}
//  	return 0;
// }

// --------------------------------------------------------------------------------
// 12 Program to find Upper Triangular Matrix
// --------------------------------------------------------------------------------

// int main()
// {
//  	int arr[3][3] = {2,5,3,9,5,6,1,8,7},i,j;
//  	printf("Matrix is: \n");
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3;j++)
//     	{
//       		printf("%d ", arr[i][j]);
//     	}
//         printf("\n");
//   	}
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3; j++)
//     	{
//     		if(i > j)
//     			arr[i][j] = 0;
//    	 	}
//   	}
//     printf("Matrix is: \n");
//  	for(i = 0; i < 3; i++)
//   	{
//    		for(j = 0; j < 3;j++)
//     	{
//       		printf("%d ", arr[i][j]);
//     	}
//         printf("\n");
//   	}
//  	return 0;
// }

// --------------------------------------------------------------------------------
// 13 Program to find Tridiagonal Matrix
// iff arr[i][j] = 0 for |i-j| > 1
// --------------------------------------------------------------------------------

// int main()
// {
//     int arr[4][4] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
//     printf("The matrix is:\n");
//     for (int i = 0; i < 4; i++)
//     {
//         for (int j = 0; j < 4; j++)
//         {
//             printf("%3d ",arr[i][j]);
//         }
//         printf("\n");
//     }
//     for (int i = 0; i < 4; i++)
//     {
//         for (int j = 0; j < 4; j++)
//         {
//             if (i==j || i-j==1 || i-j==-1)
//                 continue;
//             else
//                 arr[i][j]=0;
//         }
//     }
//     printf("Tridiagonal matrix is: \n");
//     for (int i = 0; i < 4; i++)
//     {
//         for (int j = 0; j < 4; j++)
//         {
//             printf("%3d ",arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// --------------------------------------------------------------------------------
// 14 program of stack using array
// --------------------------------------------------------------------------------

// int top = -1;
// int max_size = 10;
// int stack[max_size], ch, n;
// int push(int n)
// {
//     if (top >= max_size-1)
//         printf("Stack overflow !!!");
//     else
//     {
//         top = top+1;
//         stack[top]=n;
//     }
//     return 0;
// }
// int pop()
// {
//     if (top == -1)
//         printf("Stack underflow !!!");
//     else
//     {
//         // stack[top] = NULL;
//         top = top-1;
//     }
//     return 0;
// }
// void display()
// {
//     for (int i = top; i >= 0; i--)
//     {
//         printf("%d\n",stack[i]);
//     }
// }
// int main()
// {
//     while (1)
//     {
//         printf("[ 1 ] Push\n[ 2 ] Pop\n[ 3 ] Display\n[ 0 ] Exit\n");
//         printf("Choose operation: ");
//         scanf("%d", &ch);
//         switch (ch)
//         {
//         case 1:
//             printf("Enter element to push on stack: ");
//             scanf("%d", &n);
//             push(n);
//             break;
//         case 2:
//             pop();
//             break;
//         case 3:
//             display();
//             break;
//         case 0:
//             printf("Exiting....");
//             exit(1);
//         default:
//             printf("Please choose correct operation...");
//         }
//     }
//     return 0;
// }
// ----------------------------------------------------------------------------------------------
// 15 Program to evaluate postfix expression
// ----------------------------------------------------------------------------------------------

// #define exp_size 33
// #define stack_size 33
// int top = -1;
// int stack[stack_size];
// void evaluate(char exp[exp_size]);
// int push(int num);
// int pop();

// int main()
// {
//     char exp[exp_size];
//     printf("Enter the expression in postflix [add ')' in the end of expression] : ");
//     for (int i = 0; i < exp_size; i++)
//     {
//         scanf("%c", &exp[i]);
//         if (exp[i] == ')')
//         {
//             break;
//         }
//     }

//     evaluate(exp);
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
//         }
//     }
//     printf("Result of given expression is: %d",pop());
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
//     //we have returned the final above already, if execution is not coming to this printf
//     // printf("%d",final); //WE CANNOT DO THIS here, we have to return the final
// }

// -------------------------------------------------------------------------------
// 16 Program to convert infix to postfix using stack
// -------------------------------------------------------------------------------

// char stack[100];
// int top = -1;

// void push(char x)
// {
//     stack[++top] = x;
// }

// char pop()
// {
//     if(top == -1)
//         return -1;
//     else
//         return stack[top--];
// }

// int priority(char x)
// {
//     if(x == '(')
//         return 0;
//     if(x == '+' || x == '-')
//         return 1;
//     if(x == '*' || x == '/')
//         return 2;
//     return 0;
// }

// int main()
// {
//     char exp[33];
//     char *e, x;
//     printf("Enter the expression : ");
//     scanf("%33s",exp);
//     printf("\n");
//     e = exp;
//     while(*e != '\0')
//     {
//         if(isalnum(*e))
//             printf("%c ",*e);
//         else if(*e == '(')
//             push(*e);
//         else if(*e == ')')
//         {
//             while((x = pop()) != '(')
//                 printf("%c ", x);
//         }
//         else
//         {
//             while(priority(stack[top]) >= priority(*e))
//                 printf("%c ",pop());
//             push(*e);
//         }
//         e++;
//     }

//     while(top != -1)
//     {
//         printf("%c ",pop());
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 17 Program to Implement a Queue using an Array
// --------------------------------------------------------------------------------

// #define size 33
// int rear = -1, front = -1;
// void enqueue();
// void dequeue();
// void display();
// int queue[size];
// int main()
// {
//     int ch;
//     while (1)
//     {
//         printf(" [ 1 ] Enqueue\t");
//         printf(" [ 2 ] Dequeue\t");
//         printf(" [ 3 ] Display\t");
//         printf(" [ 0 ] Exit\n");
//         printf("\n Choose operation: ");
//         scanf("%d", &ch);
//         switch (ch)
//         {
//         case 1:
//             enqueue();
//             break;

//         case 2:
//             dequeue();
//             break;

//         case 3:
//             display();
//             break;

//         case 0:
//             printf("Exiting...");
//             exit(1);
//         default:
//             printf("Please choose correct operation !!!");
//             break;
//         }
//     }
//     return 0;
// }
// void enqueue()
// {
//     int value;
//     if (rear == size - 1)
//     {
//         printf("Queue is FULL !!\n");
//     }
//     else
//     {
//         if (front == -1)
//         {
//             front = 0;
//         }
//         printf("Enter the element to insert: ");
//         scanf("%d", &value);
//         rear++;
//         queue[rear] = value;
//     }
// }
// void dequeue()
// {
//     if (front == -1 || front > rear)
//     {
//         printf("Queue is already Empyt !!\n");
//     }
//     else
//     {
//         printf("Deleted element: %d", queue[front]);
//         front++;
//     }
// }
// void display()
// {
//     if (front == -1 || front > rear)
//     {
//         printf("Queue is empty\n");
//     }
//     else
//     {
//         printf("Queue: ");
//         for (int i = front; i <= rear; i++)
//         {
//             printf("%d ", queue[i]);
//         }
//         printf("\n");
//     }
// }

// --------------------------------------------------------------------------------
// 18 program of circular queue using array
// --------------------------------------------------------------------------------

// #define size 33
// int rear = -1, front = -1;
// void enqueue();
// void dequeue();
// void display();
// int queue[size];
// int main()
// {
//     int ch;
//     while (1)
//     {
//         printf(" [ 1 ] Enqueue\t");
//         printf(" [ 2 ] Dequeue\t");
//         printf(" [ 3 ] Display\t");
//         printf(" [ 0 ] Exit");
//         printf("\n Choose operation: ");
//         scanf("%d", &ch);
//         switch (ch)
//         {
//         case 1:
//             enqueue();
//             break;

//         case 2:
//             dequeue();
//             break;

//         case 3:
//             display();
//             break;

//         case 0:
//             printf("Exiting...");
//             exit(1);
//         default:
//             printf("Please choose correct operation !!!");
//             break;
//         }
//     }
//     return 0;
// }
// void enqueue()
// {
//     int value;
//     if ((rear == size - 1 && front == 0) || (front == rear + 1))
//     {
//         printf("Queue is FULL !!\n");
//     }
//     if (front == -1)
//     {
//         front = 0;
//         rear = 0;
//     }
//     else
//     {
//         if (rear == size - 1)
//         {
//             rear = 0;
//         }
//         else
//         {
//             rear++;
//         }
//         printf("Enter the element to insert: ");
//         scanf("%d", &value);
//         queue[rear] = value;
//     }
// }
// void dequeue()
// {
//     if (front == -1 || front > rear)
//     {
//         printf("Queue is already Empyt !!\n");
//     }
//     else
//     {
//         printf("Deleted element: %d\n", queue[front]);
//     }
//     if (front == rear)
//     {
//         front = -1;
//         rear = -1;
//     }
//     else
//     {
//         if (front == size - 1)
//         {
//             front = 0;
//         }
//         else
//         {
//             front++;
//         }
//     }
// }
// void display()
// {
//     if (front == -1)
//     {
//         printf("Queue is empty\n");
//     }
//     else if (rear >= front)
//     {
//         printf("Queue: ");
//         for (int i = front; i <= rear; i++)
//         {
//             printf("%d ", queue[i]);
//         }
//         printf("\n");
//     }
//     else
//     {
//         printf("Queue: ");
//         for (int i = front; i < size; i++)
//         {
//             printf("%d ", queue[i]);
//         }
//         for (int i = 0; i <= rear; i++)
//         {
//             printf("%d ", queue[i]);
//         }
//         printf("\n");
//     }
// }

// --------------------------------------------------------------------------------
// 19 program of deque using array(circular array)
// A double ended queue is an abstract datatype that generalizes a queue, for which elements can be added or removed either from the front or rear. It is often called a head-tail linked-list.
// --------------------------------------------------------------------------------

// #define size 33
// int deque[size];
// int f=-1, r=-1;
// void insert_front();
// void insert_rear();
// void delete_front();
// void delete_rear();
// void display();
// void getfront();
// void getrear();

// int main()
// {
//     insert_front(20);
//     insert_front(10);
//     display();  //Calling the display function to retrieve the values of deque
//     insert_rear(30);
//     insert_rear(50);
//     insert_rear(80);
//     display();  // Calling the display function to retrieve the values of deque
//     getfront();  // Retrieve the value at front-end
//     getrear();  // Retrieve the value at rear-end
//     delete_front();
//     delete_rear();
//     display(); // calling display function to retrieve values after deletion
//     return 0;
// }
// void insert_front(int x)
// {
//     if((f==0 && r==size-1) || (f==r+1))
//     {
//         printf("Overflow");
//     }
//     else if((f==-1) && (r==-1))
//     {
//         f=r=0;
//         deque[f]=x;
//     }
//     else if(f==0)
//     {
//         f=size-1;
//         deque[f]=x;
//     }
//     else
//     {
//         f=f-1;
//         deque[f]=x;
//     }
// }
// void insert_rear(int x)
// {
//     if((f==0 && r==size-1) || (f==r+1))
//     {
//         printf("Overflow");
//     }
//     else if((f==-1) && (r==-1))
//     {
//         r=0;
//         deque[r]=x;
//     }
//     else if(r==size-1)
//     {
//         r=0;
//         deque[r]=x;
//     }
//     else
//     {
//         r++;
//         deque[r]=x;
//     }

// }
// void display()
// {
//     int i=f;
//     printf("\nElements in a deque are: ");

//     while(i!=r)
//     {
//         printf("%d ",deque[i]);
//         i=(i+1)%size;
//     }
//      printf("%d",deque[r]);
// }
// void getfront()
// {
//     if((f==-1) && (r==-1))
//     {
//         printf("Deque is empty");
//     }
//     else
//     {
//         printf("\nThe value of the element at front is: %d", deque[f]);
//     }

// }
// void getrear()
// {
//     if((f==-1) && (r==-1))
//     {
//         printf("Deque is empty");
//     }
//     else
//     {
//         printf("\nThe value of the element at rear is %d", deque[r]);
//     }

// }
// void delete_front()
// {
//     if((f==-1) && (r==-1))
//     {
//         printf("Deque is empty");
//     }
//     else if(f==r)
//     {
//         printf("\nThe deleted element is %d", deque[f]);
//         f=-1;
//         r=-1;

//     }
//      else if(f==(size-1))
//      {
//          printf("\nThe deleted element is %d", deque[f]);
//          f=0;
//      }
//      else
//      {
//           printf("\nThe deleted element is %d", deque[f]);
//           f=f+1;
//      }
// }
// void delete_rear()
// {
//     if((f==-1) && (r==-1))
//     {
//         printf("Deque is empty");
//     }
//     else if(f==r)
//     {
//         printf("\nThe deleted element is %d", deque[r]);
//         f=-1;
//         r=-1;

//     }
//      else if(r==0)
//      {
//          printf("\nThe deleted element is %d", deque[r]);
//          r=size-1;
//      }
//      else
//      {
//           printf("\nThe deleted element is %d", deque[r]);
//           r=r-1;
//      }
// }

// --------------------------------------------------------------------------------
// 20 program of priority queue using array
// --------------------------------------------------------------------------------

// #include <stdio.h>
// #define MAX 10

// int queue[MAX];
// int priorities[MAX];
// int front = -1, rear = -1;

// void enqueue(int value, int priority) {
//   if (rear == MAX - 1) {
//     printf("Queue is full\n");
//   } else {
//     if (front == -1) {
//       front = 0;
//     }
//     rear++;
//     int i;
//     for (i = rear; i > front && priorities[i - 1] > priority; i--) {
//       queue[i] = queue[i - 1];
//       priorities[i] = priorities[i - 1];
//     }
//     queue[i] = value;
//     priorities[i] = priority;
//   }
// }

// void dequeue() {
//   if (front == -1 || front > rear) {
//     printf("Queue is empty\n");
//   } else {
//     printf("Dequeued value: %d\n", queue[front]);
//     front++;
//   }
// }

// void printQueue() {
//   if (front == -1 || front > rear) {
//     printf("Queue is empty\n");
//   } else {
//     printf("Queue: ");
//     for (int i = front; i <= rear; i++) {
//       printf("%d (priority %d) ", queue[i], priorities[i]);
//     }
//     printf("\n");
//   }
// }

// int main() {
//   enqueue(1, 2);
//   enqueue(2, 3);
//   enqueue(3, 1);
//   enqueue(4, 4);
//   printf("\n");
//   printQueue();
//   printf("\n");
//   dequeue();
//   dequeue();
//   printf("\n");
//   printQueue();
//   return 0;
// }

// --------------------------------------------------------------------------------
// 21 Program of Linked List
// --------------------------------------------------------------------------------

// struct Node {
//   int data;
//   struct Node *next;
// };

// struct Node *head = NULL;

// void append(int data) {
//   struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
//   new_node->data = data;
//   new_node->next = NULL;
//   if (head == NULL) {
//     head = new_node;
//   } else {
//     struct Node *current = head;
//     while (current->next != NULL) {
//       current = current->next;
//     }
//     current->next = new_node;
//   }
// }

// void traverse() {
//   struct Node *current = head;
//   while (current->next != NULL) {
//     printf("%d->", current->data);
//     current = current->next;
//   }
//   printf("%d",current->data);
//   printf("\n");
// }

// int main() {
//   append(1);
//   append(2);
//   append(3);
//   append(4);
//   traverse();
//   return 0;
// }

// --------------------------------------------------------------------------------
// 22 Program of searching of element in Linked List
// --------------------------------------------------------------------------------

// struct Node {
//   int data;
//   struct Node *next;
// };

// struct Node *head = NULL;

// void append(int data) {
//   struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
//   new_node->data = data;
//   new_node->next = NULL;
//   if (head == NULL) {
//     head = new_node;
//   } else {
//     struct Node *current = head;
//     while (current->next != NULL) {
//       current = current->next;
//     }
//     current->next = new_node;
//   }
// }

// void traverse() {
//   struct Node *current = head;
//   while (current->next != NULL) {
//     printf("%d->", current->data);
//     current = current->next;
//   }
//   printf("%d",current->data);
//   printf("\n");

// }

// void search(int num)
// {
//     struct Node *temp;
//     temp = head;
//     while (temp != NULL)
//     {
//         if (temp->data == num)
//         {
//             printf("\nElement %d found", num);
//             return;
//         }
//         temp = temp->next;
//     }

// }

// int main()
// {
//   append(1);
//   append(2);
//   append(3);
//   append(4);
//   append(10);
//   append(17);
//   append(100);
//   append(120);
//   traverse();
//   search(17);
//   search(200);
//   return 0;
// }

// --------------------------------------------------------------------------------
// 23 Program of reversing of Linked List
// --------------------------------------------------------------------------------

// struct Node {
//   int data;
//   struct Node *next;
// };

// struct Node *head = NULL;

// void append(int data) {
//   struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
//   new_node->data = data;
//   new_node->next = NULL;
//   if (head == NULL) {
//     head = new_node;
//   } else {
//     struct Node *temp = head;
//     while (temp->next != NULL) {
//       temp = temp->next;
//     }
//     temp->next = new_node;
//   }
// }

// void traverse()
// {
//   struct Node *temp = head;
//   while (temp->next != NULL) {
//     printf("%d->", temp->data);
//     temp = temp->next;
//   }
//   printf("%d",temp->data);
//   printf("\n");
// }
// void reverse()
// {
//   struct Node *temp = head;
//   struct Node *prev = NULL;
//   struct Node *next = NULL;
//   while (temp != NULL)
//   {
//     next = temp->next;
//     temp->next = prev;
//     prev = temp;
//     temp = next;
//   }
//   head = prev;
// }

// int main()
// {
//   append(1);
//   append(2);
//   append(3);
//   append(4);
//   append(10);
//   append(17);
//   append(100);
//   append(120);
//   traverse();
//   reverse();
//   traverse();
//   return 0;
// }

// --------------------------------------------------------------------------------
// 24 program to concatenate two Linked List
// --------------------------------------------------------------------------------

// #include <stdio.h>
// #include<stdlib.h>
// struct node
// {
//     int data;
//     struct node *link;
// };

// struct node *first=NULL,*second=NULL;

// void display(struct node *);
// void addatbegfirstlist(int);
// void addatbegsecondlist(int);
// void concat();
// int main()
// {

// addatbegfirstlist(99);
// addatbegfirstlist(88);
// addatbegfirstlist(18);
// addatbegfirstlist(28);
// addatbegfirstlist(38);
// printf("LinkedList 1: ");
// display(first);
// addatbegsecondlist(100);
// addatbegsecondlist(200);
// addatbegsecondlist(300);
// addatbegsecondlist(400);
// addatbegsecondlist(500);
// printf("LinkedList 2: ");
// display(second);

// printf("=== After Concatenation ===\nLinkedList: ");
// concat();
// display(first);

//    return 0;
// }

// void addatbegfirstlist(int num)
// {
//     struct node *temp;
//     temp=(struct node *)malloc(sizeof(struct node));
//     temp->data=num;
//     temp->link=first;
//     first=temp;
// }

// void addatbegsecondlist(int num)
// {
//     struct node *temp;
//     temp=(struct node *)malloc(sizeof(struct node));
//     temp->data=num;
//     temp->link=second;
//     second=temp;
// }
// void display(struct node *q)
// {
//     while(q->link!=NULL)
//     {
//         printf("%d->",q->data);
//         q=q->link;
//     }
//     printf("%d",q->data);
//     printf("\n");
// }

// void concat()
//  {
//      struct node *temp;
//      if(first==NULL)
//        {
//            first=second;
//        }
//        else
//          {
//              if(second!=NULL)
//               {
//                   temp=first;
//                   while(temp->link!=NULL)
//                    {
//                      temp=temp->link;
//                    }
//                    temp->link=second;
//               }
//          }
//  }

// --------------------------------------------------------------------------------
// 25 Program to delete at different position in Linked List
// --------------------------------------------------------------------------------

// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void linkedListTraversal(struct Node *ptr)
// {
//     while (ptr->next!= NULL)
//     {
//         printf("%d->", ptr->data);
//         ptr = ptr->next;
//     }
//     printf("%d",ptr->data);
//     printf("\n\n");
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

// --------------------------------------------------------------------------------
// 26 program of doubly Linked List
// --------------------------------------------------------------------------------

// struct Node
// {
//         int data;
//         struct Node *next;
//         struct Node *prev;
// };

// void traverse(struct Node *head)
// {
//         struct Node *p = head;
//         do
//         {
//                 printf("%d->",p->data);
//                 p = p->next;
//         }while (p->next != NULL);
//         printf("%d ",p->data);
// }

// int main()
// {
//         struct Node *head;
//         struct Node *second;
//         struct Node *third;
//         struct Node *fourth;
//         struct Node *fifth;

//         head = (struct Node *)malloc(sizeof(struct Node));
//         second = (struct Node *)malloc(sizeof(struct Node));
//         third = (struct Node *)malloc(sizeof(struct Node));
//         fourth = (struct Node *)malloc(sizeof(struct Node));
//         fifth = (struct Node *)malloc(sizeof(struct Node));

//         head->prev = NULL;
//         head->data = 4;
//         head->next = second;
//         second->prev = head;
//         second->data = 3;
//         second->next = third;
//         third->prev = second;
//         third->data = 6;
//         third->next = fourth;
//         fourth->prev = third;
//         fourth->data = 2;
//         fourth->next = fifth;
//         fifth->prev = fourth;
//         fifth->data = 7;
//         fifth->next = NULL;

//         printf("Doubly Linked list: ");
//         traverse(head);
//         return 0;
// }

// --------------------------------------------------------------------------------
// 27 program of circular linked list
// --------------------------------------------------------------------------------

// struct Node
// {
//     int data;
//     struct Node *next;
// };

// void traversing(struct Node *head){
//     struct Node *ptr = head;
//     do{
//         printf("%d->", ptr->data);
//         ptr = ptr->next;
//     }while(ptr!= head);
//     // printf("%d->", ptr->data);

// }
// struct Node* insert(struct Node* head, int data)
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

//     printf("Circular LinkedList: ");
//     traversing(head);
//     traversing(head);
//     return 0;
// }

// --------------------------------------------------------------------------------
// 28 program of Stack using Linked List
// --------------------------------------------------------------------------------

// struct node
// {
//     int data;
//     struct node *link;
// };

// struct node *p = NULL;

// void display(struct node *);
// void push(int);
// void pop();
// int main()
// {
//     printf("Push Operation: \n");
//     push(14);
//     push(30);
//     push(25);
//     push(42);
//     push(17);
//     push(19);
//     display(p);
//     printf("POP operation: \n");
//     pop();
//     display(p);
//     printf("POP operation: \n");
//     pop();

//     display(p);
//     return 0;
// }

// void display(struct node *q)
// {
//     while (q != NULL)
//     {
//         printf("%d\n", q->data);
//         q = q->link;
//     }
//     printf("\n");
// }

// void push(int num) /* add at beginning */
// {
//     struct node *temp;
//     temp = (struct node *)malloc(sizeof(struct node));
//     temp->data = num;
//     temp->link = p;
//     p = temp;
// }

// void pop() /* delete at beginning  because  adding  at beginning */
// {
//     struct node *temp;
//     int n;
//     if (p == NULL)
//     {
//         printf("stack is empty");
//         return;
//     }
//     temp = p;

//     n = temp->data;
//     p = p->link;
//     free(temp);
// }

// --------------------------------------------------------------------------------
// 29 program of queue using Linked List
// --------------------------------------------------------------------------------

// struct node
// {
//     int data;
//     struct node *link;
// };

// struct node *front = NULL, *rear = NULL, *f;

// void enqueue(int);
// void display();
// void dequeue();
// int main()
// {
//     printf("Enqueue operation: \n");
//     enqueue(14);
//     display();
//     printf("Enqueue operation: \n");
//     enqueue(30);
//     display();
//     printf("Enqueue operation: \n");
//     enqueue(25);
//     display();
//     printf("Enqueue operation: \n");
//     enqueue(42);
//     display();
//     printf("Enqueue operation: \n");
//     enqueue(17);
//     display();
//     printf("Dequeue operation: \n");
//     dequeue();
//     display();
//     printf("Dequeue operation: \n");
//     dequeue();
//     display();

//     return 0;
// }

// void enqueue(int num)
// {
//     struct node *temp;
//     if (front == NULL || rear == NULL) /* queue is empty */
//     {
//         temp = (struct node *)malloc(sizeof(struct node));
//         rear = temp;
//         rear->data = num;
//         rear->link = NULL;
//         front = rear;
//     }
//     else
//     {
//         temp = (struct node *)malloc(sizeof(struct node));
//         temp->data = num;
//         temp->link = NULL;
//         rear->link = temp;
//         rear = temp;
//     }
// }
// void dequeue()
// {
//     f = front;
//     if (f == NULL)
//     {
//         printf("\n queue empty queue");
//         return;
//     }
//     else if (f->link != NULL) /* queue has more than one elent */
//     {
//         f = f->link;
//         free(front);
//         front = f;
//     }
//     else /* queue has only one element */
//     {
//         free(front);
//         front = NULL;
//         rear = NULL;
//     }
// }

// void display()
// {
//     f = front;
//     if ((f == NULL) && (rear == NULL)) /* queue is empty */
//     {
//         printf("Queue is empty");
//         return;
//     }
//     if (f == rear) /* queue have only one element */
//     {
//         printf("%d ", f->data);
//         printf("\n");
//     }
//     else
//     {
//         while (f != rear) /* before rear */
//         {
//             printf("%d ", f->data);
//             f = f->link;
//         }
//         printf("%d ", f->data); /* at rear */
//         printf("\n");
//     }
// }

// --------------------------------------------------------------------------------
// 30 Program of Binary tree using Linked List
// --------------------------------------------------------------------------------

// struct node {
//   int data;
//   struct node *left;
//   struct node *right;
// };

// struct node* createNode(int data) {
//   struct node* newNode = (struct node*) malloc(sizeof(struct node));
//   newNode->data = data;
//   newNode->left = NULL;
//   newNode->right = NULL;
//   return newNode;
// }

// struct node* insert(struct node* root, int data) {
//   if (root == NULL) {
//     root = createNode(data);
//   } else if (data <= root->data) {
//     root->left = insert(root->left, data);
//   } else {
//     root->right = insert(root->right, data);
//   }
//   return root;
// }

// void inorder(struct node* root) {
//   if (root == NULL)
//     return;
//   inorder(root->left);
//   printf("%d ", root->data);
//   inorder(root->right);
// }

// int main() {
//   struct node* root = NULL;
//   root = insert(root, 5);
//   root = insert(root, 3);
//   root = insert(root, 7);
//   root = insert(root, 2);
//   root = insert(root, 4);
//   root = insert(root, 6);
//   root = insert(root, 8);
//   inorder(root);
//   return 0;
// }

// --------------------------------------------------------------------------------
// 31 program of binary search tree using Linked List
// --------------------------------------------------------------------------------

// struct node
// {
//     int data;
//     struct node *left;
//     struct node *right;
// };

// // Create a new node with the given data
// struct node *newNode(int data)
// {
//     struct node *node = (struct node *)malloc(sizeof(struct node));
//     node->data = data;
//     node->left = NULL;
//     node->right = NULL;
//     return node;
// }

// // Insert a new node with the given data into the binary search tree
// struct node *insert(struct node *node, int data)
// {
//     // If the tree is empty, return a new node
//     if (node == NULL)
//     {
//         return newNode(data);
//     }

//     // Otherwise, recur down the tree
//     if (data < node->data)
//     {
//         node->left = insert(node->left, data);
//     }
//     else if (data > node->data)
//     {
//         node->right = insert(node->right, data);
//     }

//     // Return the unchanged node pointer
//     return node;
// }

// // Search for a node with the given data in the binary search tree
// struct node *search(struct node *root, int data)
// {
//     // Return NULL if the tree is empty
//     if (root == NULL)
//     {
//         return NULL;
//     }

//     // If the data is less than the root's data, search the left subtree
//     if (data < root->data)
//     {
//         return search(root->left, data);
//     }

//     // If the data is greater than the root's data, search the right subtree
//     if (data > root->data)
//     {
//         return search(root->right, data);
//     }

//     // If the data is equal to the root's data, return the root
//     return root;
// }
// void inorder(struct node* root) {
//   if (root == NULL)
//     return;
//   inorder(root->left);
//   printf("%d ", root->data);
//   inorder(root->right);
// }

// int main()
// {
//     // Create an empty binary search tree
//     struct node *root = NULL;

//     // Insert some nodes into the tree
//     root = insert(root, 50);
//     root = insert(root, 30);
//     root = insert(root, 20);
//     root = insert(root, 40);
//     root = insert(root, 70);
//     root = insert(root, 60);
//     root = insert(root, 80);
//     inorder(root);
//     printf("\n");
//     // Search for a node with the given data
//     int data;
//     printf("Enter data to search: ");
//     scanf("%d",&data);
//     struct node *result = search(root, data);
//     if (result != NULL)
//     {
//         printf("Found node with data %d\n", result->data);
//     }
//     else
//     {
//         printf("Could not find node with data %d\n", data);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 32 Program of Insertion sort
// --------------------------------------------------------------------------------

// // Function to sort an array using insertion sort
// void insertionSort(int arr[], int n) {
//   int i, key, j;
//   for (i = 1; i < n; i++) {
//     key = arr[i];
//     j = i - 1;

//     // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
//     while (j >= 0 && arr[j] > key) {
//       arr[j + 1] = arr[j];
//       j = j - 1;
//     }
//     arr[j + 1] = key;
//   }
// }

// // Function to print an array
// void printArray(int arr[], int n) {
//   int i;
//   for (i = 0; i < n; i++) {
//     printf("%d ", arr[i]);
//   }
//   printf("\n");
// }

// int main()
// {
//     int arr[] = {12, 17, 13, 50, 63};
//     int n = sizeof(arr) / sizeof(arr[0]);

//     printArray(arr, n);
//     insertionSort(arr, n);
//     printArray(arr, n);

//     return 0;
// }

// --------------------------------------------------------------------------------
// 33 Program of Selection sort
// --------------------------------------------------------------------------------

// void swap(int *x, int *y)
// {
//     int temp;
//     temp = *x;
//     *x = *y;
//     *y = temp;
// }

// void selectionSort(int arr[], int n)
// {
//     for (int i = 0; i < n-1; i++)
//     {
//         for (int j = i+1; j < n; j++)
//         {
//             swap(&arr[i],&arr[j]);
//         }
//     }
// }

// void printArray(int arr[], int n)
// {
//     int i;
//     for (i = 0; i < n; i++)
//     {
//         printf("%d ", arr[i]);
//     }
//     printf("\n");
// }

// int main()
// {
//     int arr[] = {12, 7, 13, 50, 43};
//     int n = sizeof(arr) / sizeof(arr[0]);

//     printArray(arr, n);
//     selectionSort(arr, n);
//     printArray(arr, n);

//     return 0;
// }

// --------------------------------------------------------------------------------
// 34 Program of Linear search
// --------------------------------------------------------------------------------

// int search(int arr[], int n, int x)
// {
//     int i;
//     for (i = 0; i < n; i++)
//     {
//         if (arr[i] == x)
//         {
//             return i;
//         }
//     }
//     return -1;
// }

// int main()
// {
//     int arr[] = {2, 3, 4, 10, 40};
//     int n = sizeof(arr) / sizeof(arr[0]);
//     int x;
//     for (int i = 0; i < n; i++)
//     {
//         printf("|%d",arr[i]);
//     }
//     printf("|");
//     printf("\nEnter the element to search: ");
//     scanf("%d",&x);
//     int result = search(arr, n, x);
//     if (result == -1)
//     {
//         printf("\nElement is not present in the array\n");
//     }
//     else
//     {
//         printf("\nElement is present at index %d\n", result);
//     }
//     return 0;
// }

// --------------------------------------------------------------------------------
// 35 Program of Binary search 
// --------------------------------------------------------------------------------

// int binarySearch(int arr[], int beg, int size, int x)
// {
//     int mid;
//     if (size>=beg)
//     {
//         mid = (beg+(size-1))/2;
//         if (arr[mid] < x)
//             return binarySearch(arr, (mid+1), size, x);
//         else if (arr[mid] > x)
//         {
//             return binarySearch(arr, beg, (mid-1), x);
//         }
//         else
//             return mid;
//     }
//     return -1;
// }

// int main()
// {
//     int arr[] = {2, 3, 4, 10, 40};
//     int size = sizeof(arr) / sizeof(arr[0]);
//     int beg=0,x;
//     for (int i = 0; i < size; i++)
//     {
//         printf("|%d",arr[i]);
//     }
//     printf("|");
//     printf("\nEnter the element to search: ");
//     scanf("%d",&x);

//     int result = binarySearch(arr, beg, size, x);
//     if (result == -1)
//     {
//         printf("\nElement is not present in the array\n");
//     }
//     else
//     {
//         printf("\nElement is present at index %d\n", result);
//     }
//     return 0;
// }

// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>


// struct items{
//     char item[20];
//     int qty;
//     float price;

// };
// struct orders{
//     char customer[50];
//     char date[20];
//     int numOfItems;

//     struct items itm[20];
// };

// void generateBillHeader(char name[50],char date[30]){
//     printf("\n\n");
//     printf("\t\t KANYAWATI_AND_SONS");
//     printf("\n\t\t-------------------");
//     printf("\ndate:%s",date);
//     printf("\nInvoice To: %s",name);
//     printf("\n");
//     printf("--------------------------------------------------------\n");
//     printf("Items");
//     printf("\t\tQty\t\t");
//     printf("Total\t\t");
//     printf("\n-------------------------------------------------------");
//     printf("\n\n");
// }

// void generateBillFfooter(float total){
//     printf("\n");
//     float dis = 0.1*total;
//     float netTotal  = total-dis;
//     float cgst=0.09*netTotal,grandTotal=netTotal + (cgst*2);
//     printf("-----------------------------------------------------\n");
//     printf("Sub Total\t\t\t%.2f",total);
//     printf("\nDiscount @10%s\t\t\t%2.f","%",dis);
//     printf("\n\t\t\t\t------");
//     printf("\nNet Total\t\t\t%.2f",netTotal);
//     printf("\nCGST @9%s\t\t\t%.2f","%",cgst);
//     printf("\nSGST @9%s\t\t\t%.2f","%",cgst);
//     printf("\n---------------------------------------------------------\n");
//     printf("Grand Total\t\t\t%.2f",grandTotal);
//     printf("\n---------------------------------------------------------");
// }

// void generateBillBody(char item[30],int qty, float price){
//     printf("%s\t\t",item);
//     printf("%d\t\t",qty);
//     printf("%.2f\t\t",qty*price);
//     printf("\n");
// }



// int main(){
   
//    system("clear");
//     int opt,n;
//     struct orders ord;
//     struct orders order;
//     FILE* fp;
//     char name[50];
//     char saveBill = 'y',continueflag = 'y';
//     while(continueflag == 'y'){
//     system("clear");
//     int invoiceFound = 0;
//     float Total = 0;
//     printf("\t\t\n===========KANYAWATI_AND_SONS===========\n");
//     printf("\n\nPlease Enter your Prefered Operation\n\n");
//     printf("\n1.Generate Invoice");
//     printf("\n2.Show all Invoices");
//     printf("\n3.Search Invoice");
//     printf("\n4.Exit");

//     printf("\n\nYour choice :\t");
//     scanf("%d",&opt);
//     fgetc(stdin);

//     switch(opt){
//         case 1:
//         system("clear");
//         printf("\nPlease Enter the name of the Customer : \t");
//         fgets(ord.customer,50,stdin);
//         strcpy(ord.date,__DATE__);
//         printf("Please Enter the number of items : \t");
//         scanf("%d",&n);
//         ord.numOfItems = n;
//         for(int i = 0; i < n; i++){
//         fgetc(stdin);
//         printf("\n\n");
//         printf("Please enter the item %d :\t",i+1);
//         fgets(ord.itm[i].item,20,stdin);
//         ord.itm[i].item[strlen(ord.itm[i].item)-1] = 0;

//         printf("Please Enter the Quantity :\t");
//         scanf("%d",&ord.itm[i].qty);
//         printf("Please Enter the Unit Price\t");
//         scanf("%f",&ord.itm[i].price);
//         Total += ord.itm[i].qty * ord.itm[i].price;
//         }

//         generateBillHeader(ord.customer,ord.date);
//         for(int i = 0; i < ord.numOfItems; i++){

//             generateBillBody(ord.itm[i].item,ord.itm[i].qty,ord.itm[i].price);
//         }
//         generateBillFfooter(Total);

//         printf("\n Do you want to save the Invoice [y/n]:\t");
//         scanf("%s",&saveBill);

//         if(saveBill == 'y'){
//             fp = fopen("Restaurant.dat","a+");
//             fwrite(&ord,sizeof(struct orders),1,fp);
//             if(fp != 0){
//                 printf("\nSuccessfully saved");
//             }
//             else
//             printf("Error Saving");
//             fclose(fp);
//         }
//         break;
//         case 2:
//         system("clear");
//         fp = fopen("Restaurant.dat","r");
//         printf("\n\t****Your Previous Invoices****\n");

//         while(fread(&order,sizeof(struct orders),1,fp)){
//             float tot = 0;
//             generateBillHeader(order.customer,order.date);
//             for(int i = 0; i < order.numOfItems;i++){
//                 generateBillBody(order.itm[i].item,order.itm[i].qty,order.itm[i].price);
//                 tot+=order.itm[i].qty*order.itm[i].price;
//             }
//             generateBillFfooter(tot);
//         }
//         fclose(fp);
//         break;
//         case 3:
//         printf("\nenter the name of the Customer:\t");
//        // fgetc(stdin);
//         fgets(name,50,stdin);
//         name[strlen(name)-1] = 0;
//         system("clear");
//         fp = fopen("Restaurant.dat","r");
//         printf("\t****Invoice Of %s****",name);
//         while(fread(&order,sizeof(struct orders),1,fp)){
//             float tot = 0;
//             if(strcmp(order.customer,name)){
//             generateBillHeader(order.customer,order.date);
//             for(int i = 0; i < order.numOfItems;i++){
//                 generateBillBody(order.itm[i].item,order.itm[i].qty,order.itm[i].price);
//                 tot+=order.itm[i].qty*order.itm[i].price;
//             }
//             generateBillFfooter(tot);
//             invoiceFound = 1;
//         }
//         }
//         if(!(invoiceFound)){
//             printf("Sorry the invoice for %s doesnot found\n",name);
//         }
//         fclose(fp);
//         break;
//         case 4 :
//         printf("\n\t\t Bye Bye :)\n\n\n");
//         exit(0);
//         break;

//         default:
//         printf("Sorry Invalid Option");
//         break;
//     }
//     printf("\nDo you want to perform another operation [y/n]:\t");
//     scanf("%s",&continueflag);
//    }
   
//   printf("\n\t\t Bye Bye :)\n\n\n");  
//   printf("\n\n\n");
// }

// ======================================================================


