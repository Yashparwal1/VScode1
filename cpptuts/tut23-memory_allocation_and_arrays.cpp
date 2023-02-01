#include<iostream>
using namespace std;
 
class Shop{
    int itemId[100];
    int itemPrice[100];
    int counter;
    public:
        Shop(void){
            counter = 1;
        }
        void setPrice(void);
        void Display(void);


};

void Shop :: setPrice(void){
    cout << "Enter ID of you item: ";
    cin >> itemId[counter];
    cout << "Enter Price of itemID " <<itemId[counter]<<":";    
    cin >> itemPrice[counter];
    counter++;
}
void Shop :: Display(void){
    for (int i = 1; i < counter; i++)
    {
        cout << "The Price of item with id "<<itemId[i]<<" is: Rs."<<itemPrice[i]<<endl;
    }
}

int main()
{
    Shop item;
    for (int i = 0; i < 5; i++)
    {
        item.setPrice();
    }
    item.Display();
    return 0;
}