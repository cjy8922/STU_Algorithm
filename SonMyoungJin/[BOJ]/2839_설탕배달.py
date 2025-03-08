#00:37.48.18
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
Nkg 설탕을 5kg, 3kg에 나누어 담을 때, 쓸 수 있는 최소 봉지갯수 구하는 문제
- 봉지를 최소로 사용하기 위해 5kg봉지를 최대한 많이 사용하고 남은 거는 3kg로
- N을 5로 나눈 나머지가 3의 배수 아니라면, 5 갯수 줄이고 다시 계산 
    => 가장 최적의 선택을 매번 반복 => 그리디 알고리즘

1. 5kg 봉지의 최대 갯수는 N // 5이기 때문에 cnt_5 = N//5
2. 1,2,4는 나눠담을 수 없으므로 -1
3. 현재 N - cnt_5 * 5 가 3의 배수 아니면 cnt_5 -=1 해서 계속 계산해줌
    - cnt_5가 0보다 작아지면
        - 나눠 담을 수 없으니까 break해서 나오고 -1 출력
    - while문 정상적으로 종료되면 cnt_3까지 계산해서 합산해서 출력
    
'''

N = int(input())

cnt_3 = 0
cnt_5 = N // 5 # 5kg 봉지의 최대 갯수
remain = N % 5

if cnt_5 == 0 and remain != 3 and remain != 0: # 1,2,4
     print(-1)
     
else:
    while (N - (cnt_5 * 5)) % 3 != 0:
        cnt_5 -= 1
        if cnt_5 < 0:
            cnt_5 = 0
            break

    if (N - (cnt_5 * 5)) % 3 == 0:
        cnt_3 = (N - (cnt_5 * 5)) // 3
        print(cnt_5 + cnt_3)
    else:
        print(-1)
        
'''
# 이렇게 작성해야함.

def sugar_delivery(N):
    cnt_5 = N // 5
    for i in range(cnt_5, -1, -1):
        remain_weight = N - i * 5
        if remain_weight % 3 == 0:
            return i + remain_weight // 3
    return -1

print(sugar_delivery(N))

'''

