import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            for (int ii = 0; ii < b; ii++) {
                for (int iii = 0; iii < a; iii++) {
                    System.out.print("X");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}