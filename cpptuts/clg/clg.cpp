#include <iostream>
using namespace std;

// enum year {jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dece};
int main()
{
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

    // ------------------------------CONTROL STRUCTURE-------------------------------------------

    int n,i=1;
    cout << "Enter a positive no.: " <<endl;
    cin >> n;
    long sum = 0;
    // while (i<=n)
    // {
    //     sum += i++;
    //     // i++;
    // }
    // do
    // {
    //     sum += i;
    //     i++;
    // } while (i<=n);
    cout << "Sum of first "<<n<<" integers is "<<sum<<endl;
    




}   

