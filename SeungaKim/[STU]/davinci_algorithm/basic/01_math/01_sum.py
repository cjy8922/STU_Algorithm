'''
    [01] 1 부터 n 까지의 합계 구하기
    n : user input
    1 부터 n 까지의 합계 구하는 프로그램 만들기 :
    (1) using for loop, (2) using while loop
'''
# (1) USING FOR LOOP
# user_input = input("Type a random number you want to add up : ")
# random_n = int(user_input)
# sum_n = 0

# for i in range(1, random_n + 1):
#     sum_n += i

# print("Total sum is : ", sum_n)

# (2) USING WHILE LOOP
# user_input2 = input("Type a ran number you wanna add up : ")
# random_n2 = int(user_input2)
# count = 1
# sum_num2 = 0

# while(count < random_n2 + 1):
#     sum_num2 += count
#     count += 1

# print("Total sum(second one) is : ", sum_num2)

# (3)USING 'SUM()' FUNCTION
# user_input3 = int(input("Type n : "))
# sum_n3 = sum(range(1, (user_input3+1)))
# print("Total sum(third one) is : ", sum_n3)

'''
# 8393
'''
user_input = input()
random_n = int(user_input)
sum_n = 0

for i in range(1, random_n + 1):
    sum_n += i

print(sum_n)