package PGS.더_맵게;

import java.util.*;
import java.io.*;

// 스코빌 지수를 K 이상으로 만들고 싶다
// 가장 낮은 2개의 음식을 섞는다
// 스코빌 지수가 가장 낮은 음식 + 두번째로 낮은 음식 * 2
// 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복한다
// 이때 음식을 섞어야 하는 최소 횟수를 return 하라
// 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 땐 -1을 출력하라.
public class Solution {

    public static int solution(int[] scovilleArray, int K) {
        int answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int scoville : scovilleArray) {
            pq.add(scoville);
        }

        Integer first = 0, second = 0;
        while(!pq.isEmpty()) {
            first = pq.poll();
            second = pq.poll();

            if(second == null || first >= K) {
                break;
            }
            pq.add(first + 2 * second);
            answer += 1;

        }

        if(first < K) {
            return -1;
        }

        return answer;
    }


    public static void main(String args[]) throws Exception {

        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 100;


        System.out.println(solution(scoville, K));


    }
}
