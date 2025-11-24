# 3.3 Zahlenvergleich (14%)

Implementieren Sie eine Funktion, welche das Maximum und das Minimum von 6 Integer-Zahlen ermittelt und zurückgibt. Verwenden Sie dafür möglichst wenige Vergleiche zwischen den einzelnen Zahlen.

Die von Python bereitgestellten Funktionen min() und max() dürfen nicht verwendet werden.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahlen die sortiert werden sollen, werden an die untenstehende Funktion
# als Variablen "a", "b", "c", "d", "e" und "f" übergeben.
# Die Variablen "_min_" und "_max_" sollen die Lösungen als Integer enthalten.
​
def get_min_max(a, b, c, d, e, f):
    _max_ = a
    _min_ = a

    for val in [b, c, d, e, f]:
        if val > _max_:
            _max_ = val
        if val < _min_:
            _min_ = val

    return _min_, _max_
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_3_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
get_min_max(21, 23, 13, 44, 5, 26)
```
