# 3.2 Summenberechnung (14%)

Implementieren Sie eine Funktion, welche bei der Zahl 3 startet und jede fünfte Zahl, die noch kleiner als die übergeben Zahl x ist, zu der bisherigen Summe (d.h. 3 + 8 + 13 + 18 + ...) hinzuaddiert. Am Ende soll die Summe dieser Berechnung zurückgegeben werden.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Variable "sum" soll die Lösung als Integer enthalten.
​
def my_sum(x):
    sum = 0

    for i in range (3, x, 5):
        sum += i

    return sum
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_2_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
my_sum(132)
```
