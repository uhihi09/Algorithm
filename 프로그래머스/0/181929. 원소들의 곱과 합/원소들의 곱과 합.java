import java.util.Arrays;
class Solution {
    public int solution(int[] num_list) {
        int ans1 = Arrays.stream(num_list).sum();
        int ans2 = 1;
        for (int num : num_list) {
            ans2 *= num;
        }
        return ans2 < ans1 * ans1 ? 1 : 0;
    }
}