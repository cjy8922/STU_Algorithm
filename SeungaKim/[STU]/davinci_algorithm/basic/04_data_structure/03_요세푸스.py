# 11866 요세푸스 문제0
'''
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

출력
예제와 같이 요세푸스 순열을 출력한다.
input : 7 3 
otuput : <3, 6, 2, 7, 5, 1, 4>
'''
#6:52

# N, K = input().split()

# def print_jose(n, k):
#     list = []
#     new_list = []
    
#     for a in range(1, n+1):
#         list.append(a)
        
#     # for idx in range(n):
#     #     if idx == k:
#     #         new_list.append(list[idx])
#     #         list.remove(idx)
#     #     print(f'list = {list}')
#     #     print(f'new list = {new_list}')
#     while len(list) == 0:
#         idx = 0
        
#         if idx == k:
#             new_list.append(list[idx])
#             list.remove(idx)
#             print(f'list = {list}')
#             print(f'new list = {new_list}')
#         else:
#             idx += 1
#     return new_list
# ---------------------------------

## deque 로 변환
from collections import deque

## function definition
def print_jose(n, k):
    # !!코드 참조 : deque 이용해서 데이터 추가/삭제하는 방법
    # n 값 입력 받아 queue 에 1~ n 까지 데이터 만듦 -> loop 만들 필요가 없었다
    list = deque(range(1, n+1))
    jose_list = []
    while len(list):
        count = 1
        while count < k:    # pass
            # 아하 temp 이용해서 저장해뒀다 원래 리스트 뒤로로 다시 넣어주네?
            temp = list.popleft()
            list.append(temp)
            count+=1
        # count == k 인 경우
        temp = list.popleft()  # 뒤ㄴㄴ 앞 데이터ㅇㅇ 꺼내기!
        jose_list.append(temp)
        # print(list)
        # print(jose_list)
    print("<", end="")    
    print(*jose_list, sep=', ', end="")
    print(">")


## function call
N, K = map(int, input().split())
if N > 1000 or N < 1 or K < 1 or K > 1000:
    exit()
else:
    print_jose(N,K)
    

# 8:29