package clg;

// class Main{
//     public static void main(String[] args){
//         System.out.println("Hello world");
//     }
// }

// abstract class Shape {
//     private double wd;
//     private double ht;
//     public Shape(double width, double height){ //constructor
//         this.wd = width;
//         this.ht = height;
//     }   

//     public final double getWidth(){ //cannot be overridden due to final, so no inheritence
//         return wd;
//     }
//     public final double getHeight(){ //cannot be overridden due to final, so no inheritance
//         return ht;
//     }
//     abstract double getArea(); //will be defined in child class like get area of which shape, rect, sq etc 

// }

// class Rectangle extends Shape{
//     public Rectangle(double width, double height){
//         super(width,height); //calling parent's constructor 
//     }

//     @Override
//     final double getArea(){
//         return this.getWidth()*getHeight();
//     }
// }
// class Square extends Shape{
//     public Square(double side){
//         super(side,side); //calling parent's constructor 
//     }

//     @Override
//     final double getArea(){
//         return this.getWidth()*getHeight(); //wd and ht is same, so side*side
//     }
// }

// class Main{
//     public static void main(String[] args) {
//         // create and new Rectangle object and assigns it to the var s1. Rectangle class is a subclss of Shape, so the s1 var can be used to refer to the Rectangle object 
//         Shape s1 = new Rectangle(6.3, 5.2);
//         Shape s2 = new Square(4.6);

//         //we have to use contatination in println, or use printf for "something",s1.getArea() but concat. is slower :)
//         // System.out.println("Area of rectange is: ",s1.getArea()); 
//         System.out.println("Area of rectangle is: "+s1.getArea());
//         System.out.println("Area of square is: "+s2.getArea());

//     } 
// }

// ===========================================================================================

// class Animal {
//     void makeSound() {
//         System.out.println("Animal makes a generic sound");
//     }
// }
// class Dog extends Animal {
//     @Override
//     void makeSound() {
//         System.out.println("Dog barks");
//     }

//     // Method overloading in the same class
//     void makeSound(String barkType) {
//         System.out.println("Dog barks with " + barkType + " sound");
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         System.out.println("Method Overloading Example");
//         Dog myDog = new Dog();
//         myDog.makeSound();
//         myDog.makeSound("Loud");

//         System.out.println("\nMethod Overriding Example");
//         Animal anotherAnimal = new Animal();
//         anotherAnimal.makeSound(); // animal class method is called
//         Animal anotherDog = new Dog(); // Upcasting
//         anotherDog.makeSound(); // dog class method is called (Dynamic Binding)
//     }
// }

// =======================================================================================

// import java.io.*;

// interface Vehicle {
//     // all are the abstract methods.
//     void changeGear(int a);

//     void speedUp(int a);

//     void applyBrakes(int a);
// }

// class Bicycle implements Vehicle {
//     int speed;
//     int gear;

//     // to change gear
//     @Override
//     public void changeGear(int newGear) {
//         gear = newGear;
//     }

//     // to increase speed
//     @Override
//     public void speedUp(int increment) {
//         speed = speed + increment;
//     }

//     // to decrease speed
//     @Override
//     public void applyBrakes(int decrement){
//         speed = speed - decrement;
//     }

//     public void printStates() {
//         System.out.println("speed: " + speed
//                 + " gear: " + gear);
//     }
// }
// class Bike implements Vehicle {
//     int speed;
//     int gear;
//     // to change gear
//     @Override
//     public void changeGear(int newGear){
//         gear = newGear;
//     }
//     // to increase speed
//     @Override
//     public void speedUp(int increment){
//         speed = speed + increment;
//     }
//     // to decrease speed
//     @Override
//     public void applyBrakes(int decrement){
//         speed = speed - decrement;
//     }
//     public void printStates() {
//         System.out.println("speed: " + speed + " gear: " + gear);
//     }
// }

// class Main {
//     public static void main (String[] args) {
//         // creating an instance of Bicycle
//         // doing some operations
//         Bicycle bicycle = new Bicycle();
//         bicycle.changeGear(2);
//         bicycle.speedUp(3);
//         bicycle.applyBrakes(1);
//         System.out.println("Bicycle present state :");
//         bicycle.printStates();

