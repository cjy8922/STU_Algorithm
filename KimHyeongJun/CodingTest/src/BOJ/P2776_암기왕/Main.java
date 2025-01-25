package BOJ.P2776_암기왕;


import java.util.*;
import java.io.*;


public class Main {

    static int N, M;
    static  Map<Integer, Boolean> noteOne;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());

            noteOne = new HashMap<>();
            st = new StringTokenizer(br.readLine());

            for(int n = 0; n < N; n++) {
                noteOne.put(Integer.parseInt(st.nextToken()), true);
            }

            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());

//            noteTwo = new boolean[N+1];
            st = new StringTokenizer(br.readLine());

            for(int m = 0; m < M; m++) {
                if(noteOne.get(Integer.parseInt(st.nextToken())) == null){
                    sb.append(0 + "\n");
                } else {
                    sb.append(1 + "\n");
                }

            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
