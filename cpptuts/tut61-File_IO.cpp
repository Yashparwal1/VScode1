/*
Reading File Operation Output:
We learnt reading from a file using ifstream.

string st;
// Opening files using constructor and reading it
ifstream in("this.txt"); // Read operation
in>>st;

Writing File Operation Output:
We learnt reading from a file using ofstream.

string st = "Harry bhai";
// Opening files using constructor and writing it
ofstream out("this.txt"); // Write operation
out<<st;

 */

#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    // connecting our file with hout object of ofstream
    ofstream hout("tut60-sample.txt");

    // creating a name string variable and assigning it with string entered by the user
    string name;
    cout << "Enter your name: ";
    cin >> name;

    // writing the string to the file
    hout << name + " is my name";

    // disconnecting our file
    hout.close();
    // connecting our file with hin stream
    ifstream hin("tut60-sample.txt");

    // creating a content string variable and filling it with string present there in the text file
    string content;
    hin >> content;
    cout << "The content of the file is: " << content;

    // disconnecting our file
    hin.close();
    return 0;
}
