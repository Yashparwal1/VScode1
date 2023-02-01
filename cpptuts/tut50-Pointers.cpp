// Pointers are variables that are used to store the address. Pointers are created using “*”.
#include<iostream>
using namespace std;

int main(){
    // Basic Example
    int a = 4;
    int* ptr = &a; //OR *ptr = 4
    cout<<"The value of a is "<<*(ptr)<<endl;
  
    // "new" operator
    // int *p = new int(40);
    float *p = new float(40.78);
    cout << "The value at address p is " << *(p) << endl;
    
    int *arr = new int[3]; //integer array using new 
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    cout << "The value of arr[0] is " << arr[0] << endl;
    cout << "The value of arr[1] is " << arr[1] << endl;
    cout << "The value of arr[2] is " << arr[2] << endl;

    // "delete" operator
    int *arr = new int[3];
    arr[0] = 10;
    arr[1] = 20; //OR *(arr+1) = 20
    arr[2] = 30;
    delete[] arr; //NOW below cout statements will give garbage values
    cout << "The value of arr[0] is " << arr[0] << endl;
    cout << "The value of arr[1] is " << arr[1] << endl;
    cout << "The value of arr[2] is " << arr[2] << endl;

    return 0;
}

