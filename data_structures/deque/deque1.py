from collections import deque

print("\n-----Demonstrating Queue-----")
queue = deque(['name','age','gender'])
print(queue) # Output: deque(['name', 'age', 'gender'])


print("\n-----Appending Items Efficiently-----")
queue = deque([1,2,3])
queue.append(4) # insert value to the right end of deque
print(queue) # Output: deque([1, 2, 3, 4])

queue.appendleft(0)
print(queue) # Output: deque([0, 1, 2, 3, 4])


print("\n-----Popping Items Efficiently-----")
queue = deque([0,1,2,3,4])
queue.pop()
print(queue) # deque([0, 1, 2, 3])

queue.popleft()
print(queue) # deque([1, 2, 3])


print("\n-----Size of a deque-----")
queue = deque([1,2,3,4,5,6])
print(len(queue)) # 6


print("\n-----Front and Back of a deque-----")
queue = deque([1,2,3,4,5,6])
print(queue[0]) # 1
print(queue[-1]) # 6


print("\n-----Accessing Items in a deque-----")
queue = deque([1,2,3,3,4,2,4])
print(queue.index(4,2,5)) # 4

queue.insert(4, 10) # insert value 10 at the 5th position
print(queue) # deque([1, 2, 3, 3, 10, 4, 2, 4])

queue.remove(4) # removes the first occurrence of 4
print(queue) # deque([1, 2, 3, 3, 10, 2, 4])

print(queue.count(3)) # count the occurrences of 3, Output: 2


print("\n-----Different operations on deque-----")
queue = deque([1,2,3])
queue.extend([4,5,6])
print(queue) # deque([1, 2, 3, 4, 5, 6])

queue.extendleft([0,-1,-2]) 
print(queue) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6])

queue.reverse()
print(queue) # deque([6, 5, 4, 3, 2, 1, 0, -1, -2])

queue.rotate(-3) # rotates by 3 to left
print(queue) # deque([3, 2, 1, 0, -1, -2, 6, 5, 4])