//         // creating instance of the bike
//         Bike bike = new Bike();
//         bike.changeGear(1);
//         bike.speedUp(4);
//         bike.applyBrakes(3);

//         System.err.println("Bike present state: ");
//         bike.printStates();
//     }
// }

// ==================================================================

// import java.applet.*;
// import java.awt.*;
// public class Main extends Applet
// {
//     public void paint(Graphics g){
//         Color c;
//         c=Color.black;
//         g.setColor(c);
//         g.fillRect(237,114,10,500);
//         c=Color.red;
//         g.setColor(c);
//         g.fillRect(248,125,200,25);
//         c=Color.white;
//         g.setColor(c);
//         g.fillRect(248,150,200,25);
//         c=Color.green;
//         g.setColor(c);
//         g.fillRect(248,175,200,25);
//         c=Color.blue;
//         g.setColor(c);
//         g.drawOval(342,149,25,25);
//         int l=0;
//         int x=355,y=162;
//         double x1,y1;
//         double d;
//         c=Color.black;
//         g.setColor(c);
//         for(int i=1;i<=24;i++)
//         {
//             d=(double)l*3.14/180.0;
//             x1=x+(double)10*Math.cos(d);
//             y1=y+(double)10*Math.sin(d);
//             g.drawLine(x,y,(int)x1,(int)y1);
//             l=l+(360/24);
//         }
//     }
// }

// ===================================================================
// class Main {
//     public static void main(String[] args) {

//         try {

//             // code that generate exception 
//             int divideByZero = 5 / 0;
//             System.out.println("Rest of code in try block");
//         }

//         catch (ArithmeticException e) {
//             System.out.println("ArithmeticException => " + e.getMessage());
//         }
//     }
// }

// class Main {
//     public static void main(String[] args) {
//         try {
//             // code that generates exception 
//             int divideByZero = 5 / 0;
//         }
//         catch (ArithmeticException e) {
//             System.out.println("ArithmeticException => " + e.getMessage());
//         }
//         finally {
//             System.out.println("This is the finally block");
//         }
//     }
// }

// class Main {
//     public static void divideByZero() {

//         // throw an exception 
//         throw new ArithmeticException("Trying to divide by 0");
//     }

//     public static void main(String[] args) {
//         divideByZero();
//     }
// }

// ===================================================================

// import java.util.HashSet;
// import java.util.Scanner;
// import java.util.Set;

// public class Main {
//     public static void main(String[] args) { 
//         Scanner scanner = new Scanner(System.in); 
//         Set<Integer> uniqueNumbers = new HashSet<>(); 
//         System.out.println("Enter 5 numbers between 10 and 100 inclusive:"); 
//         for (int i = 0; i < 5; i++) { 
//             int number; 
//             // Ensure the entered number is between 10 and 100 inclusive 
//             do { 
//             System.out.print("Enter number " + (i + 1) + ": "); number = scanner.nextInt(); 
//             } while (number < 10 || number > 100); 

//             // Check if the number is a duplicate 
//             if (uniqueNumbers.add(number)) { 
//                 System.out.println("Unique values: " + uniqueNumbers); 
//             } 
//             else { 
//                 System.out.println("Duplicate number. Not added to the set."); i--; // Decrement i to re‐enter the current number 
//             } 
//         }
//         System.out.println("Final set of unique values: "+uniqueNumbers);
//         scanner.close();
//     }
// }

// ===================================================================
// import java.lang.*;

// class ThreadDemo extends Thread {
//     // Method 1
//     // run() method for the thread that is called // as soon as start() is invoked
//     // for thread in main() 
//     public void run()
//     {
//         System.out.println("Inside run method");
//     }
//     public static void main(String[] args) {

//         // Creating random threads with the help of above class
//         ThreadDemo t1 = new ThreadDemo();
//         ThreadDemo t2 = new ThreadDemo();
//         ThreadDemo t3 = new ThreadDemo();

//         // Thread 1 - Display the priority of above thread using getPriority() method
//         System.out.println("t1 thread priority : "+ t1.getPriority());
//         // Thread 2 - Display the priority of above thread
//         System.out.println("t2 thread priority : " + t2.getPriority());
//         // Thread 3
//         System.out.println("t3 thread priority : " + t3.getPriority());

