## ITI0102 - Programmeerimise algkursus
### Funktsioon
#### _Function_

---

## Funktsioon

@ul

- Funktsiooniga saab kirjeldada alamprogrammi või alamülesannet
- Funktsioon on koodiosa, mis täidab mingit konkreetset ülesannet või arvutab midagi
- Funktsioonil on (üldiselt) nimi

@ulend

---

## Funktsiooni kirjeldamine

- Funktsioon kirjeldatakse ära koos nime, valikuliste parameetrite ja funktsiooni kehaga (funktsiooni sisu kood)

```python
def hello():
    print("Hello world!")
```

@[1](Defineeritakse funktsioon, mille nimi on ``hello``)
@[2](Funktsiooni sisu ehk keha on taandega definitsiooni suhtes)

---

## Funktsioon argumendiga

- Funktsiooni defineerides võib kirjeldada parameetrid, millega saab funktsiooni juhtida

```python
def hello_name(name):
    print(f"Hello {name}!")
```

@[1](Parameeter ``name``, mida saab funktsiooni sees kasutada muutujana)
@[2](Funktsiooni sisu sõltub ``name`` väärtusest)

---

## Funktsiooni kasutamine

@ul

- Funktsiooni saab välja kutsuda (käivitada) nimega
- Kui definitsioon eeldab argumente (deklareeritud parameetrid), tuleb need kaasa anda

@ulend

```python
hello()

hello_name("Guido")
```

@[1](Väljakutse ilma argumendita)
@[3](Väljakutse ühe argumendiga)

---

## Funktsiooni kasutamine

- Kui interpretaator jõuab funktsiooni väljakutseni, jääb koodi käivitamine sellel real pooleli
 - seejärel täidetakse ära funktsiooni sisu
 - kui funktsioon lõppeb, jätkatakse eelnevalt poolelijäänud realt

```python
print("Start")
hello()
print("Between")
hello_name("Karumõmm")
print("End")
```

- Vt siin: https://goo.gl/Mc7376

---

## Parameeter ja argument

@ul

- Parameeter on muutuja funktsiooni kirjelduses
- Argument on väärtus, mis funktsiooni saadetakse


```python
def hello_name(name):
    print(f"Hello {name}!")
    
hello_name("Marja-Liis")
```

@[1](``name`` on parameeter)
@[4](Väärtus ``"Marja-Liis"`` on argument)

---

## Tagastamine (``return``)

@ul

- Pythonis funktsioon alati tagastab midagi
- Tagastada saab ``return`` korraldusega
- Kui ``return`` korraldust pole, tagastab funktsioon ``None``

@ulend

```python
def triangle_area(a, h):
    return a * h / 2

s = triangle_area(10, 10)
print(s)
```

@[1](Defineeritakse funktsioon, mis saab kaks väärtust - algus ja kõrgus)
@[2](Funktsioon tagastab kolmnurga pindala)
@[4](Funktsiooni väljakutsudes saab tulemuseks arvutatud pindala, see pannakse muutujasse)

---

## Tagastamine (``return``)

- Tagastada võib ka mitu väärtust
- Tulemus tagastatakse ennikuna (_tuple_)

```python
def get_multipliers(eq):
    x2pos = eq.find("x2")
    a = int(eq[:x2pos].replace(" ", ""))
    b = int(eq[x2pos + 2:eq.find("x", x2pos + 1)].replace(" ", ""))
    c = int(eq[eq.find("x", x2pos + 1) + 1:].replace(" ", ""))
    return a, b, c

a, b, c = get_multipliers("3x2 + 3x - 4")
print(a, b, c)

multipliers = get_multipliers("2x2 - 12x + 3")
print(multipliers)
```

@[1](Funktsioon saab sisendiks sõne, milles on avaldis)
@[2-5](Funktsiooni sisu arvutab välja kordajad ``a``, ``b``, ``c``)
@[6](Funktsioon tagastab kolm väärtust)
@[8-9](Funktsiooni väljakutsel võib väärtused panna eraldi muutujatesse: ``3 3 -4``)
@[11-12](Samuti võib need küsida ühte muutujasse, sellisel juhul muutujas on ennik ja selles on 3 väärtust: ``(2, -12, 3)``)

---

## Tagastamine (``return``)

- ``return`` korraldus lõpetab funktsiooni täitmise

