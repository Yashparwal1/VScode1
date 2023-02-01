#include<iostream>
using namespace std;
/* 
In C++, we can create short functions that are not actually called, rather their code is expanded in line
at the point of each invocation. This process is similar to using a function-like macro. To cause a
function to be expanded in line rather than called, precede its definition with the inline keyword.
 * A function which is expanded in a line when it is called is called inline function.
 * It executes faster than other member function.
 * It can be recursive.
 * Its body does not contain if else, switch, loop, goto statement.
 * The inline keyword is preceded by function definition.

WHY it is USED ????
Whenever a function is called, control jumps to definition part of the function. During this jumping of
control, a significant amount of time is required. For functions having short definition if it is called
several time, huge amount of time will be lost. Therefore we declare such function as inline so that
when the function is called, rather than jumping to the definition of function, function definition is
expanded in a line wherever it is called.
 
*/
inline int product(int a, int b){
    // Not recommended to use below lines with inline functions
    // static int c=0; // This executes only once
    // c = c + 1; // Next time this function is run, the value of c will be retained
    return a*b;
}

float moneyReceived(int currentMoney, float factor=1.04){ // default value to factor [can be overwritten]
    return currentMoney * factor;
}

// int strlen(const char *p){

// }

int main(){
    int a, b;
    // cout<<"Enter the value of a and b"<<endl;
    // cin>>a>>b;
    // cout<<"The product of a and b is "<<product(a,b)<<endl;
    int money = 100000;
    cout<<"If you have Rs."<<money<<" in your bank account, you will recive Rs."<<moneyReceived(money)<< " after 1 year"<<endl;
    cout<<"For VIP: If you have Rs."<<money<<" in your bank account, you will recive Rs."<<moneyReceived(money, 1.1)<< " after 1 year";
    return 0;
}
