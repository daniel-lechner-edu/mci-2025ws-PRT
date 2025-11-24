# 1.3 Regular Expressions (25 %)

Gegeben sei folgende RegEx:

```
^(00|\+)[0-9]{1,2} [\d]{1,3}( [\d]{2,3}){3}$
```

Welche der folgenden Eingaben werden zu einem "Match" führen?

```txt
a) 0043 660 12 34 567
b) +18660 19 33 147
c) +43 699 9838712
d) +43 512 2070 991
e) 0043 512 20 70 512
f) +987654321
g) +0 99 67 18 210
h) 0033 1 919 533 12
```

## Antwort

```python
# Beantworten Sie die Frage, indem Sie die KORREKTEN Antworten in die unten stehende Liste einfügen.
# Sind Ihrer Meinung nach die Antworten 'a', 'c' und 'e' korrekt, dann sollte das Ergebnis **genau so** aussehen:
#
#         exercise_1_3_result = ["a", "c", "e"]
#
# Bitte vergessen Sie nicht, die einzelnen Antworten mit Anführungsstrichen zu umgeben
# und durch Beistriche zu trennen, so wie es im obigen Beispiel zu sehen ist.

# Datentyp: list of strings

# ^ = Anfang
# (00|\+)         -> beginnt mit 00 oder +
# [0-9]{1,2}      -> 1-2 Zahlen
# [\d]{1,3}       -> 1-3 Zahlen
# ( [\d]{2,3})    -> 3x (Leerzeichen + 2-3 Zahlen)
# $               -> ende

# a) 0043 660 12 34 567  -> match
# b) +18660 19 33 147    -> kein leerzeichen nach den ersten zwei ziffern
# c) +43 699 9838712     -> nur 2 leerzeichen gruppen, braucht genau 3
# d) +43 512 2070 991    -> gruppe hat 4 ziffern, erlaubt sind 2-3
# e) 0043 512 20 70 512  -> match
# f) +987654321          -> keine leerzeichen
# g) +0 99 67 18 210     -> match
# h) 0033 1 919 533 12   -> match

exercise_1_3_result = ["a", "e", "g", "h"]

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_3_solved = True
```
