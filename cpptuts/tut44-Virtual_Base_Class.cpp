// The virtual base class is a concept used in multiple inheritances to prevent ambiguity between multiple instances. For example: suppose we created a class “A” and two classes “B” and “C”, are being derived from class “A”. But once we create a class “D” which is being derived from class “B” and “C” as shown in figure 1. There will be ambiguity for the data inherited from class "A"
/*
                                              A  --> GRANDPARANT [VIRTUAL BASE CLASS]
                                             / \
                                PARENT1 <-- B   C --> PARENT2  [DERIVED CLASSES]
                                             \ /
                                              D  --> CHILD

class B : virtual public A                                          class C : virtual public A
*/

// #include <iostream>
// using namespace std;
// class A
// {
// public:
//     void say()
//     {
//         cout << "Hello world" << endl;
//     }
// };
// class B : public virtual A{

// };
// class C : public virtual A{

// };
// class D : public B, public C{

// };

// ------------------------------------------------------------------------------------

#include<iostream>
using namespace std;
 
class Student{
    protected:
        int roll;
    public:
        void set_Roll(int a){
            roll = a;
        }
        void display_roll(){
            cout << "Roll No. is: "<<roll<<endl;
        }
};

class Test : virtual public Student{
    protected:
        float maths, physics;
    public:
        void set_Marks(float m1, float m2){
            maths = m1;
            physics = m2;
        }
        void display_marks(){
            cout<< "Student marks: " <<endl
                << "Maths: "<<maths<<endl
                << "Phisics: "<<physics<<endl;
        }
};
class Sports : virtual public Student{
    protected:
        int score;
    public:
        void set_Score(int s){
            score = s;
        }
        void display_score(){
            cout<< "Score is: "<<score <<endl;
        }
};

class Result : public Test, public Sports{
    private:
        float total;
    public:
        void display_result(){
            total = maths+physics+score;
            display_roll();
            display_marks();
            display_score();
            cout << "Your final result is: "<< total <<endl;
        }
};

int main()
{
    Result s1;
    s1.set_Roll(21);
    s1.set_Marks(30.5, 20.7);
    s1.set_Score(30);
    s1.display_result();
    return 0;
}