#include <iostream>
#include <cstring>
using namespace std;
/*
 ==> Rules for virtual functions <==
1. They cannot be static
2. They are accessed by object pointers**
3. Virtual functions can be a friend of another class
4. A virtual function in the base class might not be used sometimes.
5. If a virtual function is defined in a base class, there is no necessity of redefining it in the derived class
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
    virtual void display() {} // derived class vale apne pane display hi call honge while calling cwh class using pointer
    // void display(){}
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

// -------------------------------------------------------------------------------

class B
{
public:
    // virtual void show() //one time base show and other time dericed show.
    void show() //both times base show
    {
        cout << "I am in base show" << endl;
    }
};
class D : public B
{
public:
    void show()
    {
        cout << "I am in derived show" << endl;
    }
};
// int main()
// {
//     B b, *bp;
//     D d;
//     bp = &b;
//     bp->show();
//     bp = &d;
//     bp->show();
// }
