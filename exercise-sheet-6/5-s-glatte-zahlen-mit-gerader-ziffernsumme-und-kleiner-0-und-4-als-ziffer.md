# 6.5 S-glatte Zahlen mit gerader Ziffernsumme und keiner 0 und 4 als Ziffer (20%)

Die folgende Aufgabe wurde letztes Jahr bei der Klausur gestellt.

Eine 𝑆
-glatte Zahl bezüglich einer Schranke 𝑆
ist eine natürliche Zahl, in deren Primfaktorzerlegung (d.h. Menge der Primfaktoren) keine Primzahlen vorkommen, die größer als die Schranke 𝑆
sind. Beispiele für 5-glatte Zahlen: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, ...

Eine Zahl 𝑝
heißt Primfaktor einer natürlichen Zahl 𝑛
, wenn 𝑝
ein Teiler von 𝑛
ist und 𝑝
eine Primzahl ist. 𝑝
und 𝑛
können dabei identisch sein (z.B. 7 ist Primfaktor von 7).

Primzahlen sind natürliche Zahlen, die größer als 1 und ausschließlich durch sich selber oder durch 1 teilbar sind. Beispiele für Primzahlen sind 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, ...

Implementieren Sie in Python eine Funktion G( 𝑆
, 𝑛
, 𝑚
), die alle 𝑆
-glatten Zahlen mit gerader Ziffernsumme im Bereich von 𝑛
bis 𝑚
(beide Grenzen sind inklusive) findet, bei denen die Null und die Vier als Ziffer nicht vorkommen, und die Summe der gefundenen Zahlen zurückgibt.

Beispiel: G(7, 100, 300) = 112 + 125 + 189 + 192 + 196 + 288 = 1102

```python
# Implementieren Sie in dieser Zelle Ihr gesamtes Programm.
# Code außerhalb dieser Zelle wird bei der Bewertung nicht berücksichtigt.
# Die Funktion A soll Ihre Lösung als Integer zurückgeben.
# Definieren Sie, falls erforderlich, Ihre eigene(n) Funktion(en) inklusive Parameter und Rückgabewerte.
​
​
def G(S, n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
        return factors

    def has_zero_or_four(num):
        return '0' in str(num) or '4' in str(num)

    def digit_sum_is_even(num):
        return sum(int(digit) for digit in str(num)) % 2 == 0

    s_smooth_numbers = []
    for i in range(n, m + 1):
        factors = prime_factors(i)
        if all(factor <= S for factor in factors):
            if digit_sum_is_even(i) and not has_zero_or_four(i):
                s_smooth_numbers.append(i)

    return sum(s_smooth_numbers)

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_6_5_solved = False
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
G(7, 100, 300)
```
