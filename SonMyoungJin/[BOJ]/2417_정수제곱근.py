#01:20:11.53
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()
'''
주어진 정수 n에 대한 정수제곱근(q**2 >= n)을 구하는 문제
- 0 <= n < 2**63로 범위 정해져있고, 하나씩 더해서 제곱해가면서 찾으면 시간초과나기 때문에 이분 탐색 사용.
- n의 최댓값은 2**63 - 1이기 때문에 2**64 > 2**63 -1 > 2**63 q의 최댓값은 2**32.
- pow()는 부동소수점 오차 발생할 수 있으므로 **로 제곱 연산.

반례
4503599627370497 => 67108865
4503599761588225 => 67108865

67108864 * 67108864 == 4503599627370496
67108865 * 67108865 == 4503599761588225
'''
n = int(input())
#print(math.sqrt(n))
left = 0 # q의 최솟값
right = 2 ** 32 # # q의 최댓값 (n <= pow(2,63) - 1)

if n <= 1:
    print(n)
else:
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < n: 
            left = mid + 1
        elif mid * mid > n:
            right = mid - 1
        else: # mid * mid == n이면 mid 바로 출력하고 break 종료
            print(mid)
            break
    # while문이 정상 종료
    # left는 항상 q^2 >= n인 첫번째 값이므로 left 출력
    else: 
        print(left)
'''
#시간 초과!-------------
num = 0
while pow(num, 2) < n:
     num += 1
print(num)
'''

