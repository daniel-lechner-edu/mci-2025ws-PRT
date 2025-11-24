# 3.5 Division mit Rest (14%)

Implementieren Sie eine Funktion, welche die Division mit Rest für den Dividenten x und den Divisor y berechnet und zurückgibt.

Der Divisions-Operator / bzw. // und der Modulo-Operator % dürfen nicht verwendet werden.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Der Divident und der Divisor werden an die untenstehende Funktion als Variablen "x" und "y" übergeben.
# Die Variable "result" soll das Ergebnis der Division und die Variable "remainder" den Rest der Division enthalten.
​
def division_mit_rest(x, y):
    result = 0
    remainder = x

    while remainder >= y:
        remainder = remainder -y
        result = result +1

    return result, remainder
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_5_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
division_mit_rest(7, 2)
```
