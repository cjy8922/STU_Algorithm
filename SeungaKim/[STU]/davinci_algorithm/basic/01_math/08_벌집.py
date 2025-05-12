# 벌집 지나가는 방 개수 구하기
'''
위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지
(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오.

예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
'''
user_input = int(input()) # input
layers = 1    # output
nums_of_honey = 1     # nums of 벌집

# 수열 구하ㅏ기 같음, start at 12:29
if user_input > 1000000000 or user_input < 1 :
    print("Invalid input. Plz try again in (1, 1000000000)")
else : 
    while user_input > nums_of_honey :  # 뭐지? 왜 user_input >= nums_of honey 하니까 틀리는거지??
        nums_of_honey += 6*layers
        layers += 1
    
print(layers)