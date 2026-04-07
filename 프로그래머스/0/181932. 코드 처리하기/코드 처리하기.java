class Solution {
    public String solution(String code) {
        String answer = "";
        char[] arr = code.toCharArray();
        boolean mode = false;
        for (int idx = 0; idx < arr.length; idx++) {
            if (mode == false) {
                if (arr[idx] != '1') {
                    if (idx % 2 == 0) {
                        answer += arr[idx];
                    }
                } else {
                    mode = !mode;
                }
            } else {
                if(arr[idx] != '1') {
                    if (idx % 2 != 0) {
                        answer += arr[idx];
                    }
                } else {
                    mode = !mode;
                }
            }
        }
        if (answer.length() == 0) {
            answer = "EMPTY";
        }
        return answer;
    }
}