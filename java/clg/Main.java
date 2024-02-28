package clg;

abstract class Shape {
    private double wd;
    private double ht;
    public Shape(double width, double height){ //constructor
        this.wd = width;
        this.ht = height;
    }   

    public final double getWidth(){ //cannot be overridden due to final, so no inheritence
        return wd;
    }
    public final double getHeight(){ //cannot be overridden due to final, so no inheritance
        return ht;
    }
    abstract double getArea(); //will be defined in child class like get area of which shape, rect, sq etc 

}

class Rectangle extends Shape{
    public Rectangle(double width, double height){
        super(width,height); //calling parent's constructor 
    }

    @Override
    final double getArea(){
        return this.getWidth()*getHeight();
    }
}
class Square extends Shape{
    public Square(double side){
        super(side,side); //calling parent's constructor 
    }

    @Override
    final double getArea(){
        return this.getWidth()*getHeight(); //wd and ht is same, so side*side
    }
}

class Main{
    public static void main(String[] args) {
        // create and new Rectangle object and assigns it to the var s1. Rectangle class is a subclss of Shape, so the s1 var can be used to refer to the Rectangle object 
        Shape s1 = new Rectangle(6.3, 5.2);
        Shape s2 = new Square(4.6);

        //we have to use contatination in println, or use printf for "something",s1.getArea() but concat. is slower :)
        // System.out.println("Area of rectange is: ",s1.getArea()); 
        System.out.println("Area of rectangle is: "+s1.getArea());
        System.out.println("Area of square is: "+s2.getArea());

    } 
}