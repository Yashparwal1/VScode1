// Friend Class -- ek class ke function ko dusri class ka friend kaise banate h
// we made 2 classes with their respective functions and the members/functions of one class tried to access the members of other class which is not possible. So we declared the members of one class the friend of other class or we can declare the whole class friend of other class. 

#include <iostream>
using namespace std;

class Complex; // this is Forward Declaration

class Calculator
{
public:
    int add(int a, int b)
    {
        return (a + b);
    }

    int sumRealComplex(Complex, Complex);
    // // int sumRealComplex(Complex n1, Complex n2) //ERROR
    // // {return ...} here we cannot write defination becoz it does not know what n1 and n2 are, it only knows that there is a Complex class (because of Forward Declaration).. that's it, nothing else
    int sumImgComplex(Complex, Complex);
    


};
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
    // ==> Declaring indiidual functions ofCalculator class as friend
    // friend int Calculator::sumRealComplex(Complex, Complex); // Declare calculator class above otherwise face error "Calculator has not been declared"
    // friend int Calculator::sumImgComplex(Complex, Complex); 
    
    // // what if I have so many things to claculate separately.. do I have to make each function of calculator a friend of class....
    // // NO    
    // // we can make whole Calculator class a friend of Complex Class so that whicheven function want to use the data of complex class it can use it and we dont need to declare each function as friend of complex class.

    // ==> ALITER: Declaring the entire Calculator class as friend
    friend class Calculator; //now when we made entire class as friend.. then comment the individual friend func

    void display()
    {
        cout << "Number : " << a << "+" << b << "i" << endl;
    }
};

int Calculator::sumRealComplex(Complex n1, Complex n2)
{
    return ((n1.a + n2.a));
}
int Calculator::sumImgComplex(Complex n1, Complex n2)
{
    return ((n1.b + n2.b));
}

int main()
{
    Complex c1, c2, c3;
    c1.set(1, 4);
    c1.display();

    c2.set(5, 8);
    c2.display();

    Calculator cal;
    int res1 = cal.sumRealComplex(c1, c2);
    int res2 = cal.sumImgComplex(c1, c2);
    cout << "-------------" << endl;
    cout << "Sum of real part: " <<res1<<endl;
    cout << "Sum of Img. part: " <<res2<<endl;
    return 0;
}


// -----------------------REAL and IMAG PART BOTH-------------------------------------------
// #include <iostream>
// using namespace std;

// class Complex; // this is Forward Declaration

// class Calculator
// {
// public:
//     int add(int a, int b)
//     {
//         return (a + b);
//     }
//     int sumRealComplex(Complex, Complex, int*, int*);
//     // int sumRealComplex(Complex n1, Complex n2) //ERROR
//     // {return ...} here we cannot write defination becoz it does not know what n1 and n2 are, it only knows that there is a Complex class (because of Forward Declaration).. that's it, nothing else
// };
// class Complex
// {
//     int a;
//     int b;

// public:
//     void set(int x, int y)
//     {
//         a = x;
//         b = y;
//     }
//     friend int Calculator::sumRealComplex(Complex, Complex, int*, int*); // Declare calculator class above otherwise face error "Calculator has not been declared"
//     void display()
//     {
//         cout << "Result: " << a << "+" << b << "i" << endl;
//     }
// };

// int Calculator::sumRealComplex(Complex n1, Complex n2, int *res1, int *res2)
// {
//     *res1 = n1.a + n2.a; 
//     *res2 = n1.b + n2.b;
//     // return real, img; 
//     // return ((n1.a + n2.a));
//     return 0;
// }

// int main()
// {
//     Complex c1, c2, c3;
//     c1.set(1, 4);
//     c1.display();

//     c2.set(5, 8);
//     c2.display();

//     Calculator cal;
//     int res1, res2;
//     cal.sumRealComplex(c1, c2, &res1, &res2);
//     cout << "-------------" << endl;
//     cout << "Result: " <<res1<<"+"<<res2<<"i"<<endl;
//     return 0;
// }
