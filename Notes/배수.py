from collections import deque

n = int(input())

queue = deque([1])

while True:
    temp = queue.popleft()
    
    if temp%n ==0:
        print(temp)
        break
        
    queue.append(temp*10)
    queue.append(temp*10 +1)