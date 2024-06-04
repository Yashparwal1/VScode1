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
//         System.out.println(Sum.Result(num));
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

import java.util.*;

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

        Arrays.sort(filteredPlayers, new Comparator<Player>() {
            @Override
            public int compare(Player p1, Player p2) {
                // Sorting in descending order
                return Integer.compare(p2.getId(), p1.getId());
            }
        });
        
        
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