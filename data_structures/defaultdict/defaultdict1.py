from collections import defaultdict

print("\n-----default_factory in defaultdict-----")
# Creating a defaultdict with a default value of int (default value is 0 for int)
d = defaultdict(int) # can be bool, int, str, etc.
d["a"] = 7
print(d["a"]) # 7
print(d["b"]) # 0 (default value for int)

def def_value():
    return "Not Found!"
d = defaultdict(def_value)
d["a"] = 7
print(d["b"]) # Not Found!
print(d.get("a")) # 7


print("\n-----defaultdict items(), values(), keys()-----")
myDict = defaultdict(int)
myDict['apple'] = 3
myDict['banana'] = 2
myDict['cherry'] = 5

print(myDict.items()) # dict_items([('apple', 3), ('banana', 2), ('cherry', 5)])
print(myDict.values()) # dict_values([3, 2, 5])
print(myDict.keys()) # dict_keys(['apple', 'banana', 'cherry'])


print("\n-----Removing items from defaultdict-----")
myDict['watermelon']  = 60
print(myDict) # defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 5, 'watermelon': 60})

popResult = myDict.pop("apple")
popItem = myDict.popitem() # removes and returns an arbitrary key-value pair as a tuple

print(popResult) # 3
print(popItem) # ('watermelon', 60)
print(myDict.clear()) # None


print("\n-----Shallow copy of defaultdict-----")
myDict = defaultdict(int)
myDict['apple'] = 3
myDict['banana'] = 2
myDict['cherry'] = 5

copyDict = myDict.copy()
print(copyDict) # defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 5})


print("\n-----Checking if a key is in a dictionary-----")
# Returns True if the key is in the dictionary, False otherwise
print("banana" in myDict)