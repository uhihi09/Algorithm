import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        for (int i = 0; i < a.length(); i++) {
            Character b = a.charAt(i);
            if (Character.isLowerCase(b)) {
                System.out.print(Character.toUpperCase(b));
            }
            else {
                System.out.print(Character.toLowerCase(b));
            }
        }
    }
}