//         // Setting priorities by passing integer arguments
//         t1.setPriority(2); 
//         t2.setPriority(5);
//         t3.setPriority(8);

//         // t3.setPriority(21); // will throw IllegalArgumentException

//         System.out.println("t1 thread priority : " + t1.getPriority());
//         System.out.println("t2 thread priority : " + t2.getPriority());
//         System.out.println("t3 thread priority : " + t3.getPriority());

//         // Displays the name of currently executing Thread
//         System.out.println("Currently Executing Thread : " + Thread.currentThread().getName());
//         System.out.println("Main thread priority : " + Thread.currentThread().getPriority());

//         // Main thread priority is set to 10
//         Thread.currentThread().setPriority(10);
//         System.out.println("Main thread priority : " + Thread.currentThread().getPriority());
//     }
// }

// ===================================================================
// public class Main {
//     public static void main(String[] args) {
//         String str = "aaaabbbbcccc"; 
//         int len = str.length();
//         int n = 3; //devide the string in n equal parts
//         int temp = 0;
//         int chars = len / n;
//         String[] equalStr = new String[n]; // Stores the array of string
//         // Check whether a string can be divided into n equal parts
//         if (len % n != 0) {
//             System.out.println("Sorry this string cannot be divided into " + n + " equal parts.");
//         } 
//         else {
//             for (int i = 0; i < len; i = i + chars) {
//                 // Dividing string in n equal part using substring() 
//                 String part = str.substring(i, i+chars); equalStr[temp] = part;
//                 temp++;
//             }
//             System.out.println(n + " equal parts of given string are ");
//             for (int i = 0; i < equalStr.length; i++) {
//                 System.out.println(equalStr[i]);
//             }
//         }
//     }
// }

// ===================================================================
// import java.util.Scanner;

// class Figure { 
//     double dimension1;double dimension2;
//     public Figure(double dimension1, double dimension2) { 
//         this.dimension1 = dimension1; 
//         this.dimension2=dimension2;
//     }
//     // Method to calculate the area (to be overridden by subclasses) 
//     public double area() { 
//         return 0.0;
//     }
// }
// class Rectangle extends Figure {
//     public Rectangle(double length, double width){ 
//         super(length, width);
//     }
//     // Override area method for Rectangle
//     @Override
//     public double area() {
//         return dimension1 * dimension2;
//     }
// }
// class Triangle extends Figure {
//     public Triangle(double base, double height){
//         super(base,height);
//     }
//     // Override area method for Triangle
//     @Override
//     public double area() {
//         return 0.5 * dimension1 * dimension2;
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         // Creating a Rectangle object
//         System.out.println("Enter dimensions for Rectangle:");
//         System.out.print("Length: ");
//         double length = scanner.nextDouble();
//         System.out.print("Width: ");
//         double width = scanner.nextDouble();
//         Rectangle rectangle = new Rectangle(length, width);

//         // Creating a Triangle object
//         System.out.println("\nEnter dimensions for Triangle:");
//         System.out.print("Base: ");
//         double base = scanner.nextDouble();
//         System.out.print("Height: ");
//         double height = scanner.nextDouble();
//         Triangle triangle = new Triangle(base, height);

//         // Displaying the areas
//         System.out.println("\nArea of Rectangle: " + rectangle.area());
//         System.out.println("Area of Triangle: " + triangle.area());

//         scanner.close();
//     }
// }

// ===================================================================
// import java.util.ArrayList;
// import java.util.List;
// import java.util.Scanner;

// class Question {
//     String prompt;
//     String answer;
//     public Question(String prompt, String answer) {
//         this.prompt = prompt;
//         this.answer = answer;
//     }
//     public boolean isCorrect(String response) {
//         return answer.equalsIgnoreCase(response);
//     }
//     @Override
//     public String toString() {
//         return "Question: " + prompt;
//     }
// }
// class MultipleChoiceQuestion extends Question {
//     List<String> options;
//     public MultipleChoiceQuestion(String prompt, List<String> options, String answer) {
//         super(prompt, answer);
//         // Ensure the answer is a valid index (A:0, B:1, C:2, ...)
//         int correctIndex = answer.toUpperCase().charAt(0) - 'A';
//         if (correctIndex >= 0 && correctIndex < options.size()) {
//             this.answer = Integer.toString(correctIndex);
//         } else {
//             // Handle invalid answer
//             throw new IllegalArgumentException("Invalid answer for multiple-choice question");
//         }
//         this.options = options;
//     }

