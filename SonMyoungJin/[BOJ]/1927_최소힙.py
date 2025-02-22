#00:09:20.02
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

#sys.stdin = open('input.txt', 'r')

'''
python heapq 라이브러리는 최소힙으로 항상 루트에 가장 최소값을 유지하는 binary tree 자료구조.
heappush 연산은 O(logN), heappop 연산은 O(logN)
=> N개의 연산에 대해서 O(NlogN)
'''

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)