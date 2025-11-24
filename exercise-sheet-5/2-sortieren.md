# Sortieren (14%)

Implementieren sie eine Funktion, welche ein unsortiertes Integer-Array als Parameter übergeben bekommt, dieses dann sortiert und wieder zurückgibt. Verwenden Sie dazu den Sortieralgorithmus "Selectionsort". Wird True als zweiter Parameter an die Funktion übergeben, dann soll das Array aufsteigend sortiert werden, wird False übergeben, dann absteigend.

Hinweis: Selectionsort lässt sich am einfachsten implementieren, wenn Sie mit zwei getrennten Arrays S und U (gleiche Notation wie im verlinkten Wikipedia-Artikel) arbeiten. Dann brauchen Sie auch keine Vertausche-Funktion.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das sortiert werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Besitzt der Parameter "asc" den Wahrheitswert "True", dann soll ein aufsteigend sortiertes Array zurückgegeben werden.
# Besitzt der Parameter "asc" den Wahrheitswert "False", dann soll ein absteigend sortiertes Array zurückgegeben werden.
# Die Funktion soll das sortierte Array zurückgeben.
​
def selection_sort(array, asc):
    # DEINE ANTWORT HIER
    S = []
    U = array.copy()

    while U:
        extreme = min(U) if asc else max(U)
        S.append(extreme)
        U.remove(extreme)

    return S

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_2_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
selection_sort([2,4,6,5,3,1], True)
```
