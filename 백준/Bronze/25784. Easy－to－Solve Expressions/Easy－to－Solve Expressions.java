import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] cnt = new int [3];
        for (int i = 0; i < 3; i++) {
            cnt[i] = sc.nextInt();
        }
        Arrays.sort(cnt);
        if (cnt[2] == cnt[0]+cnt[1]){
            System.out.println(1);
        }
        else if (cnt[2] == cnt[1]*cnt[0]){
            System.out.println(2);
        }
        else {
            System.out.println(3);
        }
    }
}