//     @Override
//     public boolean isCorrect(String response) {
//         // Convert the response letter to an index (A:0, B:1, C:2, ...)
//         int userIndex = response.toUpperCase().charAt(0) - 'A';

//         // Compare the user's index with the correct index
//         return userIndex == Integer.parseInt(answer);
//     }

//     @Override
//     public String toString() {
//         StringBuilder sb = new StringBuilder(prompt + "\n");
//         for (int i = 0; i < options.size(); i++) {
//             sb.append((char) ('A' + i)).append(". ").append(options.get(i)).append("\n");
//         }
//         return sb.toString();
//     }
// }
// public class Main {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         // Create questions
//         List<Question> questions = new ArrayList<>();
//         questions.add(new MultipleChoiceQuestion("What is the capital of France?", List.of("Paris", "Berlin", "London", "Madrid"), "A"));
//         questions.add(new Question("Is the earth round?", "True"));
//         questions.add(new MultipleChoiceQuestion("What is 2 + 2?", List.of("3", "4", "5", "6"), "B"));
//         questions.add(new Question("Is Java a programming language?", "True"));
//         // Take the exam
//         int totalMarks = 0;
//         for (Question question : questions) {
//             System.out.println(question);
//             System.out.print("Your answer: ");
//             String userResponse = scanner.nextLine();
//             if (question.isCorrect(userResponse)) {
//                 totalMarks++;
//             }
//         }
//         // Display total marks
//         System.out.println("Total Marks: " + totalMarks);
//         scanner.close();
//     }
// }

// ===================================================================
// import javax.swing.JFileChooser;
// import javax.swing.JFrame;

// public class Main {
//     public static void main(String[] args){
//         JFrame frame = new JFrame("Save Dialog Example");
//         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//         // Create a file chooser
//         JFileChooser fileChooser = new JFileChooser();
//         // Show save dialog
//         int userSelection = fileChooser.showSaveDialog(frame);

//         if (userSelection == JFileChooser.APPROVE_OPTION) {
//             java.io.File fileToSave = fileChooser.getSelectedFile(); // Get the selected file
//             // Perform save operation (in this example, just print the selected file path)
//             System.out.println("Save to file: " + fileToSave.getAbsolutePath());
//         } 
//         else {
//             System.out.println("Save dialog canceled.");
//         }
//         frame.setSize(300, 200);
//         frame.setVisible(true);
//     }
// }

// ===================================================================
// import java.io.*;
// import java.net.URL;
// import java.net.URLConnection;

// public class Main {
//     public static void main(String[] args) 
//     // Try block to check for exceptions 
//     throws Exception{
//         try { 
//             URL u = new URL("www.geeksforgeeks.com"); 
//             // Creating an object of URLConnection class to communicate between application and URL 
//             URLConnection urlconnect = u.openConnection(); 
//             // Creating an object of InputStream class for our application streams to be read 
//             InputStream stream = urlconnect.getInputStream();  
//             int i; 
//             // Till the time URL is being read Continue printing the stream 
//             while ((i = stream.read()) != -1) { 
//                 System.out.print((char)i); 
//             } 
//         }
//         // Catch block to handle the exception 
//         catch (Exception e) {  
//             System.out.println(e); 
//         }
//     }
// }

// ===================================================================
// import java.util.LinkedList;

