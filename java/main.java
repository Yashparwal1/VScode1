// class Base {
//     int i;

//     Base(int i) {
//         this.i = i;
//     }
// }

// class Derived extends Base {
//     Derived(int a, int b) { 
//         super(a);   
//         i = b;
//     }

//     void show() {
//         System.out.println("Sub class i = " + i);
//         System.out.println("Super class i = " + super.i);
//     }
// }

// class Main {
//     public static void main(String args[]) {
//         Derived d1 = new Derived(10, 20);
//         d1.show();
//     }
// }

// ---------------------------------- Abstract Class --------------------------------------------

// abstract class Base {
//     int x,y;
//     void show(){
//         System.out.println(x);
//         System.out.println(y);
//     }
//     // with abstract method
//     abstract void display();
// }

// class Derived extends Base {
//     void get(int a, int b){
//         this.x=a;
//         this.y=b;
//     }
//     void display(){
//         System.out.println("Display");
//     }
//     // public static void main(String args[]){
//     //     Derived d = new Derived();
//     //     d.get(10, 20);
//     //     d.show();
//     // }
// }
// class Main {
//     public static void main(String args[]) {
//         Derived d = new Derived();
//         d.get(100, 200);
//         d.show();
//         d.display();
//     }
// }

// ------------------------------------ INTERFACE -----------------------------------

// interface My{
//     void show();
// }
// interface you{
//     void display();
// }

// class Derived implements My,you {
//     public void show(){
//         System.out.println("show");
//     }
//     public void display(){
//         System.out.println("display");
//     }
// }
// class Main {
//     public static void main(String args[]) {
//         Derived m = new Derived();
//         m.show();
//         m.display();
//     }
// }

// ----------------------------------------------------------------------------------------

// import java.awt.*;

// class myframe extends Frame{
//     myframe(String p){
//         super(p);
//         setSize(500, 500);
//         setVisible(true);
//     }
// }
// class Main{
//     public static void main(String[] args) {
//         new myframe("ff");
//     }
// }

// ----------------------------------------------------------------------------------------

// class Main {

//     /*
//      * Complete the 'fizzBuzz' function below.
//      *
//      * The function accepts INTEGER n as parameter.
//      */

//     public static void main(String[] args) {
//         int n = 15;
//         for(int i=1; i<=n; i++){
//             if (i%3==0 && i%5==0) {
//                 System.out.println("FizzBuzz");
//             }
//             else if (i%3==0 && i%5!=0) {
//                 System.out.println("Fizz");
//             }
//             else if (i%3!=0 && i%5==0) {
//                 System.out.println("Buzz");
//             }
//             else{
//                 System.out.println(i);
//             }
//         }

//     }

// }

// ----------------------------------------------------------------------------------------

class Main{
    public static void main(String[] args) {
        int y = 12;
        int x = 10;
        x = x++ + y++;
        System.out.println(x);
        int z = x++;
        System.out.println(z);


    }
}