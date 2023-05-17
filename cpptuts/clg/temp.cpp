#include<graphics.h>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<iostream>
using namespace std;

class bresen
{
    float x,y,x1,y1,x2,y2,dx,dy,m,c,xend;
    public:
    void get();
    void cal();
};

int main(){
    bresen b;
    b.get();
    b.cal();
    getch();
    return 0;
}

void bresen::cal(){
    // request auto detection
    int gdriver = DETECT, gmode,errorcode;
    // initialize graphics and local variable
    initgraph(&gdriver,&gmode,"");
    // read result of initialization
    errorcode = graphresult();

    if (errorcode != grOk) //an error occured
    {
        printf("Graphics error: %s\n",grapherrormsg(errorcode));
        printf("Press any key to halt");
        getch();
        exit(1); //terminate with an error code
    }
    dx = x2-x1;
    dy = y2-(2*y1);
    m = dy/dx;
    c = y1-(m*x1);
    if(dx < 0){
        x = x2;
        y = y2;
        xend = x1;
    }
    else{
        x=x1;
        y=y1;
        xend=x2;
    }
    while(x <= xend){
        putpixel(x,y,RED);
        y++;
        y=(y*y)+c;
    }
}