/* 
Q. Why Object-Oriented Programming?

- C++ language was designed with the main intention of adding object-oriented programming to C language
- As the size of the program increases readability, maintainability, and bug-free nature of the program decrease.
- This was the major problem with languages like C which relied upon functions or procedure (hence the name procedural programming language)
- As a result, the possibility of not addressing the problem adequately was high
- Also, data was almost neglected, data security was easily compromised
- Using classes solves this problem by modeling program as a real-world scenario

==> Difference between Procedure Oriented Programming and Object-Oriented Programming

[*] Procedure Oriented Programming
* Consists of writing a set of instruction for the computer to follow
* The main focus is on functions and not on the flow of data
* Functions can either use local or global data
* Data moves openly from function to function

[*] Object-Oriented Programming
* Works on the concept of classes and object
* A class is a template to create objects
* Treats data as a critical element
* Decomposes the problem in objects and builds data and functions around the objects
 
==> Basic Concepts in Object-Oriented Programming

# Classes - Basic template for creating objects
# Objects – Basic run-time entities
# Data Abstraction & Encapsulation – Wrapping data and functions into a single unit
# Inheritance – Properties of one class can be inherited into others (**enhance code reusability)
# Polymorphism – Ability to take more than one forms
# Dynamic Binding – Code which will execute is not known until the program runs
# Message Passing – message (Information) call format

==> Benefits of Object-Oriented Programming

- Better code reusability using objects and inheritance
- Principle of data hiding helps build secure systems
- Multiple Objects can co-exist without any interference
- Software complexity can be easily managed

*/

// #include<iostream>

// using namespace std;
// int f(int n){
//   if(n < 1)return 0;
//   cout << n << endl;
//   return ((n%2==0)?-n:n) + f(n-1);
// }
// int main(){
//   cout<<f(10)<<endl;
//   return 0;
// }

// #include<bits/stdc++.h>
// using namespace std;

// void fun(vector<int>&v,int i,int j,int r,vector<int>&ans){
//    if(i == r){
//     for(int k : ans)
//     cout<<k<<" ";
//     cout<<endl;
//     return;
//    }
   
//    if(j >= v.size())return;
//    ans[i] = v[j];
//    fun(v,i+1,j+1,r,ans);
//    fun(v,i,j+1,r,ans);
// }
// int main(){
//     vector<int>v={1,2,3,4};
//     int r = 3;
//     vector<int>ans(r);
//     fun(v,0,0,r,ans);    
//     return 0;
// }


// #include <iostream>
// #include <algorithm>

// using namespace std;

// // Recursive function to generate all possible combinations of the elements in the array
// void generateCombinations(int arr[], int index, int n, int k)
// {
//     // if the combination has k elements, print it
//     if (index == k)
//     {
//         for (int i = 0; i < k; i++)
//             cout << arr[i] << " ";
//         cout << endl;
//         return;
//     }

//     // if there are no more elements to choose from, return
//     if (n == 0)
//         return;

//     // recursive case: generate all combinations that include arr[n-1]
//     arr[index] = n - 1;
//     generateCombinations(arr, index + 1, n - 1, k);

//     // recursive case: generate all combinations that do not include arr[n-1]
//     generateCombinations(arr, index, n - 1, k);
// }

// int main()
// {
//     int arr[] = {1, 2, 3, 4};
//     int n = sizeof(arr) / sizeof(arr[0]);

//     // generate all possible combinations of the array elements
//     for (int k = 1; k <= n; k++)
//     {
//         int combination[k];
//         generateCombinations(combination, 0, n, k);
//     }

//   return 0;
// }