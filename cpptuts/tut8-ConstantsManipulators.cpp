#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
    // int a = 33;
    // cout << "the value of a is: " <<a<<endl;
    // a = 45; //a's value will be changed
    // cout << "the value of a is: " <<a<<endl;

    //  if we do not want this to happen, we can use Constants
    //  const int a = 4;
    //  cout << "the value of a is: " <<a<<endl;
    //  a = 45; //will give error, a is now become read only variable
    //  cout << "the value of a is: " <<a<<endl;

    // *********************************Manipulators*********************************
    // these helps in formatting of the data which you want to display (just like print(f"aaa") in python)
    // endl, setw, seth are some examples

    // int a = 1, b = 50, c = 1234;
    // cout << "The value of a without setw is: " << a << endl;
    // cout << "The value of b without setw is: " << b << endl;
    // cout << "The value of c without setw is: " << c << endl;
    // // setw(4) means take width of 4 chars and it comes with iomanip
    // cout << "The value of a with setw is: " << setw(4) << a << endl;
    // cout << "The value of b with setw is: " << setw(4) << b << endl;
    // cout << "The value of c with setw is: " << setw(4) << c << endl;
    /* OUTPUT:
    The value of a without setw is: 1
    The value of b without setw is: 50
    The value of c without setw is: 1234
    The value of a with setw is:    1
    The value of b with setw is:   50
    The value of c with setw is: 1234
     */
    
    return 0;
}
