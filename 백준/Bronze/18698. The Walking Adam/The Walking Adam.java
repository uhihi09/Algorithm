import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        for (int i = 0; i < a; i++) {
            String s = sc.next();
            int cnt = 0;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == 'D') {
                    break;
                }
                else {
                    cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
}