#00:20:48.97
import heapq

'''
음식마다의 스코빌지수가 배열로 주어질때 스코빌지수가 가장 낮은 두개를 섞어 모든 음식의 지수가 K이상이 되는 최소 믹스 횟수 구하는 문제
- 최소 스코빌지수가 K보다 작을 때, 최소값 2개를 섞어야하므로 계속 최솟값에 접근하는 것이 필요
    => 따라서, 최소힙 heapq를 이용해야함
1. scoville을 최소힙으로 바꾸면, scovile[0]이 최소 스코빌지수가 됨
2. scville[0] < k인 동안 
    - pop하면 가장 작은 스코빌, 또 pop하면 두번째 작은 스코빌
    - 두개 섞어서 push하면 알아서 정렬
3. 예외처리 필요
    [2,3]. 7
    [0,1], 7 => 만들수 없으므로 return -1
    따라서 섞은 다음에 scoville길이가 1이면 만들 수 없으므로 if문으로 확인
    [3,4], 7 => 만들 수 있으니까 scovile[0] < K인지도 확인 필요
    따라서 섞은 다음, scoville길이가 1이고 scoville[0] < K이면 return -1 
'''

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)    
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        else:
            answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution([3,4], K))