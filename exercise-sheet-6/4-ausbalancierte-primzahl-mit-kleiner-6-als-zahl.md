# 6.4 Ausbalancierte Primzahl mit keiner 6 als Ziffer (20%)

Die folgende Aufgabe wurde vorletztes Jahr bei der Klausur gestellt.

Primzahlen sind natürliche Zahlen, die größer als 1 und ausschließlich durch sich selber oder durch 1 teilbar sind. Beispiele für Primzahlen sind `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, ...`

Eine ausbalancierte Primzahl (vom englischen "balanced prime") ist eine Primzahl `𝑝𝑛`
, welche exakt zwischen der vorherigen Primzahl `𝑝𝑛−1`
und der nachfolgenden Primzahl `𝑝𝑛+1`
liegt. Es gilt: `𝑝𝑛=(𝑝𝑛−1+𝑝𝑛+1)/2`
und `𝑝𝑛−𝑝𝑛−1=𝑝𝑛+1−𝑝𝑛`
. Beispiele für ausbalancierte Primzahlen sind `5, 53, 157, 173, 211, 257, 263, 373, ...`

Implementieren Sie in Python eine Funktion A(n, m), die alle ausbalancierte Primzahlen im Bereich von 𝑛
bis 𝑚
(beide Grenzen sind inklusive) findet, bei denen die Sechs als Ziffer nicht vorkommt, und die Summe der gefundenen Zahlen zurückgibt.

Beispiel: `A(100, 300)` = `157 + 173 + 211 + 257 = 798` (263 fällt weg, da die Ziffer 6 darin vorkommt).

```python
# Implementieren Sie in dieser Zelle Ihr gesamtes Programm.
# Code außerhalb dieser Zelle wird bei der Bewertung nicht berücksichtigt.
# Die Funktion S soll Ihre Lösung als Integer zurückgeben.
​
def A(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def has_six(num):
        return '6' in str(num)

    primes = [i for i in range(n-100, m+100) if is_prime(i)]
    balanced_primes = []

    for i in range(1, len(primes)-1):
        p_prev = primes[i-1]
        p_curr = primes[i]
        p_next = primes[i+1]

        if p_prev + p_next == 2 * p_curr:
            if n <= p_curr <= m and not has_six(p_curr):
                balanced_primes.append(p_curr)

    return sum(balanced_primes)

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_6_4_solved = False
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
​
​
A(100, 300)
```
