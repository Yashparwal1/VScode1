#include<iostream>
#include<cstring>
using namespace std;

class cwh{
    protected:
        string title;
        float rating;
    public:
        cwh(string s, float r){
            title = s;
            rating = r;
        }
        virtual void display(){} //derived class vale apne pane display hi call honge while calling cwh class using pointer
        // void display(){}
};
class cwhvideo : public cwh{
    int videoID;
    public:
        cwhvideo(string s, float r, int vid) : cwh(s, r){
            videoID = vid;
        }   
        void display(){
            cout <<""<<endl;
            cout << "Video ID: " <<videoID<<endl;
            cout << "Amazing videos with title: " <<title<<endl;
            cout << "Rating is: " <<rating<<"out pf 5 stars"<<endl;
        } 
};
class cwhtext : public cwh{
    int words;
    public:
        cwhtext(string s, float r, int wc) : cwh(s, r){
            words = wc;
        }
        void display(){
            cout <<""<<endl;
            cout << "Amazing blog tutorial with title: " <<title<<endl;
            cout << "Word count: " <<words<<endl;
            cout << "Rating is: " <<rating<<" out pf 5 stars"<<endl;
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

    cwh * tuts[2];
    tuts[0] = &video;
    tuts[1] = &text;

    tuts[0]->display();
    tuts[1]->display();
     
    return 0;
}