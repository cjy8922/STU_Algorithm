'''
** 백준 1002 터렛**
조규현(1)과 백승환(2)은 터렛에 근무하는 직원이다. 
하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다.

이석원(3)은 조규현과(1) 백승환(2)에게 상대편 마린(류재명(4))의 위치를 계산하라는 명령을 내렸다.
조규현과(1) 백승환(2)은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (1) $(x_1, y_1)$와 
백승환의 좌표 (2) $(x_2, y_2)$가 주어지고, 

조규현이 계산한 류재명 과의 거리 $r_1$과 -> (1)-(3)

백승환이 계산한 류재명과의 거리 $r_2$가 주어졌을 때, -> (2)-(3)
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

! 경우의 수 무한대일 경우 = print out -1 

input) 
T : nums of testcases
x_1, y_1, r_1, x_2, y_2, r_2 :  coordinates of (1), (2) and distance

output)
N : nums of possible position of (3)
'''
# probability?
# starts at 10:18, ends at 11:32
from math import sqrt

# def constraints():
#     if x_1

test_nums = int(input())

def position():
    output = 0
    # for i in (1, test_nums) :
    # round 1, .., test_nums
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    
    # constraints 1
    if x_1 | y_1 | x_2 | y_2 > 10000 or x_1 | y_1 | x_2 | y_2 < -10000:
        print("Sorry, coordinates you entered(x1 | y1 | x2 | y2) are out of range. do it again in (-10000, 10000)")
    # constraint 2
    elif r_1 | r_2 > 10000 or r_1 | r_2 < 1 :
        print("Sorry, distance you entered(r1 or r2) is out of range. Try again in (1, 10000)")
    else:
        distance = sqrt((x_1-x_2)**2 + (y_1-y_2)**2)
        # length = abs(r_1 - r_2)
        difference = abs(r_1 - r_2)
        
        # case 1 : fully overlap
        if distance ==  0 and difference == 0:
            output = -1

        # case 2 : partially overlap
        # elif distance != 0 나는 바보 멍청이야 보니까 더 헷갈림.. 괜춘해 할수잇어 
        # 2주 뒤에 다시 풀어 볼것
        # 삼각형 특 : 가장 긴 변이 다른 두변의 길이보다 작음, 5 3 4 생각하면 됨
        elif distance < r_1 + r_2 and distance > difference:
            output = 2
        
        # case 3 : one point overlap
        elif distance == difference or distance == r_1 + r_2 : 
            output = 1
        
        # case 4 : separated
        else :
            output = 0
            
    print(output)
    
# for i in (1,test_nums):
for _ in range(test_nums):
    position()