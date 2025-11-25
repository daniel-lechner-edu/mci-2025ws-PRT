# 6.1 Rekursive Bestimmung von ungeraden Zahlen (20%)

Implementieren Sie ein Programm, welches für jede beliebige natürliche Zahl bestimmen kann, ob diese ungerade ist. Falls eine Zahl ungerade ist, soll der Wahrheitswert "True" zurückgegeben werden. Falls es sich um eine gerade Zahl handelt, dann "False". Im Gegensatz zu Übungsblatt 4 soll der Algorithmus dieses Mal mit Hilfe einer Rekursion umgesetzt werden. Wählen Sie einen passenden Rekursionsschritt und Rekursionsanfang

Hinweis: Implementieren Sie Ihre Lösung als wechselseitige Rekursion. Definieren Sie sich hierzu eine passende zweite Funktion.

```python
# Definieren Sie Ihre eigene(n) Funktion(en) inklusive Parameter und Rückgabewerte.
# Achten Sie dabei darauf, dass der/die Funktionsaufruf/e der Zelle(n) unterhalb funktioniert/funktionieren.

def is_odd(n):
    if n == 0:
        return False
    return not is_odd(n-1)

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_6_1_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
is_odd(13)
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
is_odd(44)
```
