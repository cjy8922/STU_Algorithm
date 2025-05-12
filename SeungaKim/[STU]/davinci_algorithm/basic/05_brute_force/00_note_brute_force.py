'''
BRUTE FORCE (== Finding Probability)
# bruth force -> 중2 수학
1. 조합(Combination)
    - 순서 상관 x -> (a, b) == (b, a)
        - 동일 조합 중복 불가
    - nCr
    - Python의 `itertools` 모듈 사용

    ```python
    from itertools import combinations
    
    data = ['a', 'b', 'c']
    result = list(combinations(data, 2))
    print(result)               # [('a', 'b'), ('a', 'c'), ('b', 'c')]
    ```
2. 순열(Permutation)
    - 순서 상관 o -> (a, b) != (b, a)
        - 순서 바뀐 동일 조합 중복 가능
    - nPr
    - Python의 `itertools` 모듈 사용

    ```python
    from itertools import permutations
    
    data = ['a', 'b', 'c']
    result = list(permutations(data, 2))
    print(result)                # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ...]
    ```
'''