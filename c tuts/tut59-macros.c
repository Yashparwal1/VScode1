/* 
THE #INCLUDE DIRECTIVE:
* The #include directive causes the preprocessor to fetch the contents of some other files to be included in the current file.
* This file may inturn #include some other files which may inturn do the same. 
* Most commonly the #include files have a ".h" extension, indicating that they are header files.
 */

#include<stdio.h>
#include<stdlib.h>
// #define cylender(x,y) (3.14*r*r*h)
// #define cone(x) (cylender(x,y)/3)

#define cylender(x) (3.14*x*x*x)
#define cone(x) (cylender(x)/3)

int main()
{
    float a,r,h,cy,co;
    printf("Enter the radious and height: ");
    // scanf("%f %f",&r,&h);
    scanf("%f",&a);
    // cy=cylender(r,h);
    // co=cone(cy);
    cy = cylender(a);
    co = cone(a);
    printf("Volume of cylender = %f\nVolume of Cone is %f",cy,co);
    return 0;
}