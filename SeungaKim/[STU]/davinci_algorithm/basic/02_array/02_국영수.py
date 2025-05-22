# 10825 국영수
'''
문제
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 
이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 
(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

입력
첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다.
점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다. 
이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

출력
문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.
'''
#8:14

num_students = int(input())

def sorting_grades(n):
    student_profiles = []
    
    for _ in range(num_students):
        # # 아하 map 안쓰고 이렇게도 가능!
        # name, korean, english, math = input().split()          
        # grade_k, grade_e, grade_m = int(korean), int(english), int(math)
        # student_profiles.append((name, grade_k, grade_e, grade_m))
        
        # 또는 unpacking(*) 이용해서
        name, *grades = input().split()
        student_profiles.append((name, *map(int, grades)))      # 괄호....후...
    
    # !!! lambda 사용 다 까먹음 !!!
    # sorting by korean grades(idx = 1)(descending)
    student_profiles.sort(key=lambda x : -x[1])
    
    # sort by english(idx = 2 )(ascending)
    student_profiles.sort(key=lambda x : (-x[1], x[2]))
    
    # sort by math(idx = 3)(descending)
    student_profiles.sort(key=lambda x: (-x[1], x[2],-x[3]))
    
    # sort by names(ascii)
    student_profiles.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
    
    
    return student_profiles


# print(sorting_grades(num_students))
Sorted_list = sorting_grades(num_students)
for ele in Sorted_list:
    print(ele[0])
    
# 9:52