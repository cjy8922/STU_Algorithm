#02:22:57.81
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드참고 : https://wikidocs.net/207391
Python3 => 3점 
Pypy3 => 100점

N개의 카드를 등차수열 만들거나 모두 같도록 바꾸는 데, 바꾸는 최소 횟수 구하는 문제
- 두 숫자 카드의 차이를 기준으로 다른 숫자 카드를 바꾸기 때문에 최대 횟수는 N-2
- 인덱스 간의 거리 계산 편하게 하려고 앞에 0넣어줘서 카드배열 cards 선언(그냥해도 될듯)
- 두 인덱스 i, j로 두 숫자를 기준으로 증감할 수를 계산
    - 증감할 수는 (cards[j]-cards[i]) / (j-i)
    - ex) 1 2 2 7 12 일때, 1(0)과 7(3)이라면 (7-1) / (3-0) = 2로 2씩증가하는 등차수열 만들 수 있음
                                                                =>1 3 5 7 12
- 두 숫자 기준으로 계신한 증감할 수로 만든 등차수열과 현재 숫자카드 수열 비교해 다른 만큼 바꾼횟수 계산하기위해 cnt=0
    - 첫번쨰 숫자카드를 계산해 저장하기 위해 start = cards[i] - diff * i
    - for문으로 현재 숫자카드 수열과 새로만든 등차수열 비교해 다르면 cnt += 1
    - 최솟값 min_cnt에 대입
'''

N = int(input())
cards = [0] + list(map(int, input().split()))
   
min_cnt = N - 2 # 두 숫자카드의 차이를 기준으로 다른 숫자카드를 바꾸기 때문에 최대 바꾸는 횟수는 N-2

for i in range(1, N):
    for j in range(i + 1, N + 1):
        if (cards[j] - cards[i]) % (j - i) != 0: # 증감할 수가 정수가 아니면 정수 수열 만들 수 없으니 넘어감
            continue
        diff = (cards[j] - cards[i]) / (j - i) # 증감할 수 계산 (두 숫자를 기준으로)
        start = cards[i] - diff * i # 첫번째 숫자카드 계산해서
        
        cnt = 0
        for k in range(1, N + 1):
            if cards[k] != start + diff * k: # diff를 더한 숫자랑 다르면 바꿔야되는 거니까 cnt += 1
                cnt += 1
        min_cnt = min(cnt, min_cnt)
print(min_cnt)