```python
def get_university_name(abbreviation):
    if abbreviation == "TTU":
        return "Tallinna Tehnikaülikool"
    if abbreviation == "UT":
        return "Tartu Ülikool"
    if abbreviation == "TLU":
        return "Tallinna Ülikool"
    return "Unknown"
```

@[4,5](Siin pole vaj akasutada ``elif`` või ``else`` haru)
@[3-5](Kui esimene tingimus on tõene, rakendub ``return`` ja funktsioon lõpetab töö, seega pole eraldi ``else`` osa vaja.)

---

## Miks kasutada funktsioone?

@ul

- DRY - _don't repeat yourself_
 - korduva koodi asemel kasuta funktsiooni
 - funktsionaalsuse muutumise korral piisab ühe funktsiooni muutmisest
- Abstraktsioon
 - funktsiooni kasutaja ei pea teadma, kuidas funktsioon täpselt töötab
 -võimaldab suure programmi jagada alamülesanneteks, mida võivad lahendada erinevad inimesed
-Testimine
 - Kui programmis on vaid üks funktsioon main, saame testides teada, et probleem on kusagil selle funktsiooni sees
 - Kui programm on jagatud funktsioonideks, on võimalik igat funktsiooni eraldi testida
 - Sedasi saame vea asukoha ja põhjuse täpsemini tuvastada

@ulend

---

## Kuidas kasutada

@ul

- Funktsioon peaks tegema ühte konkreetset asja:
 - hea: ``get_area(...)``
 - üldiset halb: ``get_area_and_perimeter(...)``

- Funktsioon peaks olema piisavalt lühike/lihtne, et nimega saab öelda ära, mida see teeb:
 - hea: get_word_distribution_from_text
 - halb: foo, solve_problem, helper

@ulend

---

## Veel...

- Koodi on lihtsam kirjutada kui lugeda
- Hea programmeerija mõtleb sellele, et tema kood oleks hiljem ka teiste poolt loetav
 - võrdle juturaamatuga, hea autor on üldiselt see, kes suudab end lugejale selgeks teha
 - see ei tähenda, et iga rea juurde tuleks mitu rida kommentaari kirjutada
 - pigem on muutujad/funktsioonid/meetodid arusaadavalt nimetatud ja struktureeritud

---

## ``return`` _vs_ ``print()``

- ``return`` on spetsiifiline funktsiooni korraldus, mis tagastab funktsiooni tulemuse
- ``print()`` on lihtsalt üks korraldus (funktsioon), mida saab funktsiooni sisus kasutada (ja ka mujal)
 - samamoodi võib funktsioon näiteks kirjutada faili, saata emaili vms.

---

## ``return`` _vs_ ``print()``

```python
def triangle_area_print(a, h):
    print(a * h / 2)

area = triangle_area_print(10, 10)
print("area:", area)

def triangle_area(a, h):
    return a * h / 2

area = triangle_area(10, 10)
print("area:", area)
```

@[1,2](Funktsioon ei tagasta midagi, st tagastatakse ``None``)
@[2](Ekraanile prinditakse käivitamisel ``50``)
@[1-5](``area`` väärtuseks saab ``None``, miks?)
@[1-5](Ekraanile prinditakse ``area: None``)
@[7-8](See funktsioon tagastab arvutatud pindala)
@[7-11](``area`` väärtuseks on 50)
@[7-11](Ekraanile prinditakse ``area: 50.0``)

---
## ``return`` _vs_ ``print()``

```python
from time import sleep

def triangle_area(a, h):
    print(f"Got a: {a} and h: {h}")
    print("Calculating area...")
    sleep(1)
    area = a * h / 2
    print("Done!")
    print(f"Area is: {area}")
    return area

area = triangle_area(10, 10)
print(f"Area from function: {area}")
```

@[6](``sleep()`` ei ole vajalik, aga tekitab "vinge" efekti, nagu pindala arvutatakse pikalt)
@[3-10](See funktsioon tagastab pindala, aga lisaks sellele prinditakse jooksvalt teksti ekraanile. See on näide, kuidas ``print()`` korraldust võib funktsiooni sees kasutada, see midagi erilist ei tee. ``return`` aga lõpetab funktsiooni täitmise ära ja tagastab ``area`` väärtuse)

---

## Viiteid

- https://ained.ttu.ee/pydoc/func_overview.html
- https://ained.ttu.ee/pydoc/func.html
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
