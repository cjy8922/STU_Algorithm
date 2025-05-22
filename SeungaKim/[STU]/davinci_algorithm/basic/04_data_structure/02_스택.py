# 10828 스택
'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
# 6:15

# !없이도 코드 돌아는 갔지만 채점속도가 너무 느렸음. 
# 입력(num of command (1 ≤ N ≤ 10,000))이 최대 만개라서 속도가 느림 
# -> 느려서 얘로 인풋 대체
import sys
input = sys.stdin.readline
#

nums_of_command = int(input())

# def stack_integer(n):
#     stack_i = [] # LIFO, python에서 list = stack
    
#     for _ in range(n):
#         command, num = input().split()
        
#         if command == 'push':
#             integer = int(num)
#             stack_i.append(integer)
            
#         elif command == 'pop':
#             if len(stack_i) == 1:
#                 print(-1)
#             else:
#                 print(stack_i.pop())
            
#         elif command == 'size':
#             count = 0
#             for _ in range(len(stack_i)):
#                 count += 1
#             print(count)
        
#         elif command == 'empty':
#             if len(stack_i) == 0:
#                 print(1)
#             else:
#                 print(0)
        
#         # top 을 모르것다
#         elif command == 'top':
#             if len(stack_i) == 0:
#                 print(-1)
#             else:
#                 print(stack_i[-1])
        

# print(stack_integer(nums_of_command))



def stack_integer(n):
    stack_i = [] # LIFO, python에서 list = stack
    
    for _ in range(n):
        command = input().split()
        
        if command[0] == 'push':
            integer = int(command[1])
            stack_i.append(integer)
            
        elif command[0] == 'pop':
            if len(stack_i) == 0:
                print(-1)
            else:
                print(stack_i.pop())
            
        elif command[0] == 'size':
            count = 0
            for _ in range(len(stack_i)):
                count += 1
            print(count)
        
        elif command[0] == 'empty':
            if len(stack_i) == 0:
                print(1)
            else:
                print(0)
        
        # top 을 모르것다
        elif command[0] == 'top':
            if len(stack_i) == 0:
                print(-1)
            else:
                print(stack_i[-1])
        

stack_integer(nums_of_command)

# 6:47