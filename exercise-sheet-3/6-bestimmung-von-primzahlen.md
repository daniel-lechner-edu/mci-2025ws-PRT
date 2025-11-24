# 3.6 Bestimmung von Primzahlen (15%)

Implementieren Sie eine Funktion, welche für die übergebene Zahl x bestimmt, ob diese Zahl eine Primzahl ist. Wenn es sich um eine Primzahl handelt, dann soll True zurückgegeben werden, ansonsten False.

Mathematisch gesehen ist eine Primzahl eine natürliche Zahl, die größer als 1 und ausschließlich durch sich selbst und durch 1 teilbar ist.

Zur Überprüfung Ihrer Lösung finden Sie z.B. auf Wikipedia eine Liste von Primzahlen zum Testen.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die zu überprüfende Zahl wird an die untenstehende Funktion als Variable "x" übergeben.
# Der Rückgabewert soll entweder True oder False sein
​
def is_prime(x):
    if x < 2:
        return False

    for i in range (2, int(x**0.5) +1):
        if x % i == 0:
            return False

    return True
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_6_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
is_prime(-5)
```
