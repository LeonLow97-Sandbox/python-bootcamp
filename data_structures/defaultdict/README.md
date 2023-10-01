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