// public class Main {
//     public static void main(String[] args) throws InterruptedException {
//         // Object of a class that has both produce() and consume() methods
//         final PC pc = new PC();
//         Thread t1 = new Thread(new Runnable() { // Create producer thread
//             @Override
//             public void run() {
//                 try {
//                     pc.produce();
//                 }
//                 catch (InterruptedException e) {
//                     e.printStackTrace();
//                 }
//             }
//         });
//         Thread t2 = new Thread(new Runnable() { // Create consumer thread
//             @Override
//             public void run() {
//                 try {
//                     pc.consume();
//                 }
//                 catch (InterruptedException e) {
//                     e.printStackTrace();
//                 }
//             }
//         });
//         // Start both threads
//         t1.start();
//         t2.start();
//         // t1 finishes before t2 
//         t1.join();
//         t2.join();
//     }
//     // This class has a list, producer (adds items to list) and consumer (removes items).
//     public static class PC { 
//         // Create a list shared by producer and consumer  Size of list is 2. 
//         LinkedList<Integer> list = new LinkedList<>(); 
//         int capacity = 2; 
//         public void produce() throws InterruptedException{ // Function called by producer thread
//             int value = 0; 
//             while (true) { 
//                 synchronized (this) 
//                 {  
//                     while (list.size() == capacity)// producer thread waits while list is full
//                     wait();
//                     System.out.println("Producer produced-" + value);  
//                     list.add(value++); // to insert the jobs in the list
//                     notify(); // notifies the consumer thread that now it can start consuming
//                     Thread.sleep(1000); 
//                 } 
//             } 
//         }
//         public void consume() throws InterruptedException{ // Function called by consumer thread 
//             while (true) { 
//                 synchronized (this){ 
//                     while (list.size() == 0) // consumer thread waits while list is empty 
//                     wait();  
//                     int val = list.removeFirst(); // to retrieve the first job in the list
//                     System.out.println("Consumer consumed-" + val); 
//                     notify(); // Wake up producer thread 
//                     Thread.sleep(1000); // and sleep 
//                 } 
//             } 
//         }
//     }
// }

// ===================================================================
// import java.util.Scanner;
// // Driver Class
// class Main {
//     public static boolean isPalindrome(String str){  
//         String rev = ""; //to store the reverse of the original str 
//         boolean ans = false; 
//         for (int i = str.length() - 1; i >= 0; i--) { 
//             rev = rev + str.charAt(i); 
//         }
//         if (str.equals(rev)) { 
//             ans = true; 
//         } 
//         return ans; 
//     }
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         System.out.println("Enter a string: ");
//         String str = scanner.nextLine();
//         // Convert the string to lowercase 
//         str = str.toLowerCase(); boolean A = isPalindrome(str);
//         System.out.println(A);
//         scanner.close();
//     }
// }

// ===================================================================

// class Main {
//     static void prime_N(int N)
//     {
//         int x, y, flag;
//         System.out.println("All the Prime numbers within 1 and " + N + " are:");
//         for (x = 1; x <= N; x++) {
//             if (x == 1 || x == 0) //as 0 and 1 are neither prime nor composite
//                 continue;
//             flag = 1; // Using flag variable to check if x is prime or not 
//             for (y = 2; y <= x / 2; ++y) {
//                 if (x % y == 0) {
//                     flag = 0;
//                     break;
//                 }
//             }
//             if (flag == 1)
//                 System.out.print(x + " ");
//         }
//     }
//     public static void main(String[] args)
//     {
//         int N = 45;
//         prime_N(N);
//     }
// }

// ===================================================================

// import java.util.Scanner;
// public class Main {
//     public static void main(String[] Strings) { 
//         Scanner input = new Scanner(System.in); 
//         System.out.print("Enter the value of a: "); 
//         double a = input.nextDouble(); 
//         System.out.print("Enter the value of b: "); 
//         double b = input.nextDouble(); 
//         System.out.print("Enter the value of c: "); 
//         double c = input.nextDouble(); 

//         double d = b * b -4.0 * a * c; 
//         if (d > 0.0) { 
//             double r1 = (-b + Math.pow(d, 0.5)) / (2.0 * a); 
//             double r2 = (-b - Math.pow(d, 0.5)) / (2.0 * a); 
//             System.out.println("The roots are " + r1 + " and " + r2); 
//         } 
//         else if (d == 0.0) { 
//             double r1 = -b / (2.0 * a); 
//             System.out.println("The root is " + r1); 
//         } 
//         else 
//         { 
//             System.out.println("Roots are not real."); 
//         }
//         input.close(); 
//     }
// }

// ===================================================================

