#include<iostream>
using namespace std;
 
class Complex{
    int a,b;
    public:
        Complex(int x, int y){
            a = x;
            b = y;
        }
        Complex(int x){
            a = x;
            b = 0;
        }
        void display(){
            cout << "Your no. is: "<< a << "+" << b << "i" <<endl;
        }
};
int main()
{                                           //  _
    Complex c(1,5); //parameterised constructor  |
    c.display();                            //   |   
    Complex c2(5); // parameterised constructor  |
    c2.display();                           //   |___ `Constructor Overloading`
    Complex c3();                           //   |
    c3.display(); // default constructor         |
    return 0;                               //   |
}                                           //  _|