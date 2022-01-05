# 큐 예제
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
# deque([3, 7, 1, 4])
queue.reverse()
# queue를 역순으로 바꿈
print(queue)


