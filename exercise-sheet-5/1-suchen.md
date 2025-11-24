# 5.1 Suchen (14%)

Implementieren sie eine Funktion, welche ein Integer-Array und einen Integer als Parameter übergeben bekommt, dieses Array dann nach dem übergebenen Integer durchsucht und im Falle eines Erfolgs den Index des gesuchten Integers im Array zurückgibt. Falls der Integer nicht gefunden wird, so soll None zurückgegeben werden. Falls der gesuchte Integer mehr als einmal im Array zu finden ist, dann soll der Index des ersten Auftretens zurückgegeben werden.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das untersucht werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Der Integer nach dem gesucht werden soll, wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Funktion soll den Index der gesuchten Zahl zurückgeben, oder "None" falls diese nicht gefunden werden konnte.
​
def search_array(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return None
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_1_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
# Damit Sie den Wert None in der Ausgabe sehen können, müssen Sie den Rückgabewert mit print() ausgeben.
​
print(search_array([1,2,3,3, 4,5 ,3 ], 3))
```
