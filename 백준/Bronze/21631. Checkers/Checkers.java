import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        if (a >= b-1) {
            System.out.println(b);
        }
        else if (a < b && b != 0) {
            System.out.println(a+1);
        }
    }
}