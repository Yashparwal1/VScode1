#include <iostream>
using namespace std;

// template <class T>
// class vector
// {
//     public:
//         T *arr;
//         int size;
//         vector(int m)
//         {
//             size = m;
//             arr = new T[size];
//         }
//     T dotProduct(vector &v){
//         T d=0;
//         for (int i = 0; i < size; i++)
//         {
//             d+=this->arr[i]*v.arr[i];
//         }
//         return d;
//     }
// };
 
// int main()
// {
//     vector <int> v1(3); //vector 1
//     v1.arr[0] = 4;
//     v1.arr[1] = 3;
//     v1.arr[2] = 1;
//     vector <int> v2(3); //vector 2
//     v2.arr[0]=1;
//     v2.arr[1]=0;
//     v2.arr[2]=1;
//     int a1 = v1.dotProduct(v2);
//     cout<<a1<<endl;

//     vector<float> v3(3); //vector 1 with a float data type
//     v3.arr[0] = 1.4;
//     v3.arr[1] = 3.3;
//     v3.arr[2] = 0.1;
//     vector<float> v4(3); //vector 2 with a float data type
//     v4.arr[0]=0.1;
//     v4.arr[1]=1.90;
//     v4.arr[2]=4.1;
//     float a2 = v3.dotProduct(v4);
//     cout<<a2<<endl;
//     return 0;
// }

int main(){
    char *ptr;
    char str[] = "abcdefg";
    ptr = str;
    ptr += 5;
    cout << ptr;
    return 0;
}