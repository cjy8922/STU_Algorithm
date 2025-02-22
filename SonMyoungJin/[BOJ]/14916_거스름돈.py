#00:45:51.43
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
거스름돈을 2원과 5원으로 주는데, 줄 수 있는 가장 최소 개수를 출력하는 문제
- 동전 개수가 최소가 되려면 5원짜리 동전(더 큰 단위)을 가능한 사용 후,
- 나머지 값이 2원짜리 동전으로 해결 가능하면 해결
- 5원짜리 동전을 최대한 많이 사용(가장 좋은 선택)
    => 매 선택에서 가장 좋은 선택하는 것이 "전역적인 최적해"로 이어질 수 있음
    => 그리디 알고리즘 사용

5원동전을 기준으로 하여 n % 5로 접근
1. 나머지 0이면 n//5가 가장 최소 개수.
2. 나머지 1, 3이면, n은 짝수고, 2원으로 나머지를 처리할 수 없으므로
    - cnt_five -= 1 해서, 뺀 나머지는 2원으로 처리.
        (짝수는 5원을 짝수개 사용해야 처리 가능)
    - n == 1, n == 3 => 처리 못함.
3. 나머지 2, 4이면, n은 홀수고, 2원으로 나머지를 처리 가능.

모든 상황을 포함할 수 있도록 짜야 함. 자꾸 예외상황 몇개 빼먹게 풀어서 틀림
'''

n = int(input())

cnt_five = n // 5
remain = n % 5

if remain % 2 != 0: # 5로 나눈 나머지 1, 3
    if cnt_five >= 1:
        cnt_five -= 1
        cnt_two = (n - 5 * cnt_five) // 2
        print(cnt_five + cnt_two)
    else:
        print(-1)
    
elif remain % 2 == 0 : #5로 나눈 나머지 2, 4
    cnt_two = remain // 2
    print(cnt_five + cnt_two)
    
else: # 나머지 0
    print(cnt_five)