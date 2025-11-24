# 4.3 Rechnen mit Ganzzahlen (10 %)

Führen Sie folgende Berechnungen mit Ganzzahlen durch.

## Lösen Sie die folgende Addition direkt im Binär-, Oktal-, und Hexadezimalsystem.

`29(10)+117(10)`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_3a_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# Um Fehler in der Auswertung zu vermeiden, verzichten Sie bitte auf führende Nullen.
# exercise_4_3_result_a2 = "<Summe als Binärzahl>"
# exercise_4_3_result_a8 = "<Summe als Oktalzahl>"
# exercise_4_3_result_a16 = "<Summe als Hexadezimalzahl>"
​

# Datentyp: string
exercise_4_3_result_a2 = convert_dec(29+117, 2)
exercise_4_3_result_a8 = convert_dec(29+117, 8)
exercise_4_3_result_a16 = convert_dec(29+117, 16)
```

## Lösen Sie die folgende Subtraktion direkt im Binärsystem. Verwenden Sie dazu das Zweier-Komplement und rechnen Sie mit 8-Bit Zahlen (Füllen Sie dazu die angegebenen Zahlen entsprechend auf). Geben Sie zusätzlich zum Ergebnis der Rechnung auch an, wie oft es zu einem Übertrag kommt.

`(−58(10))−29(10)`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_3b_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# exercise_4_3_result_b2 = "<Differenz als 8-Bit Binärzahl>"
# exercise_4_3_result_b10 = <Anzahl der Überträge als Dezimalzahl>
​
def count_carries(a, b):
    abin = a & 0xFF
    bbin = b & 0xFF
    carries = 0
    carry = 0

    for i in range (8):
        bita = (abin >> i) & 1
        bitb = (bbin >> i) & 1
        sumbits = bita + bitb + carry
        carry = sumbits > 1
        carries += carry

    return carries

# Datentyp: string
exercise_4_3_result_b2 = convert_dec(-58-29, 2)
# Datentyp: int
res = -58-29
exercise_4_3_result_b10 = count_carries(-58, 29)
```
