#include<iostream>
using namespace std;
    
class Binary{
    string s;
    int choice;
    void chk_bin(void); //if we dont want user to access any func, then make it private and use it using nesting
    public:
        void read(void);
        // void chk_bin(void); //now we can make it private as it is not called from main instead it is nested
        void operation(void);
};

void Binary::read(void){
    cout << "Enter a binary number: ";
    cin >> s;
}
void Binary::chk_bin(void){
    // C APPROACH
    // for (int i = 0; arr[i]!='\0' ; i++)
    // {
    //     count++
    // }
    // C++ APPROACH
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != '0' && s.at(i) != '1')
        {
            cout << "Incorrect binary format !!" <<endl;
            exit(0);
        }
    }
}

void Binary::operation(void){
    chk_bin();
    cout << "[1] 1's complementn\n[2] decimal conversion\n ==> CHOOSE: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        for (int i = 0; i < s.length(); i++)
        {
            if (s.at(i) == '0')
            {
                s.at(i) = '1';
            }
            else{
                s.at(i) = '0';
            }
        }
        cout << "After 1's complement = " <<s<<endl;
        break;
    
    case 2:
        cout <<s<<" = "<<stoi(s,0,2);
        break;
    
    default:
        break;
    }
}

int main()
{
    class Binary b;
    b.read();
    b.chk_bin(); //not calling here instead this function is nested in operation() function
    b.operation();
    return 0;
}