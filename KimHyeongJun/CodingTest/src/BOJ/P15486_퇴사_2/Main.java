package BOJ.P15486_퇴사_2;

import java.util.*;
import java.io.*;

// 아직...
// 오늘부터 N+1일째 되는 날 남은 N일 동안 최대한 많은 상담을 하려 한다.
// 하루에 하나씩 서로 다른 사람의 상담
// 상담을 완료하는데 걸리는 기간 Ti, 상담 금액 Pi
// 예)
// 1일 T1 = 3, P1 = 10
// 1일에 시작 -> 3일에 끝남, 비용은 10

// 최대 수익을 구하여라
// N (1 ≤ N ≤ 1,500,000)
// (1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000)

class Consult implements Comparable<Consult> {
    int start;
    int end;
    int price;

    Consult(int start, int end, int price) {
        this.start = start;
        this.end = end;
        this.price = price;
    }

    @Override
    public int compareTo(Consult o){
        return Integer.compare(this.end, o.end);
    }
}

public class Main {

    static int N;
    static Map<Integer, List<Consult>> consultMap;
    static long[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        consultMap = new HashMap<>();
        for(int i = 1; i <= 1500100; i++){
            consultMap.put(i, new ArrayList<>());
        }


        for(int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int end = n + t - 1;

            consultMap.get(end).add(new Consult(n, end, p));
        }

        dp = new long[N+1];

        long answer = 0;
        for(int i = 1; i <= 1500100; i++){
            if(i > N) {
                break;
            }

            if(consultMap.get(i).size() == 0) {
                dp[i] = dp[i-1];
                continue;
            }

            for(Consult consult : consultMap.get(i)) {
                dp[i] = Math.max(dp[i], Math.max(dp[i-1], dp[consult.start-1] + consult.price));
                answer = Math.max(answer, dp[i]);
            }
        }

        System.out.println(answer);
    }
}


// // 시간 초과
//public class Main {
//
//    static int N;
//    static int[] T, P;
//    static long[] dp;
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        N = Integer.parseInt(st.nextToken());
//
//        T = new int[N+1];
//        P = new int[N+1];
//        for(int n = 1; n <= N; n++) {
//            st = new StringTokenizer(br.readLine());
//            T[n] = Integer.parseInt(st.nextToken());
//            P[n] = Integer.parseInt(st.nextToken());
//        }
//
//        // dp[n] -> n일에 퇴사할 때 얻을 수 있는 최대 수익
//        dp = new long[N+1];
//
//        long answer = 0;
//        for(int n = 1; n <= N; n++) {
//            for(int i = 1; i <= n; i++) {
//
//                // 상담이 끝나는 날(end)이 퇴사 날짜(n)보다 클 경우 continue
//                int end = i + T[i] - 1;
//                if(end > n) {
//                    continue;
//                }
//                dp[n] = Math.max(dp[n], dp[i-1] + P[i]);
//                answer = Math.max(dp[n], answer);
//            }
//        }
//        System.out.println(answer);
//    }
//
//}
