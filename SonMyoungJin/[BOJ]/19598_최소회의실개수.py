#01:18.14.17
import sys
import heapq

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()
'''
시작 시각, 끝나는 시각이 주어진 N개의 회의를 하기 위해서 필요한 최소의 회의실 갯수 구하는 문제
현재 회의실 갯수에서 재사용할 수 있는 회의실이 있는지 확인하고 동작 제어.
    => 매 단계마다 최선의 선택이 필요 => 그리디 알고리즘.
    
1. 끝나야 회의 시작할 수 있으니까 끝나는 시각순 정렬
    -  회의실마다의 끝나는 시각을 저장해두고 현재 회의시작시간과 각각 비교해서 사용할 수 없으면 회의실 갯수 추가
    => 시간 초과!

2. 시작 시각순으로 정렬
    - 현재 회의 시작 시각보다 저장해둔 회의 끝나는 시각의 최솟값이 작으면 회의실 재사용가능하므로
        => 시각이 push되도 오름차순 정렬을 유지할 수 있는 우선순위큐(최소 힙) 사용 
    - 최소 heap을 이용해서 회의 끝나는 시각 저장해두고, 현재 회의 시작시간과 비교해서 사용할 수 없으면 회의실 갯수 추가
        - 회의 끝나는 최소 시각을 O(1)로 접근 가능 => 현재 시작과의 비교 연산 O(1)
'''

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x: x[0]) # 시작시각순 정렬

end_times = []
heapq.heappush(end_times, meetings[0][-1]) # 최소힙사용, 무조건 회의실 1개 쓰니까 끝나는 시각 추가

for i in range(1, N):
    # 현재회의실(end_time[0])을 사용할 수 있으니까 끝나는 시각 갱신하려고 pop
    if end_times[0] <= meetings[i][0]: 
        heapq.heappop(end_times)
    #  새로운 회의실 사용(끝나는 시각) 추가 or 끝나는 시각 갱신
    heapq.heappush(end_times, meetings[i][-1])
print(len(end_times))