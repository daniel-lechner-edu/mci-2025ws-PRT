# 5.3 Summieren (14%)

Implementieren Sie eine Funktion, welche ein Array mit Elementen beliebiger Datentypen als Parameter übergeben bekommt. Iterieren Sie mit einer While-Schleife durch dieses Array, addieren Sie die Werte aller Elemente, die den Datentyp Integer besitzen, und geben Sie die Summe dieser Addition zurück. Falls kein Integer gefunden wurde, soll 0 zurückgegeben werden.

Hinweis: Normalerweise würde man in diesem Fall eine Mengenschleife verwenden, aber manche Programmiersprachen kennen keine Mengenschleife und wie man in so einem Fall vorgeht wollen wir hier üben.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das untersucht werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Die Funktion soll die Summe aller Integer im untersuchten Array zurückgeben.
​
def sum_array(array):
​
    i = 0
    summe = 0
    while i < len(array):
        if type(array[i]) == int:
            summe += array[i]
        i+=1
    return summe
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_3_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
sum_array(["Hello", 2, "World", True, 3, 4.5])
```
