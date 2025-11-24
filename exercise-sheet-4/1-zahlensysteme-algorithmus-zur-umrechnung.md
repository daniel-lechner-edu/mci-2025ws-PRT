# 4.1 Zahlensysteme - Algorithmus zur Umrechnung (40 %)

Schreiben Sie eine Funktion convertNumber(n, B), welche die übergebene Dezimalzahl n in das Zahlensystem mit der Basis B konvertiert. Das Ergebnis soll in Form einer Zeichenkette zurückgegeben werden. Dies kann durch folgende Schritte erreicht werden:

1. Berechne n : B (n dividiert durch b) = y Rest z
2. Solange y > 0 (größer 0): Mache y zum neuen n und wiederhole Schritt 1.
3. Die Restwerte z ergeben von unten nach oben gelesen die gesuchte Zahlendarstellung.

Gehen Sie am besten folgendermaßen vor:

1. Berechnen Sie den Rest der Division.
2. Konvertieren Sie den Rest zu einem String und hängen Sie ihn an den bestehenden String aus Restwerten an.
3. Berechnen sie das neue "y"
4. Reversieren Sie den String

Zur Lösung der Aufgabe benötigen Sie folgende Informationen:

- Eine Zahl kann in Python mittels str(zahl) in einen String umgewandelt werden.
- Strings können mithilfe des + aneinandergereiht (= konkatenieren) werden - z.B. folgt aus x = "a" + "b" das Ergebnis x == "ab"
- Strings können wie folgt reversiert ("umgedreht") werden:
  - `result = "abc"`
  - `result = result[::-1]`
- Die Variable "result" enthält nun "cba"
- Man kann diese Aufgabe auch lösen, ohne den String am Ende umdrehen zu müssen. Finden Sie diese Lösung?

### Info: Die Umrechnung muss nur für Zahlensysteme der Basis kleiner 10 funktionieren.

```python
# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl, die umgewandelt werden kann wird an die untenstehende Funktion als "n" und die Basis des
# Zahlensystems als "B" übergeben.
# Die Variable "result" soll die Lösung als String enthalten.
​
def convertNumber(n, B):
    result = ''

    while n > 0:
        z = n % B
        result = result + str(z)
        n = n // B

    return result[::-1]
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_1_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
convertNumber(128, 2)
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
convertNumber(24, 8)
```
