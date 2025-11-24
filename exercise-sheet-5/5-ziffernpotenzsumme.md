# 5.5 Ziffernpotenzsumme (16%)

Die positive Ganzzahl 512
ist interessant (in der Mathematik nennt man eine Zahl interessant, wenn sie besondere Eigenschaften erfüllt) weil sie gleich der Ziffernsumme potentiert mit einer natürlichen Zahl ist: 5+1+2=8
, und 8^3=512
.

Ein anderes Beispiel ist `614656: 6+1+4+6+5+6=28`
, und `28^4=614656`

Implementieren Sie ein Programm, welches alle interessanten Zahlen (d.h. alle Zahlen, welche die oben demonstrierten Eigenschaften besitzt) innerhalb eines angegebenen Zahlenbereichs findet.

Beim Lösen solcher Aufgaben wendet man das Teile-und-Herrsche Prinzip an, d.h. man zerlegt ein komplexes Problem in mehrere leichter zu lösende Teilprobleme. Zur Erleichterung der Aufgabe haben wir das Zerlegen der Aufgabe in Teilprobleme für Sie schon vorgenommen:

1. Implementieren Sie die Funktion `get_digits(n)`, welche eine positive Ganzzahl n in die einzelnen Ziffern zerlegt und diese als Liste zurückgibt. Zum Beispiel, der Aufruf von `get_digits(13442)` liefert die Liste `[1, 3, 4, 4, 2]`. Die Reihenfolge der einzelnen Ziffern in dieser Liste ist dabei egal.
2. Implementieren Sie die Funktion `digit_power_sum(digits, power)`, welche die Summe der Ziffern in der übergebenen Liste (1.Argument) berechnet und mit dem angegebenen Exponenten (2. Argument) potentiert (Zur Berechnung der Potenz können Sie in Python den Operator `**` verwenden). Das Ergebnis wird anschließend zurückgegeben. Zum Beispiel, der Aufruf von `digit_power_sum([2, 3, 1], 3)` liefert als Ergebnis 216.
3. Implementieren Sie die Funktion is_interesting_number(n), welche die Funktion `get_digits(n)` verwendet, um die Zahl n in ihre Ziffern zerlegt. Anschließend wird `digit_power_sum(digits, power)` mit unterschiedlichen Exponenten aufgerufen und überprüft, ob das Ergebnis gleich der Zahl n ist. Wenn die Zahl interessant ist, soll True zurückgegeben werden, ansonsten False. Zum Beispiel, der Aufruf von `is_interesting_number(512)` liefert als Ergebnis True.
4. Implementieren Sie die Funktion `get_interesting_numbers(l, u)`, welche für alle Zahlen im Interval von l bis u (beide Grenzen inklusive) überprüft, ob diese interessant sind. Alle gefundenen interessanten Zahlen sollen als Liste zurückgegeben werden. Zum Beispiel, der Aufruf von `get_interesting_number(400, 600)` liefert als Ergebnis [512].

### Tipps:

- Zu 1: Verwenden Sie die Operatoren `%` und `//`.
- Zu 3:
  - Wenn die Ziffernsumme 1 ist, dann können Sie die dazugehörige Zahl ignorieren, da 1 potentiert mit irgendeinem Exponenten immer 1 ergibt.
  - Wenn die Ziffernpotenzsumme mit einem Exponenten e größer als die Zahl n ist, dann ist die Überprüfung aller Exponenten größer als e sinnlos, da deren Ziffernpotenzsumme immer größer als n sein wird.

```python
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl

def get_digits(n):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits

# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "digits" ist eine Liste von positiven Ganzzahlen und "power" ist eine positive Ganzzahl

def digit_power_sum(digits, power):
    return sum(digits) ** power

# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl

def is_interesting_number(n):

    if n <= 1:
        return False

    digits = get_digits(n)
    digit_sum = sum(digits)

    if digit_sum == 1:
        return False

    power = 1
    while True:
        result = digit_power_sum(digits, power)

        if result == n:
            return True

        if result > n:
            return False

        power += 1

# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "l" und "u" sind positive Ganzzahlen

def get_interesting_numbers(l, u):
    interesting = []
    for n in range(l, u+1):
        if is_interesting_number(n):
            interesting.append(n)
    return interesting

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_5_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
get_digits(13442)

# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
digit_power_sum([2, 3, 1], 3)

# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
is_interesting_number(513)

# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
get_interesting_numbers(19000, 1000000)
```
