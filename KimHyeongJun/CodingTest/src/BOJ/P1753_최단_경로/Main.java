package BOJ.P1753_최단_경로;

import java.util.*;
import java.io.*;

// 시작 점에서 다른 모든 정점으로의 최단 경로를 구하라
// 모든 간선의 가중치는 10 이하의 자연수
// V: 정점의 개수
// E: 간선의 개수
// K: 시작 정점
// u, v, w: u에서 v로 가는 가중치 w

// 정점은 1 ~ V

class Node implements Comparable<Node>{
    int idx;
    int distance;

    Node(int idx, int distance) {
        this.idx = idx;
        this.distance = distance;
    }

    @Override
    public int compareTo(Node o) {
        if(this.distance == o.distance) {
            return Integer.compare(this.idx, o.idx);
        }

        return Integer.compare(this.distance, o.distance);
    }

}

public class Main {

    static int V, E, K;
    static Map<Integer, List<Integer>> graph, weights;
    static StringBuilder sb = new StringBuilder();
    static int[] answer;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());

        graph = new HashMap<>();
        weights = new HashMap<>();

        for(int v = 1; v <= V; v++) {
            graph.put(v, new ArrayList<>());
            weights.put(v, new ArrayList<>());
        }

        int u, v, w;
        for(int e = 0; e < E; e++) {
            st = new StringTokenizer(br.readLine());

            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            weights.get(u).add(w);
        }

        BFS();

        for(int i = 1; i <= V; i++) {
            if(i == K) {
                sb.append(0 + "\n");
            } else if (answer[i] == Integer.MAX_VALUE) {
                sb.append("INF" + "\n");
            } else {
                sb.append(answer[i] + "\n");
            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BFS() {

        answer = new int[V+1];
        Arrays.fill(answer, Integer.MAX_VALUE);
        answer[K] = 0;

//        boolean[] visited = new boolean[V+1];
//        visited[K] = true;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(K, 0));

        while(!pq.isEmpty()) {
            Node node = pq.poll();
            int idx = node.idx;
            int distance = node.distance;

            if(distance > answer[idx]) {
                continue;
            }

            for (int i = 0; i < graph.get(idx).size(); i++) {
                int neighbor = graph.get(idx).get(i);
                int weight = weights.get(idx).get(i);

                // 새로 계산된 거리가 더 작으면 업데이트하고 큐에 넣음
                if (distance + weight < answer[neighbor]) {
                    answer[neighbor] = distance + weight;
                    pq.add(new Node(neighbor, distance + weight));
                }
            }
        }
    }

    // 시간 초과
//    static void BFS() {
//
//        boolean[] visited = new boolean[V+1];
//        answer = new int[V+1];
//
//        Arrays.fill(answer, Integer.MAX_VALUE);
//
//        Queue<Node> queue = new LinkedList<>();
//        queue.add(new Node(K, 0));
//
//        visited[K] = true;
//        answer[K] = 0;
//
//        while(!queue.isEmpty()) {
//            Node node = queue.poll();
//
//            int distance = node.distance;
//
//            int neighbor;
//            System.out.println(node.idx);
//            System.out.println("====");
//            for(int i = 0; i < weights.get(node.idx).size(); i++) {
//
//                int weight = weights.get(node.idx).get(i);
////                System.out.println(node);
//                neighbor = graph.get(node.idx).get(i);
//
//                if(answer[neighbor] == Integer.MAX_VALUE) {
//                    answer[neighbor] = distance + weight;
//                    queue.add(new Node(neighbor, answer[neighbor]));
//                }
//                else if(answer[neighbor] >= distance + weight) {
//                    answer[neighbor] = distance + weight;
//                    queue.add(new Node(neighbor, answer[neighbor]));
//                }
//            }
//        }
//    }
}
