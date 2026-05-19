import java.util.ArrayList;
import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> cnt = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String temp = String.valueOf(i);
            Boolean is_right = true;
            for (int j = 0; j < temp.length(); j++) {
                if (temp.charAt(j) != '5' && temp.charAt(j) != '0') {
                    is_right = false;
                    break;
                }
            }
            if (is_right == true) {
                cnt.add(i);
            }
        }
        if (cnt.size() == 0) {
            cnt.add(-1);
        }
    int[] answer = new int[cnt.size()];
    for (int i = 0; i < cnt.size(); i++) {
        answer[i] = cnt.get(i);
    }
    return answer;
    }
}