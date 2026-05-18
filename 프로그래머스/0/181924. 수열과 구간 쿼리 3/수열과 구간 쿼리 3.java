class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        for (int i = 0; i < queries.length; i++) {
            int temp1 = queries[i][0];
            int temp2 = queries[i][1];
            int temp3 = answer[temp1];
            answer[temp1] = answer[temp2];
            answer[temp2] = temp3;
        }
        return answer;
    }
}