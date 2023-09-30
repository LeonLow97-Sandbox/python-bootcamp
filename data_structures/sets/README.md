# Sets

- A Set is an **unordered** collection data type that is
  - iterable,
  - mutable and
  - has no duplicate elements.
- Sets are represented by `{}` (values enclosed in curly braces).
- The major advantage of using a set, as opposed to a list, is that it has a highly **optimized method for checking whether a specific element is contained in the set**.
  - This is based on a data structure known as a hash table.
- Since sets are unordered, we cannot access items using indexes as we do in lists.

# Set Methods and Time Complexity

|      Methods       | Time Complexity  | Description                                           |
| :----------------: | :--------------: | ----------------------------------------------------- |
|   `add(element)`   |       O(1)       | Adds an element to the set                            |
| `update(iterable)` | O(len(iterable)) | Adds elements from an iterable to the set             |
| `remove(element)`  |       O(1)       | Removes a specified element from the set              |
| `discard(element)` |       O(1)       | Removes a specified element from the set if present   |
|      `pop()`       |       O(1)       | Removes and returns an arbitrary element from the set |
|     `clear()`      |       O(1)       | Removes all elements from the set                     |
|      `copy()`      |       O(n)       | Creates a shallow copy of the set                     |

# Uncommon set methods and time complexity

# Set Methods Time Complexity

|              Method               |       Time Complexity        | Description                                                             |
| :-------------------------------: | :--------------------------: | ----------------------------------------------------------------------- |
|        `union(other_set)`         |   O(len(set1) + len(set2))   | Returns a new set with elements from both sets.                         |
|     `intersection(other_set)`     | O(min(len(set1), len(set2))) | Returns a new set with common elements.                                 |
|      `difference(other_set)`      |         O(len(set1))         | Returns a new set with elements in the first set but not in the second. |
| `symmetric_difference(other_set)` |   O(len(set1) + len(set2))   | Returns a new set with elements in either set, but not in both.         |
|             `copy()`              |             O(n)             | Creates a shallow copy of the set.                                      |
|       `issubset(other_set)`       | O(min(len(set1), len(set2))) | Checks if the set is a subset of another set.                           |
|      `issuperset(other_set)`      | O(min(len(set1), len(set2))) | Checks if the set is a superset of another set.                         |
|      `isdisjoint(other_set)`      | O(min(len(set1), len(set2))) | Checks if two sets have no elements in common.                          |
|         Set Comprehension         |             O(n)             | Time complexity depends on the number of elements in the set.           |
|        Frozenset creation         |             O(n)             | Time complexity depends on the number of elements in the set.           |
