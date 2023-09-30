# Deque

- Deque (Double Ended Queue) is implemented using `collections` module.
- Deque is preferred over a list in cases where we need faster append and pop operations from both ends of the container, as deque provides:
  - `O(1)` time complexity for **append** and **pop** operations.
- Compared to a list that provides `O(n)` for pop operation.
  = [GeeksForGeeks](https://www.geeksforgeeks.org/deque-in-python/)

# Methods of Deque and Time Complexity

|         Methods          | Time Complexity | Description                                                                         |
| :----------------------: | :-------------: | ----------------------------------------------------------------------------------- |
|        `append()`        |      O(1)       | insert value to the right of the deque                                              |
|      `appendleft()`      |      O(1)       | insert value to the left of the deque                                               |
|         `pop()`          |      O(1)       | remove element from the right of the deque                                          |
|       `popleft()`        |      O(1)       | remove element from the left of the deque                                           |
|      `len(dequeue)`      |      O(1)       | get the current size of the deque                                                   |
|        `Deque[0]`        |      O(1)       | access the first element of the deque with `q[0]`                                   |
|       `Deque[-1]`        |      O(1)       | access the last element of the deque with `q[-1]`                                   |
| `index(val, start, end)` |      O(N)       | get first index of the value stated, starting search from start index to end index. |
|    `insert(idx, val)`    |      O(N)       | inserts the value at the specified index                                            |
|        `remove()`        |      O(N)       | removes the first occurrence of the value mentioned in the arg                      |
|        `count()`         |      O(N)       | counts the number of occurrences of the value mentioned in arg                      |
|    `extend(iterable)`    |      O(K)       | adds multiple values to the right of the deque                                      |
|  `extendleft(iterable)`  |      O(K)       | adds multiple values to the left of the deque                                       |
|       `reverse()`        |      O(N)       | reverse the order of deque elements                                                 |
|        `rotate()`        |      O(K)       | rotates the deque by the specified number in arg                                    |
