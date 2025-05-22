# 17618 신기한 수
'''
18을 이루는 각 자릿수인 1과 8을 합한 9는 18의 약수가 된다.
민철이는 18과 같이 모든 자릿수의 합으로 나누어지는 수를 여러 개 더 찾아냈는데, 12, 21도 그런 신기한 수였다. 민철이는 이렇게 모든 자릿수의 합으로 나누어지는 수를 “신기한 수”라고 부르기로 했다. 
민철이는 더 큰 신기한 수를 찾아보기도 했는데 1729도 신기한 수라는 걸 알아내었다. 
1729는 1+7+2+9=19로 나누어진다.
입력으로 1 이상인 자연수 N이 주어질 때 N 이하인 신기한 수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 정수 N (1 ≤ N ≤ 10,000,000) 하나가 주어진다.

출력
N 이하인 신기한 수의 개수를 정수로 출력한다.
'''
# 2:39
# max_val = input(int)
max_val = int(input())
min_val = 1

def remainder_sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

# constraint, (1 ≤ N ≤ 10,000,000)
if max_val < 1 or max_val > 10000000:
    print("Invalid input, please try again. (1 ≤ N ≤ 10,000,000)")
    exit()
else:
    common_divisor_array = [False]*(max_val+1)
    sum_value = 0
    count = 0
    for i in range(1, max_val + 1):
        sum_value = remainder_sum(i)
        if i % sum_value == 0:
            common_divisor_array[i] = True
            count += 1
        else:
            common_divisor_array[i] = False

    # print nums of 신기한 수
    print(count)
    
# 2:51