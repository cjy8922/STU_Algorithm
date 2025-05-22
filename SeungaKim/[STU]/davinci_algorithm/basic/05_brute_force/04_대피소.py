# 28215 대피소
'''
INPUT
N K
X1 Y1
X2 Y2
X3 Y3
..
Xi Yi

OUTPUT
대피소와 집 사이 거리 중 최대거리가 짧은 거리 값

CONSTRAINTS
1. 주어지는 모는 수는 정수
2. 1 <= K <= 3
3. K <= N <= 50
4. 0 <= Xi <= 100000
5. 0 <= Yi <= 100000
6. 집의 위치는 중복되지 않는다 (X1, Y1), (X2, Y2), ... (Xi, Yi) 는 고유하다
'''
# 5:54
from itertools import combinations

def input_coordinates(n):
    house_position = list()
    for _ in range(n):
        X_i, Y_i = map(int, input().split())
        # constraints
        if not 0 <= X_i <= 100000 and 0 <= Y_i <= 100000:
            exit()
        else:
            house_position.append((X_i,Y_i))  # (Xi, Yi)로 묵는거 까먹어서 에러났음
    return house_position 

def shelter_combinations(H):
    '''
    # combinations 사용법 코드 참조
    for comb in combinations(range(N), K):
        print(comb)
    '''
    possible_combo = list()
    for shelter in combinations(H, K):
        possible_combo.append(shelter)
    # print(possible_combo)
    return possible_combo

def find_max_distance(s_list):
    # d_list = []
    # !! 초기화하기 -> 어떤 원리? float('inf')?
    INF = float('INF')
    min_max_distance = INF
    
    for shelters in s_list:
        # ??
        max_d = 0
        for h_x, h_y in house:
            # calculate distance closest to possible 대피소
            d_shelter = min(abs(h_x - s_x) + abs(h_y - s_y) for s_x, s_y in shelters)
            
            max_d = max(max_d, d_shelter)
            # d_list.append(max_d)
        min_max_distance = min(min_max_distance, max_d)
        
    return min_max_distance


N, K = map(int, input().split())

# check constraints
if K > 3 or K < 1:
    exit()
elif N < K or N > 50 :
    exit()
else:
    house = input_coordinates(N)
    # print(house)
    shelter_list = shelter_combinations(house)
    # print(shelter_list)
    max_distance = find_max_distance(shelter_list)
    print(max_distance)
    

#6:38
# 1:02
# 2:29