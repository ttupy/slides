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

@div[left-50 fragment]
```python
print("Start")
hello()
print("Between")
hello_name("Karumõmm")
print("End")
```
@divend

@div[right-50 fragment]
```
Start
Hello world!
Between
Hello, Karumõmm
End
```
@divend

---

## Viiteid

- https://ained.ttu.ee/pydoc/func_overview.html
- https://ained.ttu.ee/pydoc/func.html
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
