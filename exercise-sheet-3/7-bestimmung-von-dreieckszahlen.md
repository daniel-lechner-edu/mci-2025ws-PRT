# 3.7 Bestimmung von Dreieckszahlen (15%)

Implementieren Sie eine Funktion, welche für die übergebene Zahl x bestimmt, ob diese Zahl eine Dreieckszahl ist. Wenn es sich um eine Dreieckszahl handelt, dann soll True zurückgegeben werden, ansonsten False.

Eine Dreieckszahl ist eine Zahl, die der Summe aller Zahlen von 1 bis zu einer Obergrenze n entspricht. Die 10 ist beispielsweise eine Dreieckszahl, da 1+2+3+4=10
, die 28 ist auch eine Dreieckszahl, da 1+2+3+4+5+6+7=28
.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die zu überprüfende Zahl wird an die untenstehende Funktion als Variable "x" übergeben.
# Der Rückgabewert soll entweder True oder False sein
​
def is_triangular(x):
    if x == 0:
        return True

    n = int((2*x)**0.5)
    return x > 0 and n * (n+1) // 2 == x
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_7_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
is_triangular(28)
```
