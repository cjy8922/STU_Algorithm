'''
**백준 14215 세 막대**
문제
영선이는 길이가 a, b, c인 세 막대를 가지고 있고, 
각 막대의 길이를 마음대로 줄일 수 있다.
영선이는 세 막대를 이용해서 아래 조건을 만족하는 삼각형을 만들려고 한다.

각 막대의 길이는 양의 정수이다
세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
삼각형의 둘레를 최대로 해야 한다.
a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 a, b, c (1 ≤ a, b, c ≤ 100)가 주어진다.

출력
첫째 줄에 만들 수 있는 가장 큰 삼각형의 둘레를 출력한다.

예제
예제 입력 1
1 2 3
예제 출력 1
5

예제 입력 2
2 2 2
예제 출력 2
6
'''
# a, b, c = map(int, input().split())
# max_length = 0
# longest = max(a, b, c)
# shortest = min(a, b, c)
# middle = a + b + c - longest - shortest

# if shortest + middle > longest:
#     max_length = shortest + middle + longest
# else:
#     adjust_longest = shortest + middle - 1
#     max_length = shortest + middle + adjust_longest

# print(max_length)

'''
# => **아하 모먼트 : array sorting 하면 되는거였다**

세 막대 모범 답안
arr = list(map(int, input().split()))

arr.sort()
a, b, c = arr

if a + b <= c:
    c = a + b - 1

print(a + b + c)
'''
