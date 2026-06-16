class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer1 = "";
        for (int i: index_list) {
            answer1 += my_string.charAt(i);
        }
        return answer1;
    }
}