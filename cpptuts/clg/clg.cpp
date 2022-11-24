#include <iostream>
// #include<graphics>
using namespace std;

// enum year {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dece};
// int main()
// {
//     int y;
// int n = 2,i;
// int a = 10;
// float b = 10.5555555;
// char c = 'a';
// double d = 10.5555555555555555;
// cout << a <<endl<< b <<endl;

// for(i = 1; i<=10; i++)
// {
//     cout <<n<<" x "<<i<<" = "<<2*i<<endl;
// }

// for (y = jan; y <= dece; y++)
// {
//     cout << y << <<endl;

// }
// for (y = jan; y <= dece; y++)
// {
//     cout << y <<endl;
// }

// float c = 102.7;
// float a = 15.5;
// double t = c*a;
// cout <<t<<endl;
/*
First var. c of datatype int is converted into type float and stored in a temp. var. before being multiplied by var. a of type float. Also the multiplication c*a which comes in type float is then converted into double.
 */
// int a = 200, b = 400;
// float c;
// c = (float)b/a;
// cout << c <<endl;

//     int n;
//     cout << "Enter a day number: "<<endl;
//     cin >> n;
//     switch (n)
//     {
//     case 1:
//         cout << "Monday" <<endl;
//         break;
//     case 2:
//         cout << "Tuesday" <<endl;
//         break;
//     case 3:
//         cout << "Wednesday" <<endl;
//         break;
//     case 4:
//         cout << "Thrusday" <<endl;
//         break;
//     case 5:
//         cout << "Friday" <<endl;
//         break;
//     case 6:
//         cout << "Saturday" <<endl;
//         break;
//     case 7:
//         cout << "Sunday" <<endl;
//         break;

//     default:
//         cout << "Please enter correct number between 1 to 7" <<endl;
//         break;
//     }

// -------------------- Program to print table from 2 to 10 ----------------------
//     int n=2;
//     while (n<=10)
//     {
// cout << "==> Table of "<<n<< ":" <<endl;
// for (int i = 1; i <= 10; i++)
// {
//     cout << n<<"x"<<i<<"="<<n*i<<endl;
// }
// n++;
//     }

// }

/* int main()
 {
     int n;
     int i=1;
     // for (i = 1; i <= 10; i++)
     // {
     //     for (n = 2; n <= 10; n++)
     //     {
     //         cout << n<<"x"<<i<<"="<<n*i<<"\t";
     //     }
     //     cout << "" <<endl;
     // }
     while (i<=10)
     {
         // for (n = 2; n <= 10 ; n++)
         // {
         //     cout << n<<"x"<<i<<"="<<n*i<<"\t";
         // }
         n = 2;
         while (n<=10)
         {
             cout << n<<"x"<<i<<"="<<n*i<<"\t";
             n++;
         }

         i++;
         cout << "" <<endl;
     }

 } */

// ==============================================================================================

// class Sample
// {
//     private:
//         int a,b;
//     public:
//         void setvalue(){
//             a = 10;
//             b = 20;
//         }
//     friend float mean(Sample s);
// };
// float mean(Sample s)
// {
//     return float ((s.a+s.b)/2.0);
// }
// int main()
// {
//     Sample obj;
//     obj.setvalue();
//     cout << mean(obj) <<endl;
// }

// ==============================================================================================

// class Test{
//     public:
//         int max(int x, int y){
//             return x+y;
//         }
//         int max(int x, int y, int z){
//             return x+y+z;
//         }
// };

// int main()
// {
//     class Test obj;
//     cout << obj.max(99,77) <<endl << obj.max(55,66,77);
// }

// ========================================================================

// class parent
// {
//     public:
//         int a;
//         void getdata()
//         {
//             cout << "enter the number:";
//             cin >> a;
//         }
// };
// class child : public parent
// {
//     public:
//         int b;
//         void readdata()
//         {
//             cout << "Enter the number";
//             cin >> b;
//         }
//         void sum()
//         {
//             cout << "sum=" << (a + b);
//         }
// };
// int main()
// {
//     child cl;
//     cl.getdata();
//     cl.readdata();
//     cl.sum();
//     return 0;
// }

// =========================================================================
// class Complex
// {
//     private:
//         int a;
//         int b;
//     public:
//         void SetData(int x, int y) 
//         {
//             a = x;
//             b = y;
//         }
//         void Display()
//         {
//             cout << "c3(x,y) = " << a<<","<<b <<endl;
//         }
//         // Complex add(Complex c2)
//         Complex operator+(Complex c2)
//         {
//             Complex c;
//             c.a = a + c2.a;
//             c.b = b + c2.b;
//             return(c);
//         }
// };
// int main()
// {
//     Complex c1,c2,c3;
//     c1.SetData(1,2);
//     c2.SetData(3,4);
//     // c3 = c1.add(c2); //calling add() through c1 with parameter as c2
//     c3 = c1+c2; //operator overloading
//     c3.Display();
//     return 0;
// }
// int main()
// {
//     char name[10], f_name[10];
//     gotoxy(10,10);
//     cout <<"Employee's Info.";
//     return 0;
// }
// ===================================== POINTERS ==========================================
/* 
DECLARATION OF POINTERS IN CPP

* Pointer vars like all other vars must be declared before they may be used in cpp program.
* When a pointer var is declared, the var name must be preceded by an asterisk sign (*).
* This identifies that the var is a pointer.

data_type *var_name;
here var_name is the name of pointer variable and data_type is datatype of the pointer object.

*/

// int main()
// {
//     int *p;
//     int x = 20;
//     // p = &x;
//     *p = x;
//     cout << *p <<endl;
//     *p = *p+10;
//     cout << *p <<endl; 
//     return 0;
// }

// class c1{
//     private:
//         int i;
//     public:
//         c1()
//         {
//             i=10;
//         }
//         int get_i(){
//             return i;
//         }
// };
// int main()
// {
//     // c1 obj(88), *p;
//     // p = &obj;
//     c1 *p;
//     cout << p->get_i() <<endl;
//     return 0;
// }

float add(float, float);
int main()
{
    float a,b,s;
    float *p;
    p = &add;
    a = 20.5;
    b = 10.3;
    s = (*p)(a,b); //with pointer
    // s = add(a,b); //without pointer
    cout << "s = " << s <<endl;
}
float add(float x, float y)
{
    float sum;
    sum = x+y;
    return (sum);
}