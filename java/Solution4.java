public class Solution4 {
    public static void main(String[] args) {
        int a = 100;
        int b = 20;
        int c = 300;
        int d = 4;
        int result = outOfFour(a,b,c,d);
        System.out.println(result);
    }
    public static int outOfFour(int a, int b, int c, int d){
        return a>b? (a>c? (a>d? a:d) : (a>d? c:(d>c? d:c))) : (b>c? (b>d? b:d) : (b>d? c:(d>c? d:c)));
    }
}
