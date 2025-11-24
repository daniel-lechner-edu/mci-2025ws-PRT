# 4.2 Umwandlung von Ganzzahlen (10 %)

Wandeln Sie die folgende Zahl vom Dezimalsystem ins Binär-, Oktal-, und Hexadezimalsystem um.

58(10)

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_4_2_solved = True
​
# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# Um Fehler in der Auswertung zu vermeiden, verzichten Sie bitte auf führende Nullen.
# exercise_4_2_result_a2 = "<58(10) als Binärzahl>"
# exercise_4_2_result_a8 = "<58(10) als Oktalzahl>"
# exercise_4_2_result_a16 = "<58(10) als Hexadezimalzahl>"
​
def convert_dec(n, base=None):

    if(n >= 0):
        binary = bin(n)[2:]
        octal = oct(n)[2:]
        hexa = hex(n)[2:].upper()
    else:
        # negative zahlen 8-bit
        binary = bin(n & 0xFF)[2:].zfill(8)
        octal = oct(n)[2:]
        hexa = hex(n)[2:].upper()

    # print(f"Binary:         {binary}")
    # print(f"Oktal:          {octal}")
    # print(f"Hexadecimal:    {hexa}")
    # print("---")

    if(base == 2):
        return binary
    elif (base == 8):
        return octal
    elif (base == 16):
        return hexa
​
# Datentyp: string
exercise_4_2_result_a2 = convert_dec(58, 2)
exercise_4_2_result_a8 = convert_dec(58, 8)
exercise_4_2_result_a16 = convert_dec(58, 16)
```
