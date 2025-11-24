# 4.6 Rechnen mit Festkommazahlen im Binärsystem (10 %)

Lösen Sie die folgende Addition direkt im Binärsystem. Verwenden Sie für Ihre Rechnung ein Format mit exakt 8 Vorkommastellen und exakt 8 Nachkommastellen. Geben Sie zusätzlich zum Ergebnis der Addition an, ob die erhaltene binäre Festkommazahl in diesem Format im Vorkommabereich korrekt dargestellt werden kann. Geben Sie auch an, wie oft es bei dieser Addition zu einem Übertrag kommt.

`103,8125(10)+168,675(10)`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_6_solved = True
​
def add_fixed(a, b, int_bits=8, frac_bits=8):

    def to_fixed_binary(n, int_bits, frac_bits):
        int_part = int(n)
        frac_part = n-int_part

        int_bin = bin(int_part)[2:].zfill(int_bits)
        frac_bin = ''

        for _ in range(frac_bits):
            frac_part *= 2
            bit = int(frac_part)
            frac_bin += str(bit)
            frac_part -= bit

        return int_bin + frac_bin

    bin_a = to_fixed_binary(a, int_bits, frac_bits)
    bin_b = to_fixed_binary(b, int_bits, frac_bits)

    carries = 0
    carry = 0
    result = ''

    for i in range(len(bin_a) -1, -1, -1):
        bit_sum = int(bin_a[i]) + int(bin_b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
        if carry:
            carries += 1
​
    int_fits = int(result[:int_bits], 2) < 2**int_bits and carry == 0

    return result[:int_bits] + '.' + result[int_bits:], int_fits, carries
​
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# exercise_4_6_result1 = "<Summe als Binärzahl>"
# exercise_4_6_result2 = <Exakte Darstellung Vorkommabereich ::= JA | NEIN>
# exercise_4_6_result3 = <Anzahl der Überträge bei der binären Addition als Dezimalzahl>
​
result, fits, carries = add_fixed(103.8125, 168.675, 8, 8)
​
​
# Datentyp: string
exercise_4_6_result1 = result
# Datentyp: bool
exercise_4_6_result2 = fits
# Datentyp: int
exercise_4_6_result3 = carries
```
