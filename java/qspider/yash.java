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

class Test{
    int a = 20;
    static int b = 10;
    public static void main(String[] args) {
        int x = 30;
        System.out.println(x);
        System.out.println(b);
        Test access = new Test();
        System.out.println(access.a); //not directly but with object reference
    }
}