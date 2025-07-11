import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a1 = scanner.nextInt();
        int a2 = scanner.nextInt();
        int b1 = scanner.nextInt();
        int b2 = scanner.nextInt();
        if (b1 < 0 && b2 >= 10) {
            System.out.println("A storm warning for tomorrow! Be careful and stay home if possible!");
        }
        else if (b1 < a1){
            System.out.println("MCHS warns! Low temperature is expected tomorrow.");
        }
        else if (a1 <= b1 && b2 > a2) {
            System.out.println("MCHS warns! Strong wind is expected tomorrow.");
        }
        else {
            System.out.println("No message");
        }
    }
}