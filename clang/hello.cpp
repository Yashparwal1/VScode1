#include<iostream>
#define esc 27
using namespace std;

class toll
{
private:
    unsigned int totalCars;
    double totalCash;
public:
    toll()
    {
        totalCars = 0;
        totalCash = 0;
    }
public:
    void payingCars()
    {
        totalCars += 1;
        totalCash += 50;
    }
public:
    void nonpayingCars()
    {
        totalCars += 1;
    }
public:
    void display()
    {
        cout << "\nTotal no. of cars passed: ", totalCars;
        cout << "\nTotal money collected: ", totalCash;
    }
};

int main()
{
    toll obj;
    int ch;
    while (1)
    {
        cout << "\n1. for paying cars.";
        cout << "\n2. for Non-paying cars.";
        cout << "\nEsc. to exit the program.\n";
        cin >> ch;
        switch (ch)
        {
        case 1:
            obj.payingCars();
            break;
        case 2:
            obj.nonpayingCars();
            break;
        case esc:
            obj.display();
            break;
        default:
            cout << "Wrong Choice !!\n";
            break;
        }
    }
    
    return 0;    
}

