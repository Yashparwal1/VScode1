// Solution 3 -- take 3 ponints with coordinates, find highest distance from origin for each point and print it.

import java.util.*;
/* 
class Point {
    double x;
    double y;
    
    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    // int getX(){
    // return x;
    // }
    // int getY(){
        // return y;
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
        Point distance = highestDestanceFromOrigin(p1, p2, p3);
        // System.out.println(distance); // Point@hexno
        System.out.println(distance.x + "," + distance.y);
    }

    public static Point highestDestanceFromOrigin(Point p1, Point p2, Point p3) {
        double d1 = Math.sqrt(p1.x * p1.x + p1.y + p1.y); // squrt((x2-x1)^2 + (y2-y1)^2) [origin is 0,0]
        double d2 = Math.sqrt(p2.x * p2.x + p2.y * p2.y); // so this will be squrt(x2^2 + y2^2)
        double d3 = Math.sqrt(p3.x * p3.x + p3.y * p3.y);
        
        // conditional statement
        // return d1>d2?(d1>d3?p1:p3):(d2>d3?p2:p3);
        // using if-else
        if (d1 > d2) {
            if (d1 > d3) {
                return p1;
            } else {
                return p3;
            }
        } else {
            if (d2 > d3) {
                return p2;
            } else {
                return p3;
            }
        }
    }
}
 */

// ================================distance b/w two points======================================================
// import java.io.*;
// import java.util.*;
// import java.text.*;
// import java.math.*;
// import java.lang.*;
// import java.util.regex.*;

// public class Solution {
//     public static void main(String args[] ) throws Exception {
//         Scanner sc = new Scanner(System.in);
//         double x1 = sc.nextInt();
//         double y1 = sc.nextInt();
//         double x2 = sc.nextInt();
//         double y2 = sc.nextInt();
//         Point p1 = new Point(x1, y1);
//         Point p2 = new Point(x2, y2);
//         double distance = findDistance(p1, p2);
//         System.out.println(String.format("%.3f",distance));
//     }

//     public static double findDistance(Point p1, Point p2)
//     {
//        double distance = Math.sqrt(Math.pow(p2.x-p1.x,2) + Math.pow(p2.y-p1.y,2));
//        return distance;
//     }
// }

// class Point
// {
//     double x;
//     double y;
//     Point(double x, double y){
//         this.x = x;
//         this.y = y;
//     }
// }
// ==================================================================================================

// Solution 4 -- take an integer as input. calculate the sum of its digits. if sum is div by 3. then print true else print false.

// import java.util.*;

// class Sum{
//     public static int Result(int num){
//         int sum = 0;
//         int digit;
//         while (num!=0) {
//             digit = num % 10;
//             sum = sum+digit;
//             num = num/10;
//         }
//         return sum;
//     }
// }

// class Main{
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter a number: ");
//         int num = sc.nextInt();
//         sc.close();
//         int sum = Sum.Result(num);
//         System.out.println(sum%3==0?"TRUE":"FALSE");
//     }

// }

// ==================================================================================================
// avg of numbers in an array between given limits

// class Main{
//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         int digit[] = new int[5];
//         for(int i=0; i<5; i++){
//             System.out.println(i+1+": ");
//             int num = sc.nextInt();
//             digit[i] = num;
//         }
//         System.out.println("limits");
//         int limit1 = sc.nextInt();
//         int limit2 = sc.nextInt();
//         int sum = 0; 
//         int count=0;
//         for (int i : digit) {
//             if (i>limit1 && i<limit2){
//                 sum = sum+i;
//                 count++;
//             }
//         }
//         // for(int i = 0; i>limit1&&i<limit2;){
//         //     sum  = sum+i;
//         //     count++;
//         // }
//         System.out.println(sum/count);
//     }
// }

