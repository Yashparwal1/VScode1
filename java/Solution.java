import java.util.*;

class Bike{
    private int id;
    private int quantity;
    private String name;
    private int price;
    
    public Bike(int id, int quantity, String name, int price){
        this.id = id;
        this.quantity = quantity;
        this.name = name;
        this.price = price;
    }
    public int getId(){
        return this.id;
    }
    public int getQuantity(){
        return this.quantity;
    }
    public int getPrice(){
        return this.price;
    } 
    public String getName(){
        return this.name;
    }
    public String toString(){
        return "id-" + id + "\nquantity-"+quantity + "\nname-"+name+ "\nprice-"+price;
    }
}

public class Solution {
    public static Bike findMaxPriceOfBike(Bike[] bikes){
        Bike maxPriceBike = bikes[0];
// for each loop -- bike is temp var of same type as of bikes array followed by colon and array bikes
        for (Bike bike:bikes){
            if (bike.getPrice() > maxPriceBike.getPrice()){
                maxPriceBike = bike;
            }
        }
        return maxPriceBike;
    }
    public static Bike searchBikeByName(Bike[] bikes, String name){
        for(Bike bike:bikes){
            if(bike.getName().equalsIgnoreCase(name)){
                return bike;
            }
        }
        return null;
    }
    
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner sc = new Scanner(System.in);
        int noOfBikes = sc.nextInt();
        Bike[] bikes = new Bike[noOfBikes];
        for (int i = 0; i < noOfBikes; i++) {
            int id = sc.nextInt();
            sc.nextLine();
            int quantity = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            int price = sc.nextInt();
            sc.nextLine();   
            bikes[i] = new Bike(id, quantity, name, price); 
        } 
           
        String searchName = sc.nextLine();
        sc.close();
        // for (int i = 0; i < bikes.length; i++) {
        //     System.out.println("here:"+bikes[i]);
        // }
        // System.out.println("till here");
        Bike maxPriceBike = findMaxPriceOfBike(bikes);
        if (maxPriceBike != null){
            System.out.println(maxPriceBike);
        }
        else{
            System.out.println(0);
        }
        
        Bike searchBike = searchBikeByName(bikes, searchName);
        if (searchBike != null){
            System.out.println(searchBike);
        }
        else{
            System.out.println("No Bike found with mentioned attribute");
        }
    }
    
}