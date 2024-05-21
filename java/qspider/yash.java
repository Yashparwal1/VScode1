package qspider;
import java.util.*;

// class yash {
//     // public static void test(String[] args) {
//     //     System.out.println("test method");
//     // }
//     public static void main(String[] args) {
//     //  System.out.println("Hello world");
    
//     }
//     // public static void demo(String[] args) {
//     //     System.out.println("demo method");
//     // }
// }
 
// class Test{
//     public static void start(){
//         System.out.println("this is start method");
//     }
//     public static void main(String[] args) {
//         start();
//         Test.start();
//     }
// }
// class Test{
//     public void start(){
//         System.out.println("this is start method");
//     }
//     public static void main(String[] args) {
//         Test t1 = new Test();
//         t1.start();
//     }
// }

// -------------------------------------------------------------

// class Vehicle{
//     public static void main(String[] args) {
//         System.out.println("This is main method of Vehical");
//         Car c1 = new Car();
//         c1.start();
//     }
// }

// -------------------------------------------------------------

// class Employ{
//     int x = 10;
//     double y;
//     String z = "mohan";
//     String p;
// }
// class Test{
    // public static void main(String[] args) {
        // int x = 30;
        // Employ e1 = new Employ();
        // System.out.println(x); // 30
        // System.out.println(e1); // Employ@hexNo
        // System.out.println(e1.x); //10
        // System.out.println(e1.y); // 0.0
        // System.out.println(e1.x); // mohan
        // System.out.println(e1.p); // null
        
        // int i = 0;
        // while (true) {
        //     System.out.println("i = "+i);
        //     i++;
        // }
        // System.out.println("End program"); // unreachable statement
    // }
// }

// you can access static variables using an object in many programming languages, but it is generally not recommended.

// class abc{
//     static int roll = 1002;
//     static int mark;
// }
// class Test{
//     public static void main(String[] args) {
//         abc obj = new abc();
//         abc obj01 = new abc();
//         obj01.mark = 300;
//         obj01.roll = 1020;
//         obj.mark = 400;
//         System.out.println("roll no: "+obj01.roll);  //47.44 timestamp
//         System.out.println("roll no: "+obj01.roll);
//     }
// }

// class myClass {
//     public static String name = "";
//     public static void assignName(String passedName){
//         name = passedName;
//     }
// }
// class HelloWorld {
//     public static void main(String[] args) {
//         myClass.assignName("Board Infinity"); //directly using class name
//         System.out.println(myClass.name);
 
//         // Accessing the static method assignName()
//         // having the object reference
//         myClass object = new myClass();
        
//         // Assign the name
//         object.assignName("Java");
        
//         // Display the name
//         System.out.println(object.name);
//     }
// }

// class Test{
//     public static void start(){
//         System.out.println("this is start method");
//     }
//     public static void main(String[] args) {
//         Test t1 = new Test();
//         start(); //directly
//         Test.start(); //using class reference
//         t1.start(); // uisng object reference
//     }
// }

// class Test{
//     int a = 20;
//     static int b = 10;
//     public static void main(String[] args) {
//         int x = 30;
//         System.out.println(x);
//         System.out.println(b);
//         Test access = new Test();
//         System.out.println(access.a); //not directly but with object reference
//     }
// }

// ==============================================================
/* 123 = 1 fact + 2 fact + 3 fact = 9 
* condition: one method to separate digit and add fact of them. 2nd method to find fact of each digit and reyturn so that 1st method can add them
* 1st method to be called by main and 2nd to be called by 1st method
*/

// class Fact{
//     // static int n;
//     public static int factorial(int x){
//         // n = x;
//         if (x==1 || x==0) {
//             return 1;
//         }
//         else if (x==2){
//             return 2;
//         }
//         else{
//             int fact = 1;
//             for (int i = x; i >= 2; i--){
//                 fact = fact*i;
//             }
//             return fact;
//         }
//     }
// }
// class Num{
//     public static int getDigits(int d){
//         int temp=0;
//         String str = Integer.toString(d);
//         for(int i = 0; i<str.length(); i++){
//             // System.out.println(str.charAt(i));
//             char c= str.charAt(i);
//             // int c_int = c-'0';
//             int f = Fact.factorial(c-'0');
//             temp = temp + f;
//         }
//         return temp;
//     }
// }
// class Main{
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter a no: ");
//         int n = sc.nextInt();
//         System.out.println(Num.getDigits(n));
//         sc.close();
//     }
// }

// ==============================================================

// pass a no. to a method and return square value
// class Main{
//     public static void main(String[] args) {
//         int x = 10;
//         int result = getSquare(x);
//         System.out.println(result);
//     }
//     public static int getSquare(int x){
//         return x*x;
//     }
// }

// ===========================================================
// design a method which will take an int no and will return no is even or odd
// use condditional op

// class Main{
//     public static void main(String[] args) {
//         int x = 10;
//         String result = EvenOrOdd(x);
//         System.out.println(result);
//     }
//     public static String EvenOrOdd(int x){
//         return x%2==0?"Even":"odd";
//     }
// }

