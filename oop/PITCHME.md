## ITI0102 - Programmeerimise algkursus
### Objektid, klassid
#### _objects_, _classes_, OOP

---

## Objekt

- Objekt kirjeldab ära konkreetse loogilise kogumi
 - näiteks õues olev punane auto on üks objekt
 - selle taga olev roheline auto on teine objekt jne
- Tavaliselt mõtleme me arvust kui ühest väärtusest (nt 7)
- Objekt koosneb tavaliselt mitmest väärtusest
 - värv, mark, mudel, pikkus, registrimass jne
 
---

## Klass

- Klass kirjeldab ära struktuuri
 - näiteks autol on värv, pikkus jne
- Klass (üldiselt) ei sisalda andmeid
- Klass on andmetüüp
- Samatüüpi andmed pärinevad kõik ühest klassist
 - punane auto on auto, roheline auto on auto jne
- Kuigi meil on maailmas mitu autot (objekti), siis meil on üks klass auto

---

## OOP

- Objekt-orienteeritud programmeerimine (OOP) on programmeerimise paradigma, mis kasutab objekte

- Python on objekti-orienteeritud programmeerimiskeel (OOP)

- Pythonis kõik asjad on objektid

---

## Sõne

- Sõne on objekt
- Kui loote uue sõne, siis tegelikult luuakse uus objekt, mille tüüp on `str`.
- Sõne "funktsioone" kutsutakse meetoditeks
 - ehk siis klassis kirjeldatud funktsioonid on meetodid
 
 ```python
s = "Hello"
print(type(s))  # <class 'str'>
print(id(s))  # 30773472
print(id(s.replace("H", "h")))  # 61507648

```

@[1-2](Loome sõne `s` ja küsime selle tüübi. Tüüp on `str` klass)
@[1-3](`id` tagastab objekti kohta unikaalse arvu. Kui id on erinev, siis on ka objekt erinev (st mälus erinevas kohas))
@[1-4](`replace` teeb uue sõne, seda näeme ka `id`-ga)

---

## List

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(id(a))   # 44058024
a.append(4)
print(id(a))   # 44058024 still the same
print(id(b))   # 44059184
print(id(c))   # 44059184 - same as b
b.pop()
print(id(b))   # 44059184 - still the same
print(id(c))   # 44059184 - and same
```
@[1-3](Loome kolm listi)
@[1-7](List on _mutable_, seega elemendi lisamine muudab olemasolevat listi. `id` jääb samaks)
@[1-3,8,9](`b=c` puhul viitavad mõlemad samale objektile)
@[1-3,8-12](Ühe listi muutmine muudab mõlemat)

---

## Veel objekte

```python
print(type(1))     # <class 'int'>
print(type(True))  # <class 'bool'>
print(type(1.2))   # <class 'float'>
print(type(None))  # <class 'NoneType'>
print(type(len))   # <class 'builtin_function_or_method'>
print(type(type))  # <class 'type'>
```

---

## Klass kui andmetüüp

- Iga klass on andmetüüp
- Näiteks on Pythonis klass `str`
- Iga konkreetne sõne, näiteks `"tere"`, on selle klassi objekt (ehk isend)
- Ühest klassist saab luua lõpmata palju objekte
- Objekti kohta öeldakse ka isend ja instants
 - Üldiselt mõeldakse "objekt", "isend", "instants" terminitega samu asju
 - Erinevates allikates võivad neil mingid erinevused olla
 - Siin aines kasutame termineid objekt ja isend.
 
---

## Teeme oma klassi

- Väga lihtne klassi (andmetüübi) kirjeldus:

```python
class Student:
    pass

s = Student()
print(type(s))  # <class '__main__.Student'>
print(id(s))    # 12448112

t = Student()
print(type(t))  # <class '__main__.Student'>
print(id(t))    # 12423408
```
@[1-2](Kirjeldame ära klassi. `pass` ei tee midagi, see on vajalik tühja sisu puhul (nt funktsioonis, if-lauses jne). Klassil on nimi `Student`)
@[1-5](Loome uue isendi e objekti)
@[1-10](Loome teise isendi. Kuigi need isendid on ühte tüüpi, on nende `id` erinev, ehk mälus kahes kohas)

---

## Objektide võrdlemine

- Objektide võrdlemine `==` võrdlusega kontrollib vaikimisi seda, kas nad viitavad samale objektile
- Seda, mida täpselt kontrollitakse, saab üle kirjutada
- Näiteks sõne puhul kontrollitakse seda, kas sisu (st sümbolid) on samad jne

```python
s1 = Student()
s2 = Student()
s3 = s1

print(s1 == s2)   # False
print(s1 == s3)   # True
print(s2 == s3)   # False
```

---

## Meetod

- Klassis sisalduvaid funktsioone nimetatakse meetoditeks

```python
class Student:
    """Student class."""

    def hello(self):
        """Method (function) which just prints out "Hello!"."""
        print("Hello!")


s = Student()
s.hello()       # no "self" argument
```

@[1-7](Kirjeldame klassi `Student` ja sinna sisse meetodi (funktsooni) `hello`)
@[4](Meetodil on eriline parameeter `self`, millest räägime hiljem. Seda ei pea välja kutsudes kaasa andma.)
@[1-10](Loome objekti muutujasse `s` ja kutsume objektil välja meetodi `hello()`.)
@[1-10](Nagu näha, siin argumenti kaasa ei anna. )
