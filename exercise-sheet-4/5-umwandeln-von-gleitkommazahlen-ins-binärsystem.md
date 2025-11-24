# 4.5 Umwandeln von Gleitkommazahlen ins Binärsystem (10 %)

Wandeln Sie die folgende Gleitkommazahl vom Dezimalsystem ins Binärsystem um. Stellen Sie die Lösung als binäre Gleitkommazahl mit einfacher Genauigkeit im IEEE 754 Format dar. Geben Sie zusätzlich zum Ergebnis der Umwandlung an, ob die erhaltene binäre Gleitkommazahl in diesem Format korrekt dargestellt werden kann.

`−2,5∗10^(−2)`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
def convert_ieee754(n):
    sign = '1' if n < 0 else '0'
    n = abs(n)

    int_part = int(n)
    frac_part = n - int_part

    int_binary = bin(int_part)[2:] if int_part > 0 else ''

    frac_binary = ''

    for _ in range(150):
        frac_part *= 2
        bit = int(frac_part)
        frac_binary += str(bit)
        frac_part -= bit
        if frac_part == 0:
            break

    if int_binary:
        mantissa_full = int_binary[1:] + frac_binary
        exp = len(int_binary) -1

    else:
        first_one = frac_binary.index('1')
        mantissa_full = frac_binary[first_one + 1:]
        exp =- (first_one + 1)

    mantissa = mantissa_full[:23].ljust(23, '0')
    exp_binary = bin(exp + 127)[2:].zfill(8)

    exact = len(mantissa_full) <= 23
​
    return sign + exp_binary + mantissa, exact
# Datentyp: bool
exercise_4_5_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# exercise_4_5_result1 = "<Binäre Gleitkommazahl mit einfacher Genauigkeit>"
# exercise_4_5_result2 = <Exakte Darstellung ::= True | False>
​
result, exact = convert_ieee754(-2.5 * 10**-2)
# Datentyp: string
exercise_4_5_result1 = result
# Datentyp: bool
exercise_4_5_result2 = exact
```
