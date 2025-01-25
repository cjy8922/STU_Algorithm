package BOJ.P15664_N과M_10;

import java.util.*;
import java.io.*;

// 다시 풀어보기
public class Main {

    static int N, M;
    static int[] nums;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int n = 0; n < N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        boolean[] visited = new boolean[N];
        List<Integer> result = new ArrayList<>();
        BackTracking(result, 0);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(List<Integer> result, int start) {
        if(result.size() == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return;
        }

        int before = 0;
        for(int i = start; i < N; i++) {
            if(before == nums[i]) {
                continue;
            }
            result.add(nums[i]);
            BackTracking(result, i + 1);
            result.remove(result.size() - 1);
            before = nums[i];
        }
    }
}
