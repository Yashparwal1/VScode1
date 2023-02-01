
#include<iostream>
using namespace std;

class Y; //forward declaration
class X{
    int data;
    public:
        void set(int value){
            data = value;
        }
        friend void add(X,Y); //compiler doesn't know what the heck here Y is.
};
class Y{
    int num;
    public:
        void set(int value){
            num = value;
        }
        friend void add(X,Y);
};
void add(X o1, Y o2){
    cout << "Summing data of X and Y objects is:"<<o1.data+o2.num<<endl;
}
// int main()
// {
//     X a;
//     Y b;
//     a.set(3);
//     b.set(5);
//     add(a,b);
//     return 0;
// }

class D; //forward declaration

class C{
    int cval;
    public:
        int indata(int a){
            cval = a;
        }
        void display(){
            cout << "x = "<<cval <<endl;
        }
        friend void exchange(C &,D &);
};
class D{
    int dval;
    public:
        int indata(int a){
            dval = a;
        }
        void display(){
            cout << "y = "<<dval <<endl;
        }
        friend void exchange(C &,D &);
};

void exchange(C &x, D &y){
    int temp = x.cval;
    x.cval = y.dval;
    y.dval = temp;
}

int main()
{
    C x;
    D y;
    x.indata(10);
    y.indata(20);
    cout << "Before Swapping:" <<endl;
    x.display();
    y.display();
    exchange(x,y);
    cout << "Before Swapping:" <<endl;
    x.display();
    y.display();

}