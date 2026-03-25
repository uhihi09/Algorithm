class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int cnt1 = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int cnt2 = 2 * a * b;
        if (cnt1 >= cnt2) {
            answer = cnt1;
        } else{
            answer = cnt2;
        }
        return answer;
    }
}