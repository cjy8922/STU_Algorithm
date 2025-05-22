'''
최대 공약수 구하기 - Find gcd(greates common divisor or factor)

두 개의 숫자 a, b를 입력받고 그 수의 최대 공약수를 구해보겠습니다.
'''
# a, b = map(int, input().split())
# divisor = 0
# remainder = 0
# gcd = 0

# if a > b:
#     divisor = b
# else :  # when 'b' is greater or equal to a, still set an 'a' as a divisor
#     divisor = a
    
# for i in range(divisor, 1, -1):
#     # 1 2 3 4 5 6 / 4 6 
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print(f'GCD : {gcd}')

'''
**유클리드 호제법**

두 수 중 큰 수를 작은 수로 나눕니다.
나머지가 0이면 작은 수가 최대 공약수가 됩니다.
나머지가 0이 아니면 작은 수가 큰 수가 되고, 
나머지를 작은 수로 대체하고 1단계로 돌아갑니다.

이것이 유클리드 호제법의 알고리즘입니다. 
예를 들어 510과 210의 최대 공약수를 구해보겠습니다.

510을 210으로 나눕니다. 나머지는 90입니다. 510 = 210 * 2 + 90
210을 90으로 나눕니다. 나머지는 30입니다. 210 = 90 * 2 + 30
90을 30으로 나눕니다. 나머지는 0입니다. 90 = 30 * 3 + 0
나머지가 0이므로 최대공약수는 30입니다.

유클리드 호제법을 몰랐다면 210부터 30까지 거꾸로 반복하면서 나눗셈을 모두 해봐야 했지만,
유클리드 호제법으로 4단계 만에 최대공약수를 구했습니다. 
이것을 직접 코드로 작성해 보겠습니다.
'''
print("Enter any two numbers to find GCD >>")
a, b = map(int, input().split())


def euclidean(a, b):
    dividend = 0
    divisor = 0
    remainder = 0
    gcd = 0
    
    if a > b :
        dividend = a    # bigger num
        divisor = b     # smaller num
    else : # a <= b
        dividend = b
        divisor = a
    
    remainder = dividend % divisor  # **redundant statement** -> further optimization is needed
    while remainder != 0:
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
    
    gcd = divisor
    return gcd

result = euclidean(a, b)
print(f'GCD : {result}')