#include<iostream>
using namespace std;

class Complex{
    int real, imag;
    public:
        void setData(int x, int y){
            real = x;
            imag = y;
        }
        void getData(){
            cout << "The real part is "<< real<<endl;
            cout << "The Imaginary part is "<< imag<<endl;
        }
};

int main()
{
    // Complex c1;
    // c1.setData(2,5);
    // c1.getData();

    // Complex *ptr = &c1; //accessing public member through the pointer... pointer --> object --> members
    // ---OR---
    Complex *ptr = new Complex;
    (*ptr).setData(2,5); // parenthesis are necessay coz precenence of . operator is higher that asterisk 
    (*ptr).getData();
    
    ptr->setData(2,5); //ARROW OPERATOR
    ptr->getData();

    Complex *ptr1 = new Complex[3]; // ARRAY OF OBJECTS (3 objects here)
    //USE FOR LOOP to run for 3 objects 
    ptr1->setData(2,5); //ARROW OPERATOR
    ptr1->getData();


    return 0;
}