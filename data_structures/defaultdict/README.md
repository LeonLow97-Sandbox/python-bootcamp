# Dictionary

- [Defaultdict in Python](https://www.geeksforgeeks.org/defaultdict-in-python/?ref=lbp)
- Dictionary in Python is an **unordered** collection of data values that are used to store data values like a map.
- Unlike other data types that hold only single value as an element, the Dictionary holds **key-value** pair.
- In Dictionary, the key must be unique and immutable.
  - This means that a Python Tuple can be a key whereas a Python List cannot.
- A Dictionary can be created by placing a sequence of elements within curly braces `{}`, separated by commas.

```py
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
print(Dict[1])

# Output:
# {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# Geeks
```

- If you try to access a key that does not exist in a Python dictionary, a `KeyError` is raised and it might become a problem.
- To overcome this, Python introduces another dictionary like container known as `defaultdict` which is present inside the `collections` module.

```py
print(Dict[4])

# Output:
'''
Traceback (most recent call last):
  File "/home/1ca83108cc81344dc7137900693ced08.py", line 11, in
    print(Dict[4])
KeyError: 4
'''
```

# `defaultdict`

- `defaultdict` is a container like dictionaries present in the `collections` module.
- `defaultdict` is a sub-class of the dictionary class that returns a dictionary-like object.
- The functionality of both dictionaries and `defaultdict` are almost same except that `defaultdict` never raises a `KeyError`. It provides a default value for the key that does not exist.
- Syntax: `defaultdict(default_factory)`
  - `default_factory`: A function returning the default value for the dictionary defined. If this argument is absent, the dictionary raises a `KeyError`.

# Common Methods of `defaultdict` and time complexity

| Methods | Time Complexity | Description |
| :-----: | :-------------: | ----------- |
|`defaultdict.get(key)`|O(1)|Returns the value of the specified key|
|`defaultdict.items()`|O(1)|Returns the dictionary's key-value pairs as tuples|
|`defaultdict.values()`|O(1)|Returns the dictionary's values|
|`defaultdict.keys()`|O(1)|Returns the dictionary's keys|
|`defaultdict.pop(key, default=None)`|O(1) if the key is present, O(n) in the worse case|Removes the specified key and returns its value, or returns the default value if the key is not found|
|`defaultdict.popitem()`|O(1)|Removes and returns an arbitrary key-value pair as a tuple|
|`defaultdict.clear()`|O(1)|Removes all items from the defaultdict|
|`defaultdict.copy()`|O(n)|Returns a shallow copy of the default dict|
|`key in defaultdict`|O(1)|Returns True if the key is in the dictionary, False otherwise|