// ===============================================================================
/* 
class Player {
    private int playerId;
    private String playerName;
    private int runs;
    private String playerType;
    private String playerMatch;

    public Player(int id, String name, int run, String type, String match) {
        this.playerId = id;
        this.playerName = name;
        this.runs = run;
        this.playerType = type;
        this.playerMatch = match;
    }

    public int getId() {
        return this.playerId;
    }

    public String getName(){
        return this.playerName;
    }

    public int getRuns() {
        return this.runs;
    }

    public String getType() {
        return this.playerType;
    }

    public String getMatch() {
        return this.playerMatch;
    }
    // public String toString(){
    //     return "id-" + playerId + "\nname-"+playerName + "\nruns-"+runs+ "\ntype-"+playerType+ "\nmatch-"+playerMatch;
    // }
}

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Player[] players = new Player[2];
        for (int i = 0; i < players.length; i++) {
            System.out.print("Id: ");
            int id = sc.nextInt();
            sc.nextLine();
            System.out.print("name: ");
            String name = sc.nextLine();
            System.out.print("Runs: ");
            int run = sc.nextInt();
            sc.nextLine();
            System.out.print("Type: ");
            String type = sc.nextLine();
            System.out.print("Match: ");
            String match = sc.nextLine();
            players[i] = new Player(id, name, run, type, match);
        }
        System.out.println("Type for func1:");
        String type = sc.nextLine();
        System.out.println("Match for func2:");
        String match = sc.nextLine();

        int runs =  findPlayerWithLowestRuns(players, type);
        System.out.println(runs>0?runs:"No such player");
        
        Player[] result = findPlayerWithMatchType(players, match);
        if (result != null) {
            for (Player p:result) {
                System.out.println(p.getId());
            }
        } 
        else {
            System.out.println("No Player with given matchType");
        }
    }

    public static int findPlayerWithLowestRuns(Player[] players, String type) {
        // int valid = 0;
        // int index = 0;
        // Player temp;
        int tempRuns = 0;
        for (Player p : players) {
            // System.out.println(p.getType());
            if (p.getType().equalsIgnoreCase(type)) {
                if (p.getRuns() < tempRuns){
                    tempRuns = p.getRuns();
                    System.out.println("in if part"+p.getRuns());
                }
                else{            
                    tempRuns = p.getRuns();
                    System.out.println("in else part"+p.getRuns());
                }
            }
        }
        return tempRuns;

    }

    public static Player[] findPlayerWithMatchType(Player[] players, String match) {
        int count = 0;
        for (Player player : players) {
            if (player.getMatch().equals(match)) {
                count++;
            }
        }
        if (count == 0) {
            return null;
        }
        Player[] filteredPlayers = new Player[count];
        int index = 0;
        for (Player player : players) {
            if (player.getMatch().equals(match)) {
                filteredPlayers[index++] = player;
            }
        }

        //sorting acc. to id

        // Arrays.sort(filteredPlayers, new Comparator<Player>() {
        //     @Override
        //     public int compare(Player p1, Player p2) {
        //         // Sorting in descending order
        //         return Integer.compare(p2.getId(), p1.getId());
        //     }
        // });

        
        Player temp = null;
        for (int i = 0; i < filteredPlayers.length; i++) {
            for (int j = i+1; j < filteredPlayers.length; j++) {
                if (filteredPlayers[i].getId()<filteredPlayers[j].getId()) {
                    temp = filteredPlayers[i];
                    filteredPlayers[i] = filteredPlayers[j];
                    filteredPlayers[j] = temp;
                }
            }
        }

        return filteredPlayers;
    }
} 
*/

// ==================================================================================================

// class Solution3{
//   public static void main(String[] args){
//     Scanner sc = new Scanner(System.in);
//     int num = sc.nextInt();
//     int sum = 0;
//     while(num!=0){
//         sum = sum+(num%10);
//         num = num/10;
//     }
//     if(sum%3==0){
//         System.out.println("TRUE");
//     }else{
//         System.out.println("FALSE");
//     }
//     sc.close();
//   }
// }  
// ============================================================================================
/* 
123 
HP
Windows
35000
5
124
Apple 
Mac OS
70000
5
125
Dell
Ubuntu
30000
4
126
HP
windows
40000
4
HP
windows
*/

class Laptop {
    private int laptopId;
    private String brand;
    private String osType;
    private double price;
    private int rating;

