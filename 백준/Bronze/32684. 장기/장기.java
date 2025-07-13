import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a1 = sc.nextInt();
        float b1 = sc.nextInt();
        float c1 = sc.nextInt();
        float d1 = sc.nextInt();
        float e1 = sc.nextInt();
        float f1 = sc.nextInt();
        float a2 = sc.nextInt();
        float b2 = sc.nextInt();
        float c2 = sc.nextInt();
        float d2 = sc.nextInt();
        float e2 = sc.nextInt();
        float f2 = sc.nextInt();
        double ans1 = a1*13 + b1*7 + c1*5 + d1*3 + e1*3 + f1*2;
        double ans2 = a2*13 + b2*7 + c2*5 + d2*3 + e2*3 + f2*2 + 1.5;
        if (ans1 > ans2) {
            System.out.println("cocjr0208");
        }
        else if (ans2 > ans1) {
            System.out.println("ekwoo");
        }
        else {
            System.out.println("ekwoo");
        }
    }
}