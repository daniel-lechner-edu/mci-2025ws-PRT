# 4.7 Rechnen mit Gleitkommazahlen im Binärsystem (10 %)

Lösen Sie die folgende Addition direkt im Binärsystem. Gegeben sind zwei binäre Gleitkommazahlen mit einfacher Genauigkeit im IEEE 754 Format. Stellen Sie Ihre Lösung ebenfalls in diesem Format dar.

`01000001001110010000000000000000+01000010101011011000000000000000`

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
def ieee754_to_float(binary):
    sign = -1 if binary[0] == '1' else 1
    exponent = int(binary[1:9], 2) - 127
    mantissa = 1.0
    for i, bit in enumerate(binary[9:], 1):
        if bit == '1':
            mantissa += 2**-i
    return sign * mantissa * (2**exponent)
​
def add_ieee754(bin1, bin2):
    float1 = ieee754_to_float(bin1)
    float2 = ieee754_to_float(bin2)
    result = float1 + float2

    ieee_result, _ = convert_ieee754(result)
    return ieee_result
​
​
# Datentyp: bool
exercise_4_7_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# exercise_4_7_result = "<Summe als binäre Gleitkommazahl mit einfacher Genauigkeit>"
​
# Datentyp: string
exercise_4_7_result = add_ieee754(
    "01000001001110010000000000000000",
    "01000010101011011000000000000000"
)
```