    Laptop(int id, String brand, String os, double price, int rating) {
        this.laptopId = id;
        this.brand = brand;
        this.osType = os;
        this.price = price;
        this.rating = rating;
    }

    public int getId() {
        return this.laptopId;
    }

    public String getBrand() {
        return this.brand;
    }
    public String getOs(){
        return this.osType;
    }
    public int getRating() {
        return this.rating;
    }
    @Override
    public String toString() {
        return this.laptopId + "\n" + this.rating;
    }

}

class Solution3 {
    public static void main(String[] args) {
        System.out.println("hello world");
        Scanner sc = new Scanner(System.in);
        Laptop[] laptops = new Laptop[4];
        for (int i = 0; i < laptops.length; i++) {
            int id = sc.nextInt();
            sc.nextLine();
            String brand = sc.nextLine();
            String os = sc.nextLine();
            double price = sc.nextDouble();
            int rating = sc.nextInt();
            sc.nextLine();
            laptops[i] = new Laptop(id, brand, os, price, rating);
        }

        String searchBrand = sc.nextLine();
        String searchOs = sc.nextLine();

        // for (Laptop laptop : laptops) {
        // System.out.println("Laptop ID: " + laptop.getId() + ", Brand: " +
        // laptop.getBrand() + ", Rating: " + laptop.getRating());
        // }
        System.out.println("--------");
        int result = countOfLaptopByBrand(laptops, searchBrand);
        System.out.println(result == 0 ? 0 : result);
        Laptop[] result2 = searchLaptopByOsType(laptops, searchOs);
        if(result2 != null){
            for(Laptop laptop:result2){
              System.out.println(laptop);
            }
        }
        else{
              System.out.println("This given os is not available");
        }
    }

    public static int countOfLaptopByBrand(Laptop[] laptops, String searchBrand) {
        int count = 0;
        for (Laptop laptop : laptops) {
            if (laptop.getBrand().equals(searchBrand) && laptop.getRating() > 3) {
                count++;
            }
        }
        return count;
    }

    public static Laptop[] searchLaptopByOsType(Laptop[] laptops, String searchOs) {

        int count = 0;
        for (Laptop l : laptops) {
            if (l.getOs().equalsIgnoreCase(searchOs)) {
                count++;
            }
        }
        if (count == 0) {
            return null;
        }

        Laptop[] filteredLaptops = new Laptop[count];
        int index = 0;
        for (Laptop laptop : laptops) {
            if (laptop.getOs().equalsIgnoreCase(searchOs)) {
                filteredLaptops[index++] = laptop;
            }
        }
        Laptop temp = null;
        for (int i = 0; i < filteredLaptops.length; i++) {
            for (int j = i + 1; j < filteredLaptops.length; j++) {
                if (filteredLaptops[i].getId()<filteredLaptops[j].getId()){
                    temp = filteredLaptops[i];
                    filteredLaptops[i] = filteredLaptops[j];
                    filteredLaptops[j] = temp;
                }
            }
        }
        return filteredLaptops;
        
        // Laptop[] filteredLaptops = Arrays.stream(laptops)
        //                                  .filter(l -> l.getOs().equalsIgnoreCase(searchOs))
        //                                  .toArray(Laptop[]::new);

        // if (filteredLaptops.length == 0) {
        //     return null;
        // }

        // // Sort the filtered laptops in descending order of laptopId
        // Arrays.sort(filteredLaptops, (l1, l2) -> Integer.compare(l2.getId(), l1.getId()));

        // return filteredLaptops;
    }
}

// ============================================================================================


// ================================================================================================

// import java.util.*;

// class Solution3{
//   public static void main(String[] args){
//     Scanner sc = new Scanner(System.in);
//     int[] nums = new int[5];
//     int sum = 0;
//     for(int i=0; i<nums.length; i++){
//       int num = sc.nextInt();
//       nums[i] = num;
//       if(num%2!=0){
//         sum = sum+num;
//       }
//     }
//     if(sum>8 && sum<50){
//       System.out.println("Sum of odd numbers:"+sum);
//     }
//   }
// }

