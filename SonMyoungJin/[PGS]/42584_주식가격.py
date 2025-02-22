#00:32:04.89
from collections import deque
'''
초 단위로 기록된 주식가격 배열 있을 때, 각 초단위에 대한 가격에서 가격이 떨어지지 않은 기간이 몇초인지 구하는 문제
- [1,2,3,2,3]
- 1초 시점 = $1 => 5초 시점 = $3 까지 가격 안떨어짐 => 4(5-1)초 동안 가격이 떨어지지 않음
- 2초 시점 = $2 => 5초 시점 = $3 까지 가격 안떨어짐 => 3(4-1)초 동안 가격이 떨어지지 않음
- 3초 시점 = $3 => 4초 시점 = $2 까지 가격 안떨어짐 => 1(4-3)초 동안 가격이 떨어지지 않음
- 5초 시점 = $5 => 5초가 마지막이므로 가격 떨어지지 않은 시간 없음 0(5-5)초 동안 가격이 떨어지지 않음

1. 현재 가격과 순차적으로 이후의 가격들을 비교해야 하므로 FIFO인 큐를 사용.
    - 현 가격과 그 다음 가격들을 순차적으로 비교하기 위해 deque(prices) 사용해서,
    첫번째 가격은 popleft하고 그다음은 for문으로 접근해 비교.
        - 기간 계산을 위해 sec 변수 선언해서 가격 안떨어졌으면 sec += 1
        
첫번째 가격과 n-1개의 가격 비교해야하니까 => O(n^2)

스택이 더 효율적 (가장 최근 상태를 기억하고 그 상태에 따라서 이전 상태를 처리) 
'''
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        sec = 0
        price = queue.popleft()
        for next_price in queue:
            if price <= next_price:
                sec +=1
            else:
                sec += 1
                break
        answer.append(sec)
    return answer
        
prices = [1, 2, 3, 2, 3]
print(solution(prices))


'''
# 시간초과!---------------------------------
O(n^2)인데,
for i in range(len(prices)):
        queue = deque(prices[i+1:]) 
=> 여기서 매번 새로운 큐 만드니까 불필요한 메모리할당

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        queue = deque(prices[i+1:])
        while queue:
            next_price = queue.popleft()
            if prices[i] <= next_price:
                answer[i] += 1   
            else:
                answer[i] += 1
                break
    return answer
  
# 더 빠른 정답 코드-----------------------------
# 가격들을 스택에 넣고, 이전 가격 > 현 가격 이면, 떨어진 거니까 stack.pop()해서 기간을 바로 계산 해줌.
# 최대 한번씩만 스택에 넣고 한번씩만 빼니까 => O(N)

def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        if stack != []:
            #print(stack)
            while stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
        
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
        
    return answer
        
prices = [1, 2, 3, 2, 3]
print(solution(prices))
'''