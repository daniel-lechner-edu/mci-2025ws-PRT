# 4.4 Umwandeln von Festkommazahlen ins Binärsystem (10 %)

Wandeln Sie folgende Festkommazahlen vom Dezimalsystem ins Binärsystem um. Verwenden Sie für Ihre Rechnung ein Format mit exakt 8 Vorkommastellen und exakt 8 Nachkommastellen. Geben Sie zusätzlich zum Ergebnis der Umwandlung an, ob die erhaltene binäre Festkommazahl in diesem Format korrekt dargestellt werden kann (sowohl im Vorkomma-, als auch im Nachkommabereich).

`103,8125(10)`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_4_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# exercise_4_4_result1 = "<Ergebnis der Umwandlung>"
# exercise_4_4_result2 = <Exakte Darstellung Vorkommabereich ::= True | False>
# exercise_4_4_result3 = <Exakte Darstellung Nachkommabereich ::= True | False>
​
def convert_fixed_point(n, int_bits=8, frac_bits=8):
    int_part = int(n)
    frac_part = n - int_part

    int_binary = bin(int_part)[2:]

    frac_binary = ''

    for _ in range(frac_bits):
        frac_part *= 2
        bit = int(frac_part)
        frac_binary += str(bit)
        frac_part -= bit

    int_fits = len(int_binary) <= int_bits
    frac_exact = frac_part == 0

    int_binary = int_binary.zfill(int_bits)

    return f"{int_binary}.{frac_binary}", int_fits, frac_exact
​
​
result, int_fits, frac_exact = convert_fixed_point(103.8125, 8, 8)
​
​
# Datentyp: string
exercise_4_4_result1 = result
# Datentyp: bool
exercise_4_4_result2 = int_fits
# Datentyp: bool
exercise_4_4_result3 = frac_exact
```