// ================================================================================================
/* 
101
Best Stay
01-jan-2022
10
Yes
20000
102
Apple Stay
12-Feb-2022
3
Yes
4000
103
Accord
11-May-2022
5
Yes
15000
104
Royal Park
22-Dec-2021
7
Yes
12000
May
Yes
 */
// class Hotel {
//     private int hotelId;
//     private String hotelName;
//     private String dateOfBooking;
//     private int noOfRoomsBooked;
//     private String wifiFacility;
//     private double totalBill;

//     Hotel(int id, String name, String date, int rooms, String wifi, double bill) {
//         this.hotelId = id;
//         this.hotelName = name;
//         this.dateOfBooking = date;
//         this.noOfRoomsBooked = rooms;
//         this.wifiFacility = wifi;
//         this.totalBill = bill;
//     }

//     public int getId(){
//         return this.hotelId;
//     }
//     public String getDate() {
//         return this.dateOfBooking;
//     }

//     public int getRooms() {
//         return this.noOfRoomsBooked;
//     }

//     public String getWifi() {
//         return this.wifiFacility;
//     }
//     public double getBill(){
//         return this.totalBill;
//     }
// }

// class Solution3{
//   public static void main(String[] args){
//     Scanner sc = new Scanner(System.in);
//     Hotel[] hotels = new Hotel[4];
//     for(int i=0; i<hotels.length; i++){
//       int id = sc.nextInt();
//       sc.nextLine();
//       String name = sc.nextLine();
//       String date = sc.nextLine();
//       int rooms = sc.nextInt();
//       sc.nextLine();
//       String wifi = sc.nextLine();
//       double bill = sc.nextDouble();
//       hotels[i] = new Hotel(id,name,date,rooms,wifi,bill);
//     }
//     sc.nextLine();
//     // System.out.println("month: ");
//     String month = sc.nextLine();
//     // System.out.println("wifi?: ");
//     String wifiOption = sc.nextLine();
    
//     int result = noOfRoomsBookedInGivenMonth(hotels, month);
//     System.out.println(result!=0?result:"No rooms booked in the given month");
//     Hotel result2 = searchHotelByWifiOption(hotels, wifiOption);
//     System.out.println(result2.getId());
//   }

//     public static int noOfRoomsBookedInGivenMonth(Hotel[] hotels, String month) {
//         int count = 0;
//         for (Hotel h : hotels) {
//             // String[] parts = h.getDate().split(month, '-');
//             // System.out.println(parts[1]);
//             if(h.getDate().substring(3,6).equals(month)) {
//                 // System.out.println("true");
//                 count += h.getRooms();
//             }
//         }
//         return count;
//     }

//     public static Hotel searchHotelByWifiOption(Hotel[] hotels, String wifiOption) {
//         Hotel highestBillHotel = null;
//         Hotel secondHighestBillHotel = null;

//         for (Hotel hotel : hotels) {
//             if (hotel.getWifi().equals(wifiOption)) {
//                 if (highestBillHotel == null || hotel.getBill() > highestBillHotel.getBill()) {
//                     secondHighestBillHotel = highestBillHotel;
//                     highestBillHotel = hotel;
//                 } 
//                     else if (secondHighestBillHotel == null || hotel.getBill() > secondHighestBillHotel.getBill()) {
//                     secondHighestBillHotel = hotel;
//                 }
//             }
//         }

//         return secondHighestBillHotel;
//     }
// }

// ===================================================================================

