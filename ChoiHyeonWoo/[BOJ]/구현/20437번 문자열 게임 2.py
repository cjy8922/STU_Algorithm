# import sys
# input = sys.stdin.readline
# T = int(input())
# for turn in range(T):
#     W = input()
#     K = int(input())
#     answer = []
#     for i in range(0, len(W)):
#         check = W[i]
#         cnt = K
#         for j in range(i + K-1, len(W)):
#             if W[j] == check:
#                 answer.append(cnt)
#                 break
#             cnt += 1
#     if answer:
#         print(min(answer), max(answer))
#     else:
#         print(-1)

from collections import defaultdict
import sys

input = sys.stdin.readline
T = int(input())
for turn in range(T):
    minimum = 393958458495
    maximum = -39483985
    check = []
    W = input()
    K = int(input())
    dict_list = defaultdict(list)
    for i in range(len(W)):
        dict_list[W[i]].append(i)
    for idx_list in dict_list.values():
        if len(idx_list) < K:
            continue
        for i in range(len(idx_list)-K+1):
            minimum = min(minimum, idx_list[i + K -1] - idx_list[i] + 1)
            maximum = max(maximum, idx_list[i + K -1] - idx_list[i] + 1)
    if maximum < 0:
        print(-1)
    else:
        print(minimum, maximum)