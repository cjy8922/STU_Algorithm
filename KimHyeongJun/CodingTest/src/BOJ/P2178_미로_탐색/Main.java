package BOJ.P2178_미로_탐색;

import java.util.*;
import java.io.*;

class Man {
    int y;
    int x;
    int count;
    Man(int y, int x, int count) {
        this.y = y;
        this.x = x;
        this.count = count;
    }
}

public class Main {

    static int N, M;
    static int[][] miro;
    static boolean[][] visited;

    // 상, 하, 좌, 우
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());


        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        miro = new int[N + 1][M + 1];
        visited = new boolean[N + 1][M + 1];

        for (int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            String row = st.nextToken();

            for (int m = 0; m < M; m++) {
                miro[n][m + 1] = Character.getNumericValue(row.charAt(m));
            }
        }

        BFS();

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

    static void BFS() {
        Queue<Man> queue = new LinkedList<>();

        queue.add(new Man(1, 1, 1));
        visited[1][1] = true;

        while (!queue.isEmpty()) {
            Man man = queue.poll();

            int y = man.y;
            int x = man.x;
            int count = man.count;

            for (int i = 0; i < 4; i++) {
                int ty = y + dy[i];
                int tx = x + dx[i];

                if (ty < 1 || ty > N || tx < 1 || tx > M) {
                    continue;
                }
                if (visited[ty][tx] || miro[ty][tx] == 0) {
                    continue;
                }

                if (ty == N && tx == M) {
                    sb.append(count + 1);
                    return;
                }
                queue.add(new Man(ty, tx, count + 1));
                visited[ty][tx] = true;
            }
        }
    }
}
