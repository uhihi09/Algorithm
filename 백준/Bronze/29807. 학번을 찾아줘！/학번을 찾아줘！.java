import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[5];
        int ans = 0;
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        if (arr[0] > arr[2]) {
            ans += (arr[0] - arr[2]) * 508;
        } else {
            ans += (arr[2] - arr[0]) * 108;
        }
        if (arr[1] > arr[3]) {
            ans += (arr[1] - arr[3]) * 212;
        } else {
            ans += (arr[3] - arr[1]) * 305;
        }
        if (arr[4] > 0){
            ans += arr[4] * 707;
        }
        System.out.println(ans*4763);
    }
}