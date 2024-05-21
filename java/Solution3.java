// take 3 ponints with coordinates, find highest distance from origin for each point and print it.

import java.util.*;
class Point{
    double x;
    double y;
    Point(double x, double y){
        this.x = x;
        this.y = y;
    }
    // int getX(){
    //     return x;
    // }
    // int getY(){
    //     return y;
    // }
}
public class Solution3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter coordinates (x1,y1,x2,y2,x3,y3): ");
        double x1 = sc.nextInt();
        double y1 = sc.nextInt();
        double x2 = sc.nextInt();
        double y2 = sc.nextInt();
        double x3 = sc.nextInt();
        double y3 = sc.nextInt();
        sc.close();
        Point p1 = new Point(x1, y1);
        Point p2 = new Point(x2, y2);
        Point p3 = new Point(x3, y3);
        Point distance = highestDestanceFromOrigin(p1,p2,p3);
        // System.out.println(distance); // Point@hexno
        System.out.println(distance.x+","+distance.y);
    }
    public static Point highestDestanceFromOrigin(Point p1, Point p2, Point p3){
        double d1 = Math.sqrt(p1.x*p1.x + p1.y+p1.y); // squrt((x2-x1)^2 + (y2-y1)^2) [origin is 0,0]
        double d2 = Math.sqrt(p2.x*p2.x + p2.y*p2.y); // so this will be squrt(x2^2 + y2^2)
        double d3 = Math.sqrt(p3.x*p3.x + p3.y*p3.y);
        
        //conditional statement
        // return d1>d2?(d1>d3?p1:p3):(d2>d3?p2:p3);
        //using if-else
        if (d1>d2){
            if (d1>d3) {
                return p1;
            }
            else{
                return p3;
            }
        }
        else{
            if (d2>d3) {
                return p2;
            }
            else{
                return p3;
            }
        }
    }
}