// Write a method calculateInterest which will take account object and no of years as input parameters and return the interest amount. For specified no of years, first find out the percentage value those no of years based on specified interestRate. E.g. if no of years is 5 and specified interestRate is 4%, then 4% of 5 is 0.2. This percentage should be added to original interstRate for calculating the final interest value. Hence for above example it will be 4.2 (instead of 4). Display the interest amount rounded upto three decimal places. Even if the result does not have decimal, it should be displayed with suffix ".000".
/* 
class Account{
    int id;
    double balance, interestRate;
    Account(int id, double bal, double rate){
        this.id = id;
        this.balance = bal;
        this.interestRate = rate;
    }
    public int getId() {
        return this.id;
    }
    public double getInterestRate(){
        return this.interestRate;
    }
    public double getBalance(){
        return this.balance;
    }
}
public class Solution3 {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int id = sc.nextInt();
        double bal = sc.nextDouble();
        double rate = sc.nextDouble();
        Account acc = new Account(id,bal,rate);
        int noOfYear = sc.nextInt();
        double result = calculateInterest(acc, noOfYear);
        System.out.format("%.3f",result);
    }
    public static double calculateInterest(Account acc, int years){
        double temp = years * acc.getInterestRate() / 100;
        return (acc.getBalance() * (acc.getInterestRate()+temp) / 100);
    }
}
*/

// =============================================================================================================

/* 
Sample Input 1
4
5678
6
MarutiAlto
600000
9843
9
SwiftDzire
900000
3244
3
ToyotoLiva
670000
3333
7
Bolero
1100000
Bolero
*/

/* 
class Car{
    int carNumber;
    int carQuantity;
    String carModel;
    int carOnroadprice;
    Car(int no, int q, String model, int price){
        this.carNumber = no;
        this.carQuantity = q;
        this.carModel = model;
        this.carOnroadprice = price;
    }
    public int getPrice(){
        return this.carOnroadprice;
    }
    public String getModel(){
        return this.carModel;
    }
    public String toString(){
        return "CarNumber-"+carNumber+"\nCarQuantity-"+carQuantity+"\nCarModel-"+carModel+"\nCarOnRoadPrice-"+carOnroadprice;
    }
}
public class Solution3 {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int noOfCars = sc.nextInt();
        Car[] cars = new Car[noOfCars];
        for (int i = 0; i < noOfCars; i++) {
            int no = sc.nextInt();
            sc.nextLine();
            int q = sc.nextInt();
            sc.nextLine();
            String model = sc.nextLine();
            int price = sc.nextInt();
            sc.nextLine();
            cars[i] = new Car(no, q, model, price);
        }
        String searchModel = sc.nextLine();
        Car result = findMinOnRoadPrice(cars);
        System.out.println(result!=null?result:"No Car found with mentioned attribute");
        // **** we can print object directly BUT toString method should be there in class ****

        Car[] result2 = searchCarModel(cars, searchModel);
        if (result2!=null) {
            for (Car car : result2) {
                System.out.println(car);
            }
        }
        else{
            System.out.println("No Car found with mentioned attribute");
        }
    }
    public static Car findMinOnRoadPrice(Car[] cars){
        Car minPrice = cars[0];
        for (Car c : cars) {
            if(c.getPrice()<minPrice.getPrice()){
                minPrice = c;
            }
        }
        return minPrice;
    }
    public static Car[] searchCarModel(Car[] cars, String searchModel){
        int count = 0;
        for (Car car : cars) {
            if (car.getModel().equals(searchModel)) {
                count++;
                // return car;
            }
        }
        
        if (count==0) {
            return null;
        }
        Car[] result = new Car[count];
        int i = 0;
        for (Car car : cars) {
            if (car.getModel().equals(searchModel)){
                result[i++] = car;
            }
        }
        return result;
    }
}
*/

// ==========================================================================================================

/*
4
111
Biryani
NonVeg
400
112
Shawarma
NonVeg
100
113
Poha
Veg
40
114
Upma
Veg
50
Veg
*/

// class Food{
//     private int FoodId;
//     private String FoodName;
//     private String FoodCategory;
//     private int FoodCost;

//     Food(int id, String name, String cat, int cost){
//         this.FoodId = id;
//         this.FoodName = name;
//         this.FoodCategory = cat;
//         this.FoodCost = cost;
//     }
//     public String getCat(){
//         return this.FoodCategory;
//     }
//     public int getCost(){
//         return this.FoodCost;
//     }
//     @Override
//     public String toString(){
//         return FoodId+"\n"+FoodName+"\n"+FoodCategory+"\n"+FoodCost;
//     }
// }

