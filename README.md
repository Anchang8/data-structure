### Stack(2020/04/20)
#### 스택은 LIFO(Last In First Out) 즉, 후입선출 구조이다. 파이썬에서는 list와 내장함수를 이용해 간단히 구현가능.
기능: push(스택의 맨끝에 값을 삽입), pop(스택의 맨 끝 값 삭제), top/peek(스택의 맨 끝 값 반환), empty(스택이 비어 있는지 확인), size(스택의 크기 반환)

설명: 파이썬의 내장함수 append를 이용하여 push를 구현할 수 있고, pop함수를 이용해 pop을 구현가능하지만, pop 함수를 사용하지않고 구현해보았다.
# ![stack](https://user-images.githubusercontent.com/61732687/79726849-68e42700-8326-11ea-8a1b-d16e19d4279f.png)

## Queue(2020/04/20)
#### 큐는 스택과 반대로 FIFO(First In First Out) 즉, 선입선출 구조. 파이썬에서 Queue모듈을 이용해 구현가능하지만, 사용하지않고 구현함.
기능: enqueue(큐의 앞에 값을 삽입),dequeue(큐의 맨 끝 값 삭제), front/peek(큐의 맨 앞 값 반환), empty(큐가 비어 있는지 확인), size(큐의 크기 반환)

설명: 파이썬의 Queue모듈을 이용하면, Queue.put()이 enqueue의 기능을 수행하고, Queue.get()이 dequeue의 기능을 수행한다. 

# ![queue](https://user-images.githubusercontent.com/61732687/79749224-cb9aea00-8349-11ea-9e25-d68e52ed517b.png)

## deque(2020/04/22)
#### 덱 혹은 데크,는 Queue와 Stack의 기능을 합친것이다. From collections import deque로 사용가능.
기능: append(덱의 끝에 값을 추가), appendleft(덱의 앞에 값을 추가),pop(덱의 맨 끝 값 삭제), popleft(덱의 맨 앞 값 삭제), isempty(큐가 비어 있는지 확인) 등등 built-in Function들이 많다.

설명: 백준의 문제를 풀다보니, 큐를 이용하는 문제인데 시간초과가 자꾸 되서, 덱을 써 소비시간을 줄여 풀었다. 

# ![queue_stack_deque](https://user-images.githubusercontent.com/61732687/79951845-69122d00-84b4-11ea-9483-3d66accafdf5.png)


