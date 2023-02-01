#include<iostream>
using namespace std;
// Destructor neither takes any argument nor return anything
int count = 0;
class Number{
    public:
        Number(){
            count++;
            cout << "CONSTRUCTOR is called for Objject no.: "<<count<<endl;
        }
        ~Number(){ //this '~' sign is called "tild" sign.
            cout << "DESTRUCTOR is called for Objject no.: "<<count<<endl;
            count--;
        }
};
int main(){
    cout<<"We are inside our main function"<<endl;
    cout<<"Creating first object n1"<<endl;
    Number n1;
    {
        cout<<"Entering this block"<<endl;
        cout<<"Creating two more objects"<<endl;
        Number n2, n3;
        cout<<"Exiting this block"<<endl;
    }
    cout<<"Back to main"<<endl;
    return 0;
}
