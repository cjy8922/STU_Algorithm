import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []
maximum = -12498
for _ in range(N):
    a = int(input())
    sushi.append(a)
for i in range(N):
    a = []
    for j in range(i, i + k):
        if j >= N:
            j = abs(j-N)
        a.append(sushi[j])
    print(a)
    cnt = len(set(a))
    if c not in a:
        cnt += 1
    maximum = max(maximum, cnt)
print(maximum)