// class Solution3{
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int noOfFood = sc.nextInt();
//         Food[] food = new Food[noOfFood];
//         for (int i = 0; i < 4; i++) {
//             int id = sc.nextInt();
//             sc.nextLine();
//             String name = sc.nextLine();
//             String cat = sc.nextLine();
//             int cost = sc.nextInt();
//             sc.nextLine();
//             food[i] = new Food(id, name, cat, cost);
//         }
//         String category = sc.nextLine();
//         int result = countFoodByGivenCategory(food, category); 
//         System.out.println(result!=0?result:"No Food with the given category are found");
//         Food result2 = getFoodWithMinCost(food);
//         System.out.println(result2!=null?result2:"No food found");
//     }

//     public static int countFoodByGivenCategory(Food[] food, String category){
//         int count=0;
//         for (Food f : food) {
//             if (f.getCat().equals(category)){
//                 count++;
//             }
//         }
//         return count;
//     }
//     public static Food getFoodWithMinCost(Food[] food){
//         Food temp = food[0];
//         for (Food f : food) {
//             if (f.getCost()<temp.getCost()) {
//                 temp = f;
//             }
//         }
//         return temp;
//     }

//     // public static void Hello(){
//     //     Food temp = new Food;
//     // }
// }





// =====================================My IPA Question==========================================================

/* INPUTS
4
1001
A
50000
4
TataCliq
1002
B
90000
2
Epson
1003
C
60000
5
TataCliq
1004
D
100000
3
TataCliq
3
 */

/* class Projector{
    private int projectorId;
    private String projectorName;
    private int price;
    private int rating;
    private String availableIn;

    Projector(int id, String name, int price, int rating, String aval){
        this.projectorId = id;
        this.projectorName = name;
        this.price = price;
        this.rating = rating;
        this.availableIn = aval;
    }
    public int getId(){
        return this.projectorId;
    }
    public int getPrice(){
        return this.price;
    }
    public int getRating(){
        return this.rating;
    }
    public String getAval(){
        return this.availableIn;
    }
    @Override
    public String toString(){
        return this.projectorId+"\n"+this.projectorName+"\n"+this.price+"\n"+this.rating+"\n"+this.availableIn;
    }
}

class Solution3{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int noOfProjevtors = sc.nextInt();
        Projector[] projectors = new Projector[4];
        for (int i = 0; i < 4; i++) {
            // System.out.print("Id: ");
            int id = sc.nextInt();
            sc.nextLine();
            // sc.nextLine();
            // System.out.print("Name: ");
            String name = sc.nextLine();
            // System.out.print("Price: ");
            int price = sc.nextInt();
            sc.nextLine();
            // System.out.print("Rating: ");
            int rating = sc.nextInt();
            sc.nextLine();
            // System.out.print("Available in: ");
            String aval = sc.nextLine();
            // sc.nextLine();
            projectors[i] = new Projector(id, name, price, rating, aval);
        }
        System.out.println("here");
        // sc.nextLine();
        int searchRating = sc.nextInt();
        Projector result = getMaxPriceByRatinng(projectors, searchRating);
        if (result!=null) {
            System.out.println(result.getId());

            // when we return Projector[] then treat result as array
            // for (int i = 0; i < result.length; i++) {
            //     System.out.println(result[i]);    
            // }
            // System.out.println(result[0].getId());
        }
    }
    public static Projector getMaxPriceByRatinng(Projector[] projectors, int searchRating){
        int count = 0;
        for (Projector p : projectors) {
            if (p.getRating()>searchRating && p.getAval().equals("TataCliq")) {
                count++;
            }
        }
        if(count==0){return null;}
        Projector[] temp = new Projector[count];
        int i = 0;
        for (Projector p : projectors) {
            if (p.getRating()>searchRating && p.getAval().equals("TataCliq")) {
                temp[i++] = p;
            }
        }
        Projector tempP = temp[0];
        for (Projector p : temp) {
            if (p.getPrice()>tempP.getPrice()) {
                tempP = p;
            }
        }
        return tempP;  
    }
} */