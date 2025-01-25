package BOJ.P15665_N과M_11;

import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[] nums;
    static StringBuilder sb = new StringBuilder();
    static Map<String, Boolean> tmpMap = new HashMap<>();

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

        List<Integer> result = new ArrayList<>();
        BackTracking(result);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(List<Integer> result) {
        if(result.size() == M) {
            String tmp = "";
            for(Integer num : result) {
                tmp += num + " ";
            }
            tmp += "\n";
            if(tmpMap.get(tmp) == null) {
                sb.append(tmp);
                tmpMap.put(tmp, Boolean.TRUE);
            }
            return;
        }

        for(int n = 0; n < N; n++) {
            result.add(nums[n]);
            BackTracking(result);
            result.remove(result.size() - 1);
        }
    }
}
