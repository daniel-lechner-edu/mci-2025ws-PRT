# 6.2 Rekursive ggT Berechnung (20%)

Implementieren Sie ein Programm, welches den größten gemeinsamen Teiler zweier natürlicher Zahlen berechnet. Die Berechnung soll rekursiv erfolgen und das Ergebnis soll als Integer zurückgegeben werden. Wählen Sie passende Rekursionsschritte und einen Rekursionsanfang.

```python
# Definieren Sie Ihre eigene(n) Funktion(en) inklusive Parameter und Rückgabewerte.
# Achten Sie dabei darauf, dass der/die Funktionsaufruf/e der Zelle(n) unterhalb funktioniert/funktionieren.
​
def ggt(a, b):
    if b == 0:
        return a
    return ggt(b, a % b)

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_6_2_solved = False
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
ggt(18, 27)
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
ggt(35, 14)
```
