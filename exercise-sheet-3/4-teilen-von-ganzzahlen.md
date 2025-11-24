# 3.4 Teilen von Ganzzahlen (14%)

Implementieren Sie eine Funktion, welche für eine beliebige positive Integer-Zahl ermittelt, wie oft diese ohne Entstehung eines Restbetrages durch 2 geteilt werden kann (nur gerade Zahlen können ohne Restbetrag geteilt werden) und das Ergebnis anschließend zurückgibt. Verwenden Sie dazu die in Aufgabe 3.1 implementierte Funktion "is_odd".

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl die untersucht werden soll wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Variable "count" soll Ihre Lösung als Integer enthalten.
# Bitte achten Sie darauf die in Aufgabe 4.1 implementierte Funktion is_odd zu verwenden.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der Funktion is_odd aus.
​
def count_loop(x):
    count = 0;

    if is_odd(x):
        return 0

    return 1 + count_loop(x // 2)
​
    return count
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_3_4_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
count_loop(48)
```
