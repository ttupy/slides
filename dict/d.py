a = dict(one=1, two=2, three=3)
b = dict([("two", 2), ("one", 1), ("three", 3)])
d = {"three": 3, "two": 2, "one": 1}

print(a == b == d)    # True

print(len(d))   # 3

print(d["one"])  # 1
d["one"] = 5

d = {"three": 3, "two": 2, "one": 1}
print('one' in d)   # True
print('zero' in d)  # False
print(1 in d)       # False

print(d.keys())   # dict_keys(['three', 'two', 'one'])
print(type(d.keys()))  # <class 'dict_keys'>

print(d.values())  # dict_values([3, 2, 1])
print(type(d.values()))  # <class 'dict_values'>

print(d.items())  # dict_items([('three', 3), ('two', 2), ('one', 1)])
print(type(d.items()))  # <class 'dict_items'>

a = {"two": 2, "one": 1, "three": 3}
b = {"three": 3, "one": 1, "two": 2}
d = {"one": 1, "two": 2, "three": 3}

print(a == b == d)   # True

a = {'1': 1, '2': 2}
a[1] = 11
a[2] = 22
print(a)  # {'1': 1, '2': 2, 1: 11, 2: 22}

training = {
    'monday': {'10:00': 'run', '12:00': 'swim'},
    'wednesday': {'18:00': 'gym', 'late': 'walk'},
    'friday': {'morning': 'yoga'}}
print(training['friday']['morning']) # => yoga
training['thursday'] = {'night': 'powersleep'}
