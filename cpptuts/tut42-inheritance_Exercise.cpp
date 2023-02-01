#include<iostream>
using namespace std;
 
class SimpleCalc{
    int x,y,res;
    public:
        void set(int a, int b){
            x = a;
            y = b;
        }
        void set(int a, float b){
            x = a;
            y = b;
        }
        void set(float a, int b){
            x = a;
            y = b;
        }
        void set(float a, float b){
            x = a;
            y = b;
        }
        void SimOp();
        void show(){
            cout << "Result: "<<res<<endl;
        }
};
void SimpleCalc::SimOp(){
    char op;
    int out = 1;
    while (out == 1)
    {
        cout << "Enter Operation [ + , - , * , / ] : ";
        cin >> op;
        switch (op)
        {
        case '+':
            res = x + y;
            out = 0;
            break;
        
        case '-':
            res = x - y;
            out = 0;
            break;
        
        case '*':
            res = x * y;
            out = 0;
            break;
        
        case '/':
            res = x / y;
            out = 0;
            break;
        
        default:
            cout << "Please Enter correct operator..." <<endl;
            break;
        }
    }
}

class ScientificCalc : public SimpleCalc{
    int x, y, res;
    public:
        void SciOp(); 
};
void ScientificCalc::SciOp(){
    int op;
    cout << "[1] - Exponent" <<endl<<
    "[2] - Under Root"<<endl<<
    "[3] - Log"<<endl<<
    "[4] - Log with base 10"<<endl;
    cout << "==> Choose: ";
    cin>>op;
    switch (op)
    {
    case 1:
        res = 
        break;
    
    default:
        break;
    }

}
int main()
{
    ScientificCalc obj;
    int a,b;
    cout << "Enter a: ";
    cin >> a;
    cout << "Enter b: ";
    cin >> b;
    obj.set(a,b);
    obj.SimOp();
    obj.show();   
    return 0;
}