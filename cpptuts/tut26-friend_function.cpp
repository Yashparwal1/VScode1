/*
Friend Function
1. Scope of a friend function is not inside the class in which it is declared.
2. Since its scope is not inside the class, it cannot be called using the object of that class
3. It can be called/invoked like a normal function without using any object.
4. It cannot directly access the data members like other member function and it can access the data
    members by using object through dot operator.
5. It can be declared either in private or public part of the class definition.
6. Usually it has the objects as arguments.

USE:- Friend functions are used when we wan to give permission to an outsider function to access then private members of the class.

*/

#include<iostream>
using namespace std;

class Complex
{
    int a;
    int b;
public:
    void set(int x, int y)
    {
        a = x;
        b = y;
    }
    friend Complex Sumcomplex(Complex n1,Complex n2);
    void display(){
        cout << "Your number is: " <<a<<"+"<<b<<"i"<<endl;
    }
};

//its a foreign function not any member of Complex class, so we need to make it a friend of Comlex class
//BUT still it not a member func rather its a frind func NOW...  
Complex Sumcomplex(Complex n1,Complex n2){ //6th point -- Complex n1, Complex n2 usually are the objects
    Complex n3;
    n3.set((n1.a+n2.a), (n1.b+n2.b)); //4th point
    return n3;
}
/*  ===> ANOLOGY <=== 
    Sumcomplex is using private data, it is only allowed when Sumcomplex func. is FRIEND of Complex Class.
    So Complex class declared that Sumcomplex is its FRIEND by writing <<friend Complex Sumcomplex()>>
*/
int main()
{
    Complex c1,c2,c3;
    c1.set(1,4);
    c1.display();
    
    c2.set(5,8);
    c2.display();

    c3 = Sumcomplex(c1,c2);
    c3.display();
    return 0;
}

// -----------------------------------------------------------------------------------

// class Add
// {
//     int x, y, z;

// public:
//     Add(int a, int b){
//         x = a;
//         y = b;
//     }
//     friend int calculate(Add p);
// };
// int calculate(Add p)
// {
//     return (p.x + p.y);
// }
// void main()
// {
//     Add a(5, 5);
//     cout << calculate(a);
// }

class A {
  public:
    int x;
    void display();
};

void A::display(){
        cout << "Value of x is: " <<x<<endl;   
    }

int main() {
  A obj;
  obj.x = 10;
  cout << obj.x;
  return 0;
}