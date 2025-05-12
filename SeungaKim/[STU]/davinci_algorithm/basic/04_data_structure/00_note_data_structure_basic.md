# 자료구조 간단 노트트

## 1. 배열 (Array)

- Python에서는 `array` 타입이 따로 존재하지 않음  
- **`list`가 곧 array처럼 사용됨**



## 2. 스택과 큐 (Stack and Queue)


### Stack

- **LIFO**
- Python  에서 **list 는 stack 과 같은** 형태
- **insert(#idx, value)** : 이용해서 원하는 위치에 딱 데이터 삽입할 수 있지만
- **append()** : 이용해서 마지막에 데이터 추가
- **pop()** : 그 마지막 데이터 꺼냄

### Queue

- **FIFO** 


### Deque (Double-Ended Queue)


- Stack + Queue 인 구조
 - 앞뒤로 데이터 추가/삭제 가능
    - 앞 : **appendleft(), popleft()**
    - 뒤 : **append(), pop()**
- time complexity : O(1)
  
- Python의 `collections` 모듈 사용

```python
from collections import deque
```


## 3. 우선순위 큐 (Priority Queue)

- 먼저 들어온 데이터보다 **우선순위가 높은 데이터가 먼저 나감**
- **응급실 느낌** ->  먼저 온 사람보다 상태 심각한 사람이 먼저 치료하듯이

### Heap (힙)

-  binary tree + priority queue

#### Min Heap (최소 힙)

-  parent node <= child node
- 'min' value at Root

#### Max Heap (최대 힙)

-  parent node >= child node
- 'max' value at Root
