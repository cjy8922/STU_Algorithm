#00:33:12.86
import sys

def input():
    return sys.stdin.readline().rstrip()

sys.stdin = open('input.txt','r')
'''
O(\root_S)
- 1부터 시작하여 +2, +3하여 점차적으로 더해가며 합이 S가 될때까지 더해서 N을 찾아야하는 문제
- 각 자연수 더한 합이 S 초과하면 이전까지 더한 숫자, S과 같으면 현재까지 더한 숫자가 답이 됨.
- 매 단계마다 가장 좋은 선택을 하여 전체적으로 최적의 해결책을 찾는 방식 => 그리디 알고리즘
'''

S = int(input())

num = 1 # 첫번째 자연수
sum = 1 # 합을 저장할 변수 S=3 => 1+2 부터 시작하려고 1로 초기화

# S == 2이면 1+1로 서로 다른 자연수가 아니라서 답이 없다고 생각하는데, 
# 일단은 1이 2개니까 최댓값이 1이라고 설정.
if S == 1 or S == 2:
    print(1)
else:
    while True:
        if sum > S:
            print(num-1)
            break
        elif sum == S:
            print(num)
            break
        else:
            num += 1
            sum += num
            
'''
# 더 짧게 바꾼 코드 ---------------------------------
num = 1 # 첫번째 자연수
sum = 0 # 합을 저장할 변수
while sum + num <= S:
    sum += num
    num += 1
print(num - 1) # 마지막 더한 숫자보다 1 작은값 (합이 S안넘으니까)
'''