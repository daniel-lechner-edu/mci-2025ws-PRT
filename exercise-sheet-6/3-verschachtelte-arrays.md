6.3 Verschachtelte Arrays (20%)
Implementieren Sie ein Programm, welches ein Array mit Elementen beliebiger Datentypen als Parameter übergeben bekommt. Addieren Sie die Werte aller Elemente, die den Datentyp Integer besitzen, und geben Sie die Summe dieser Addition zurück. Dabei sollen auch Integer in eventuellen verschachtelten Unterarrays beachtet werden. Für das Array [1, [2, [3]], 4.44, [5, ["Hallo", 6]]] beträgt die Summe aller Integer beispielsweise 17 (1 + 2 + 3 + 5 + 6). Die Berechnung soll rekursiv erfolgen. Falls kein Integer gefunden wurde, soll 0 zurückgegeben werden.

```python
# Definieren Sie Ihre eigene(n) Funktion(en) inklusive Parameter und Rückgabewerte.
# Achten Sie dabei darauf, dass der/die Funktionsaufruf/e der Zelle(n) unterhalb funktioniert/funktionieren.
​
def nested_sum(arr):
    total = 0
    for e in arr:
        if isinstance(e, int):
            total += e
        elif isinstance(e, list):
            total += nested_sum(e)
    return total

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_6_3_solved = False
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
nested_sum([5, [4, "3"], 4, [3, [2.5, [1, 1]]]])
```
