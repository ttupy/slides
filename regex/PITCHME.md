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

---

## Suvaline sümbol

- Vastab ühele suvalisele sümbolile

Muster: `.`

Näide: `"`@css[u](`a.bc`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`a2bc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"abc"`)

---

## Algus

- Tähistab sõne algust

Muster: `^`

Näide: `"`@css[u](`^abc`)`"`

Sisalduv tekst: @css[match](`"`)@css[match-u](`abc`)@css[match](`d"`)

Mittesisalduv tekst: @css[nomatch](`"aabc"`)

---

## Lõpp

- Tähistab sõne lõppu

Muster: `$`

Näide: `"`@css[u](`abc$`)`"`

Sisalduv tekst: @css[match](`"aa`)@css[match-u](`abc`)@css[match](`"`)

Mittesisalduv tekst: @css[nomatch](`"abca"`)

---

## 0 või 1 kord

- Eelnevat sümbolit (või alammustrit) on 0 või 1 kord

Muster: `?`

Näide: `"`@css[u](`ab?c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`ac`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"aabbcc"`)


---

## 0 või rohkem kordi

- Eelnevat sümbolit (või alammustrit) on 0 või rohkem korda

Muster: `*`

Näide: `"`@css[u](`ab*c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`ac`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abbbc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"abab"`)

Mittesisalduv tekst: @css[nomatch](`"bbc"`)

---

## 1 või rohkem kordi

- Eelnevat sümbolit (või alammustrit) on 1 või rohkem korda

Muster: `+`

Näide: `"`@css[u](`ab+c`)`"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abc`)@css[match](`a"`)

Sisalduv tekst: @css[match](`"a`)@css[match-u](`abbbc`)@css[match](`a"`)

Mittesisalduv tekst: @css[nomatch](`"aac"`)

Mittesisalduv tekst: @css[nomatch](`"abbba"`)

---

## Varjestaaine (_escape_)

- Järgnevat erilist sümbolit tõlgenatakse ilma tähenduseta

Muster: `\`

Näide: `"a`@css[u](`\.`)`bc"`

Sisalduv tekst: @css[match](`"a`)@css[match-u](`.`)@css[match](`bc"`)

Mittesisalduv tekst: @css[nomatch](`"a`)@css[nomatch-u](`2`)@css[nomatch](`bc"`)
