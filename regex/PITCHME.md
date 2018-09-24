## ITI0102 - Programmeerimise algkursus
### Regulaaravaldis
#### _Regular expression_

---

## Regulaaravaldis

- Regulaaravaldis (_regular expression_) kirjeldab ära mustri (_pattern_)
- Mustrit saab kasutada otsinguks ja teksti asendamiseks
- Võimaldab rohkem kui "otsi alamsõne X tekstist Y"

---

## `re` moodul

```python

import re

match = re.search("abc", "aabca")
print(match.group())  # abc is found in text
match = re.search("xyz", "aabca")
print(match is None)  # no match

```

@[3](Otsitakse mustrit "abc" tekstist "aabca")

---

## Muster kui alamsõne

- Muster võib olla alamsõne, millele otsitakse täpset vastet tekstist
- Üldiselt sellisel juhul mõistlikum kasutada `sub in text` (kiirem)

Muster: `"abc"`

Sisalduv tekst: `"abc"`

Mittesisalduv tekst: `"ababac"`