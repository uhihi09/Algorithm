import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ArrayList<Integer> temp_list = new ArrayList<>();
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                if (arr[j] > queries[i][2]) {
                    temp_list.add(arr[j]);
                }
            }
            if (temp_list.isEmpty()) {
                answer[i] = -1;
            } else {
                answer[i] = Collections.min(temp_list);
            }
        }
        return answer;
    }
}