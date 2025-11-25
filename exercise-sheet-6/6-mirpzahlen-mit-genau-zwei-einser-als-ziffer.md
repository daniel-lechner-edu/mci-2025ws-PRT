# 6.6 Mirpzahlen mit genau zwei Einser als Ziffer (nicht benotet)

Die folgende Aufgabe wurde vorvorletztes Jahr bei der Klausur gestellt.

Mirpzahlen sind Primzahlen, die rückwärts gelesen eine andere Primzahl ergeben (mirp ist prim rückwärts geschrieben).

Ein Primzahlpalindrom wie z.B. 131 ist daher keine Mirpzahl, da sich rückwärts gelesen zwar ebenfalls eine Primzahl ergibt, aber keine andere, sondern dieselbe.

Primzahlen sind natürliche Zahlen, die größer als 1 und ausschließlich durch sich selber oder durch 1 teilbar sind. Beispiele für Primzahlen sind 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, ...

Die Eigenschaft Mirpzahl hängt vom verwendeten Zahlensystem ab, wir gehen daher vom Dezimalsystem aus.

Beispiele für Mirpzahlen im Dezimalsystem sind 13, 17, 31, 37, 71, 73, ...

Implementieren Sie in Python eine Funktion M(n, m), die alle Mirpzahlen im Bereich von 𝑛
bis 𝑚
(beide Grenzen sind inklusive) findet, bei denen genau zweimal ein Einser als Ziffer vorkommt, und die Summe der gefundenen Zahlen zurückgibt.

Beispiel M(100, 1100) = 113 + 311 + 1021 + 1031 + 1061 + 1091 = 4628

```python
# Implementieren Sie in dieser Zelle Ihr gesamtes Programm.
# Code außerhalb dieser Zelle wird bei der Bewertung nicht berücksichtigt.
# Die Funktion M soll Ihre Lösung als Integer zurückgeben.
# Definieren Sie, falls erforderlich, Ihre eigene(n) Funktion(en) inklusive Parameter und Rückgabewerte.
​
​
def M(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_mirp(num):
        reversed_num = int(str(num)[::-1])
        return num != reversed_num and is_prime(reversed_num)

    def has_exactly_two_ones(num):
        return str(num).count('1') == 2

    mirp_numbers = []
    for i in range(n, m + 1):
        if is_prime(i) and is_mirp(i) and has_exactly_two_ones(i):
            mirp_numbers.append(i)

    return sum(mirp_numbers)

# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
M(100, 1100)
```
