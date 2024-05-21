import java.util.*;

class Grain{
    private int id;
    private String name;
    private String state;
    private int quantity;
    
    public Grain(int id, String name, String state, int quantity) {
        this.id = id;
        this.name = name;
        this.state = state;
        this.quantity = quantity;
    }
    public int getId(){
        return this.getId();
    }
    public String getName(){
        return this.name;
    }
    public String getState(){
        return this.state;
    }
    public int getQuantity(){
        return quantity;
    }
    public String toString(){
        return "id-" + id + "\nname-"+name+ "\nquantity-"+quantity ;
    }
}
public class Solution2 {
    @SuppressWarnings({ "unused", "resource" })
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.err.print("Enter no of grains: ");
        int noOfGrains = sc.nextInt();
        Grain[] grains = new Grain[noOfGrains];

        for (int i=0; i<noOfGrains; i++){
            int id = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            String state = sc.nextLine();
            int quantity = sc.nextInt();
            sc.nextLine();
            grains[i] = new Grain(id, name, state, quantity);
        }
        System.out.print("Enter name of grain: ");
        String grainSearch = sc.nextLine();
    }
}
