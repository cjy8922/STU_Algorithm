package BOJ.P1916_최소비용_구하기;

import java.util.*;
import java.io.*;

// Greedy, Dijkstra

// N개의 도시
// M개의 버스: 한 도시에서 출발 -> 다른 도시로 도착
// A 도시에서 B 도시로 가는 최소 버스 비용
// 도시 번호는 1부터 N까지
// N(1 ≤ N ≤ 1,000)
// M(1 ≤ M ≤ 100,000)
// P(비용, 0 <= P <= 100000)

class Bus implements Comparable<Bus>{
    int idx;
    int price;

    Bus(int idx, int price) {
        this.idx = idx;
        this.price = price;
    }

    @Override
    public int compareTo(Bus o){
        if(this.price == o.price){
            return Integer.compare(this.idx, o.idx);
        }

        return Integer.compare(this.price, o.price);
    }
}

public class Main {

    static int N, M;
    static Map<Integer, List<Integer>> city, price;
    static int[] answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        city = new HashMap<>();
        price = new HashMap<>();

        for(int n = 1; n <= N; n++) {
            city.put(n, new ArrayList<>());
            price.put(n, new ArrayList<>());
        }

        for(int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            city.get(u).add(v);
            price.get(u).add(p);
        }
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        answer = new int[N+1];
        Arrays.fill(answer, Integer.MAX_VALUE);
        answer[start] = 0;

        PriorityQueue<Bus> pq = new PriorityQueue<>();
        pq.add(new Bus(start, 0));

        while(!pq.isEmpty()) {
            Bus bus = pq.poll();

            int nowPrice = bus.price;

            // 이전에 계산된 가격이 더 작을 경우 continue
            if(answer[bus.idx] < nowPrice) {
                continue;
            }

            for(int i = 0; i < city.get(bus.idx).size(); i++) {
                int targetCity = city.get(bus.idx).get(i);

                // 새로 계산된 가격이 더 작을 경우 업데이트 하고 큐에 넣음
                if(answer[targetCity] > nowPrice + price.get(bus.idx).get(i)) {
                    answer[targetCity] = nowPrice + price.get(bus.idx).get(i);
                    pq.add(new Bus(targetCity, answer[targetCity]));
                }
            }
        }

        br.close();
        System.out.println(answer[end]);
    }
}
