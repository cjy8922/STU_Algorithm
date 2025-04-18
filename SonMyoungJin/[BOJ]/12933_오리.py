#01:47:30.86
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고: https://github.com/tony9402/algorithm-solutions/blob/main/solutions/baekjoon/12933/main.cpp

섞여있는 문자열에서 quack이라는 오리울음소리를 찾아 오리의 최소 마릿수 세는 문제
- 오리는 한번 이상 울 수 있는데 항상 quack으로 움
- 한 글자씩 읽어가면서 가능한 한 quack을 진행중인 오리에게 quack을 주고 안되면 새로운 오리로 간주
    => 지역적인 최적의 선택이 전체적인 최적의 선택이 되므로 그리디 문제

1. quack은 섞여있기 때문에 각 오리가 quack의 어느 부분까지 울었는지 상태 저장이 필요
    => idx(0:다시시작, 1:q, 2:u,..,5:k)를 저장한 ducks 배열로 저장해 관리
2. 섞여있는 문자열 sound에서 quack을 찾기 위해, for문을 sound로 하나 ducks로 하나 중첩으로 확인
    - 문자 ch마다 quack의 진행인지 확인

'''
sound = [i for i in input()]

def find_quack(sound):
    ducks = [] # 각 오리가 quack의 어디까지 울었는지 idx 저장 (1:q, 2:u,.., 5:k)
    quack = 'quack'
    cnt = 0
    
    for ch in sound:
        found_duck = False
        for i in range(len(ducks)):
            if quack[ducks[i]] == ch:
                ducks[i] += 1
                if ducks[i] == 5:   # quack 완성하면 다시 0으로 초기화
                    ducks[i] = 0
                found_duck = True
                break               # 현재 문자처리했으니까 다음 문자로   
        if not found_duck:
            if ch == 'q': # 새 오리 시작
                ducks.append(1) # 'q'로 시작하니까 1 push
            else:
                return -1 # q가 처음으로 나오지 않으면 -1
    
    if any(d != 0 for d in ducks): # 완성되지 않은 오리 있으면
        return -1
    
    return len(ducks)
        
print(find_quack(sound))