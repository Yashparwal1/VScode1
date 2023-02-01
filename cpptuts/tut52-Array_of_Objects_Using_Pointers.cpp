#include<iostream>
using namespace std;

class Shop{
    int id;
    float price;
    public:
        void setData(int a, float b){
            id = a;
            price = b;
        }
        void getData(){
            cout << "ITEM ID: "<<id<<endl
            <<"Price: "<<price<<endl;
        }
};

int main()
{
    int size = 3;
    // int *ptr = &size;
    // int *ptr = new int[size];
    Shop *ptr = new Shop[size];
    Shop *ptrTemp = ptr;
    int id;
    float price;
    for (int i = 0; i < size; i++)
    {
        cout << "Enter ID for item "<<i+1<<": ";
        cin>>id;
        cout << "Enter Price for item "<<i+1<<": ";
        cin>>price;
        ptr->setData(id, price);
        ptr++;   
    }
    for (int i = 0; i < size; i++)
    {
        ptrTemp->getData();
        ptrTemp++;
    }
    return 0;
}