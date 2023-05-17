/* 
C++ comes with libraires wihich helps us in performing input/output.
In C++ sequence of bytes corresponding to input and output are commonly known as streams.

=> Input Stream: Direction of flow of bytes takes place from input device (eg. keyboard) to the main memory.
=> Output Stream: Direction of flow of bytes takes place from main memory to the output device(eg. display).

*/

#include<iostream>
using namespace std;
// int main()
// {
//     int num1, num2, sum;
// // << -- this is called Extraction operator
// // >> -- this is called Insertion operator
//     cout<<"Enter the value of num1: ";
//     cin>>num1;
//     cout<<"Enter the value of num2: ";
//     cin>>num2;
//     // sum = num1 + num2;
//     // cout<<"The sum of "<<num1<<" and "<<num2<<" is: "<<sum;
//     cout<<"The sum is "<<num1+num2;
//     return 0;
// }

int operation(int x, int y){
    char op;
    while (1)
    {
        cout << "Enter Operation [ + , - , * , / ] : ";
        cin >> op;
        switch (op)
        {
        case '+':
            res = x + y;
            break;
        
        case '-':
            res = x - y;
            break;
        
        case '*':
            res = x * y;
            break;
        
        case '/':
            res = x / y;
            break;
        
        default:
            cout << "Please Enter correct operator..." <<endl;
        }
    }
}
int main(){
    int x = 10, y = 20;
    operation(x,y)
}