// class Main {
//     public static void main(String[] args) {
//         int n = 4;
//         String names[] = { "Rahul", "Ajay", "Gourav", "Riya" };
//         String temp;
//         for (int i = 0; i < n; i++) {
//             for (int j = i + 1; j < n; j++) {
//                 if (names[i].compareTo(names[j]) > 0) { 
//                     temp = names[i]; // swapping
//                     names[i] = names[j];
//                     names[j] = temp;
//                 }
//             }
//         }
//         // print output array
//         System.out.println("The names in assending order are: ");
//         for (int i = 0; i < n; i++) {
//             System.out.println(names[i]);
//         }
//     }
// }

// ===================================================================

// import java.util.Scanner;
// public class Main {

//     private static boolean isVowel(char ch) {
//         ch = Character.toLowerCase(ch);
//         return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
//     }
//     private static void countCharacters(String word) {
//         int vowelCount = 0, consonantCount = 0, digitCount = 0, specialCount = 0;
//         for (char ch : word.toCharArray()) { //process each char in a word
//             if (Character.isLetter(ch)) {
//                 // Check for vowels and consonants
//                 if (isVowel(ch)) {
//                     vowelCount++;
//                 } else {
//                     consonantCount++;
//                 }
//             } else if (Character.isDigit(ch)) {
//                 digitCount++;
//             } else {
//                 specialCount++;
//             }
//         }
//         System.out.println("Word: " + word);
//         System.out.println("Vowels: " + vowelCount);
//         System.out.println("Consonants: " + consonantCount);
//         System.out.println("Digits: " + digitCount);
//         System.out.println("Special Characters: " + specialCount);
//         System.out.println("----------------------");
//     }
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         System.out.print("Enter a string: ");
//         String input = scanner.nextLine();

//         String[] words = input.split("\\s+"); //process each word
//         for (String word : words) {
//             countCharacters(word);
//         }
//         scanner.close();
//     }
// }

// ===================================================================

// import java.util.StringTokenizer;
// import java.text.SimpleDateFormat;
// import java.util.Date;
// import java.util.Scanner;

// public class Main {
//     private static boolean isTimeBetween(int currentHours, int currentMinutes, int startHours, int startMinutes, int endHours, int endMinutes) {
//         if (currentHours > startHours && currentHours < endHours) {
//             return true;
//         } else if (currentHours == startHours && currentMinutes >= startMinutes) {
//             return true;
//         } else return currentHours == endHours && currentMinutes <= endMinutes;
//     }
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         // Get time intervals from the user
//         System.out.print("Enter start time (hh:mm): ");
//         String startTimeInput = scanner.nextLine();
//         System.out.print("Enter end time (hh:mm): ");
//         String endTimeInput = scanner.nextLine();

//         // Parse time intervals using StringTokenizer
//         StringTokenizer startTokenizer = new StringTokenizer(startTimeInput, ":");
//         int startHours = Integer.parseInt(startTokenizer.nextToken());
//         int startMinutes = Integer.parseInt(startTokenizer.nextToken());

//         StringTokenizer endTokenizer = new StringTokenizer(endTimeInput, ":");
//         int endHours = Integer.parseInt(endTokenizer.nextToken());
//         int endMinutes = Integer.parseInt(endTokenizer.nextToken());

//         // Get current system time
//         Date currentDate = new Date();
//         SimpleDateFormat dateFormat = new SimpleDateFormat("hh:mm");
//         String currentTime = dateFormat.format(currentDate);

//         // Parse current time using StringTokenizer
//         StringTokenizer currentTokenizer = new StringTokenizer(currentTime, ":");
//         int currentHours = Integer.parseInt(currentTokenizer.nextToken());
//         int currentMinutes = Integer.parseInt(currentTokenizer.nextToken());
//         System.out.println("Current time is: "+currentHours+":"+currentMinutes);
//         // Compare time intervals
//         if (isTimeBetween(currentHours, currentMinutes, startHours, startMinutes, endHours, endMinutes)) {
//             System.out.println("Correct time! The current time is between " + startTimeInput + " and " + endTimeInput);
//         } else {
//             System.out.println("Incorrect time. Try again.");
//         }

//         scanner.close();
//     }

// }

// ===================================================================

// public class Main {
//     public static void main(String[] args) {
//         int num = 5;
//         long factorial = 1;
//         for (int i = 1; i <= num; ++i) {
//             factorial = factorial * i;
//         }
//         System.out.printf("Factorial of %d = %d", num, factorial);
//     }
// }

// ===================================================================
