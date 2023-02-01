// “this” is a keyword that is an implicit pointer. “this” pointer points to the object which calls the member function
// (this pointer us objects ko point krega jisne member function ko call kia)

#include<iostream>
using namespace std;
class A{
    int a;
    public:
        void setData(int a){
            // a = a //garbage value (priority to the local variable)
            this->a = a; //
        }

        // A & setData(int a){
        //     // a = a //garbage value (priority to the local variable)
        //     this->a = a; //
        //     return *this; //if we are returning this then see line 27
        // }

        void getData(){
            cout<<"The value of a is "<<a<<endl;
        }
};

int main(){
    A a;
    a.setData(4);
    // a.setData(4).getData();
    a.getData();
    return 0;
}
