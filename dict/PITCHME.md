## ITI0102 - Programmeerimise algkursus
### Sõnastik
#### _dict_

---

## Sõnastik (_dict_)

- Järjendi (_list_) elemendid on järjestikuste arvudega positsioonidel (0, 1, 2, ..)
- Sõnastikus (_dict_) saab kasutada võtmena suvalisi arve ja sõnesid
 - täpsemalt kõiki muutumatuid (_immutable_) andmetüüpe
- Kasutatakse vastavuste loomiseks
- Sõnastik koosneb võti-väärtus (indeks-väärtus) paaridest

---

## Sõnastik (_dict_)

```python
a = dict(one=1, two=2, three=3)
b = dict([("two", 2), ("one", 1), ("three", 3)])
d = {"three": 3, "two": 2, "one": 1}

print(a == b == d)    # True

print(len(d))   # 3

print(d["one"])  # 1
d["one"] = 5
```

@[1-5](Kõik väljatoodud sõnastiku loomised annavad sama tulemuse)
@[3,7](``len`` tagastab võti-väärtus paaride koguse)
@[3,9](Kantsulgudega saab pöörduda konkreetse väärtuse poole (sulgudesse pannakse võtme väärtus))
@[3,10](Konkreetse väärtuse saab üle kirjutada)

---

## Sõnastik (_dict_)

```python
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
```

---

## Sõnastik (_dict_)

```python
a = {"two": 2, "one": 1, "three": 3}
b = {"three": 3, "one": 1, "two": 2}
d = {"one": 1, "two": 2, "three": 3}

print(a == b == d)   # True

a = {'1': 1, '2': 2}
a[1] = 11
a[2] = 22
print(a)  # {'1': 1, '2': 2, 1: 11, 2: 22}

d["one"] = 1
d["one"] = 2
print(d["one"])  # => 2
```

@[1-5](Järjekord ei ole oluline)
@[7-10](Andmetüüp on oluline. Võti '1' ja võti 1 on erinevad.)
@[12-14](Sama võtmega saab olla vaid üks väärtus)

---

## Sõnastik (_dict_)

- Väärtus võib omakorda sõnastik olla

```python
training = {
    'monday': {'10:00': 'run', '12:00': 'swim'},
    'wednesday': {'18:00': 'gym', 'late': 'walk'},
    'friday': {'morning': 'yoga'}}
print(training['friday']['morning']) # => yoga
training['thursday'] = {'night': 'powersleep'}
```

---

## Näide

```python
phones = {'politsei': '110', 'päästeamet': '112'}
print(phones)  # {'politsei': '110', 'päästeamet': '112'}
# one concrete element
print(phones['politsei'])  # 110
# add TTÜ phone
phones['ttü'] = '620 2002'
print(phones)  # {'politsei': '110', 'päästeamet': '112', 'ttü': '620 2002'}

# remove element
del phones['politsei']

print(phones)  # {'päästeamet': '112', 'ttü': '620 2002'}

```

---

## Näide

```python
for name, phonenumber in phones.items():
    print(name, phonenumber)

for name in phones:
    print(name, phones[name])

for day, day_dict in training.items():
    print(f"|{f'Training for {day}': ^24}|")
    for time, activity in day_dict.items():
        print(f"| {time: >9} | {activity: <11}|")
```

@[1-5](Kaks tsüklit prindivad täpselt sama tulemuse)
@[7-10](Koostab tabeli treeningutest)

---

## Viited

- https://ained.ttu.ee/pydoc/dict.html
- https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries