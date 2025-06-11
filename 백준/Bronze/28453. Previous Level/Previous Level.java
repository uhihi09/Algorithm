import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        for (int i = 0; i < a; i++) {
            int b = sc.nextInt();
            if (b >= 300) {
                System.out.print("1 ");
            }
            else if (b >= 275) {
                System.out.print("2 ");
            }
            else if (b >= 250) {
                System.out.print("3 ");
            }
            else {
                System.out.print("4 ");
            }
        }
    }
}