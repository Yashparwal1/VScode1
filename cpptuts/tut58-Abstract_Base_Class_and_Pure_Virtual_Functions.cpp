/* 
Abstract base class is a class that has at least one pure virtual function in its body. 
The classes which are inheriting the base class must need to override the virtual function of the abstract class otherwise compiler will throw an error.
[isko banane maksad hi hota h ki isse or derived classed bna sake and unpe kaam kia ja ske]

Pure virtual function is a function that doesn’t perform any operation and the function is declared by assigning the value 0 to it. Pure virtual functions are declared in abstract classes.
Pure virtual function are not executed but it is necessary to override them.  
[ye force krte h defived classes ko ki missing function ko banaye hi (if missing) otherwise error!!]

*/

#include <iostream>
#include <cstring>
using namespace std;
/*
    tuts[0]->display();
    tuts[1]->display();
here both derived class's display is invoked 
        BUT
what if one or both of these display function are not then...
        THEN
virtual function of base class itself will run.. we know this...
        BUT
I want to something that will force all the derived classes which do not have display function to make one.  (ek esa virtual function jiski vajah se derived class me function banana HIIII pde)
      SO WHAT CAN I DO??
      HERE COME THIS...
PURE VIRTUAL FUNCTION: (aka "do nothing function")
       FOR THIS
we only need to do one thing that is assigning '0' to the existing notrmal virtual fucntion
       LIKE THIS
    virtual void display()=0
*/

class cwh
{
protected:
    string title;
    float rating;

public:
    cwh(string s, float r)
    {
        title = s;
        rating = r;
    }
    virtual void display()=0 
};
class cwhvideo : public cwh
{
    int videoID;

public:
    cwhvideo(string s, float r, int vid) : cwh(s, r)
    {
        videoID = vid;
    }
    void display()
    {
        cout << "" << endl;
        cout << "Video ID: " << videoID << endl;
        cout << "Amazing videos with title: " << title << endl;
        cout << "Rating is: " << rating << "out pf 5 stars" << endl;
    }
};
class cwhtext : public cwh
{
    int words;

public:
    cwhtext(string s, float r, int wc) : cwh(s, r)
    {
        words = wc;
    }
    void display()
    {
        cout << "" << endl;
        cout << "Amazing blog tutorial with title: " << title << endl;
        cout << "Word count: " << words << endl;
        cout << "Rating is: " << rating << " out pf 5 stars" << endl;
    }
};

int main()
{
    string title;
    float rating;
    int vid, wc;

    title = "Demo Title";
    rating = 4.5;
    vid = 101;
    wc = 250;

    cwhvideo video(title, rating, vid);
    // harry.display();
    cwhtext text(title, rating, wc);
    // text.display();

    cwh *tuts[2];
    //if we dont use pointer, then cwh display will be called only.. no video and text class
    tuts[0] = &video;
    tuts[1] = &text;

    tuts[0]->display();
    tuts[1]->display();

    return 0;
}