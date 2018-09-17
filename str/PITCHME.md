## ITI0102 - Programmeerimise algkursus
### Sõne
#### _string_

---

## Sõne

- Sõne on objekt
- Sõne on sümbolite jada
- Sõne on muutumatu objekt
 - see tähendab, et sõne ei saa muuta
 - sõne operatsioonid loovad vajadusel uue sõne ja tagastavad selle

---

## Sõne

- Sõne loomine

```python
text = "example"
text = 'example'
text = """example"""
text = '''example'''
```

---

## Sõne loomine

```python
text = "don't do it"
text = 'don\'t do it'
text = "hello ""world"    # hello world
text = "hello " + 'world'  # hello world

```

@[1](Ülakoma kasutamine "" märkide vahel on lubatud)
@[2](Ülakoma kasutamine '' märkide vahel tuleb ülakoma varjestada (_escape_))
@[3](Pythonis võib kahe sõne kokkupanemiseks need lihtsalt ükteise otsa kirjutada)
@[3-4](Sõned võib kokku liita ka + märgiga - kaks rida annavad sama tulemuse)