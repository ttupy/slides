## Matemaatilised tehted
#### *math*

---

## Matemaatilised tehted

- Python toetab kõiki levinuid matemaatilisi operatsioone
- Paljud kasutavad Pythoni käsurida kalkulaatori asemel
- Numbrilised väärtused pole piiratud andmetüübiga
 - ehk siis saab "lõpmata" suurte arvudega opereerida

```python
print(7 + 5 / 2)   # 9.5
print(7 + 5 // 2)  # 9
print(324234234 * 234234234 ** 234) # 10210 ... 224 (1968 symbols)

```

@[1](Tavaline jagamine 5 / 2 annab tulemuseks 2.5)
@[2](Täisarvuline jagamine 5 // 2 annab tulemuseks 2 ehk täisosa)
@[3](Toetab suurte arvudega opereerimist - tulemuseks ligi 2000 kohaline arv)

---

## Matemaatilised tehted

- ``17 + 5 => 22``
- ``17 - 5 => 12``
- ``17 * 5 => 85``
- ``17 / 5 => 3.4``
- ``17 // 5 => 3``
- ``17 // 5.0 => 3.0``
- ``17 % 5 => 2``  jääk
- ``17 ** 3 => 4913``  astendamine

---

## Jääk

- ``%`` operaatorit kasutatakse jäägi arvutamiseks
- Tulemus näitab, kui palju jääb üle kahe arvu jagamisel
- Näiteks:
 - ``5 % 5 => 0``
 - ``6 % 5 => 1``
 - ``4 % 5 => 4``
 - ``-4 % 5 => 1``

--- 

## Keerukamad funktsioonid

- Keerukamad matemaatilised funktsioonid on kättesaadavad eraldi moodulist ``math``.
- Selleks, et neid kasutada, tuleb koodi algusesse kirjutada ``import math``

```python
import math

print(math.sin(math.pi / 2)) # 1.0
print(math.log2(64)) # 6.0
```

@[1](Impordime ``math`` mooduli, milles on abifunktsioonid)
@[3](Näiteks trigonomeetria funktsioonid ja ``PI`` väärtus)
@[4](Või näiteks logaritmi arvutamine)

---

## Viited

- https://ained.ttu.ee/pydoc/math.html
- https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
- https://docs.python.org/3/library/math.html

