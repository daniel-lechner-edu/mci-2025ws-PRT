# 5.6 Fakultäten der Ziffern (16%)

Die Zahl 145 ist eine Zahl mit einer interessanten Eigenschaft: `1!+4!+5!=1+24+120=145`
.

Finden Sie die Summe aller Zahlen (bis zu einer gegebenen Obergrenze n), bei denen die Summe der Fakultäten ihrer Ziffern die Zahl selber ergibt.

Hinweis :1!=1 und 2!=2 sind nicht damit gemeint, da hier keine Summe gebildet wird.

Diesmal müssen Sie das Teile-und-Herrsche Prinzip selber anwenden. Versuchen Sie dieses Problem in Teilprobleme aufzuteilen und diese getrennt voneinander zu implementieren, bevor Sie dann am Ende die Teillösungen zu einem gesamten Programm zusammenfügen.

Tipp: Sie können bestehene Teillösungen von diesem Übungszettel und den Jupyter Notebook Sheets auf Sakai wiederverwenden.

Bonusaufgabe: Wie kann man die Berechnung beschleunigen?

```python
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl
# Rückgabewert: Ganzzahl
# Schreiben Sie bitte auch alle zusätzlichen Funktionen in diese Zelle und fügen Sie keine neuen Zellen hinzu.
​
def digits_factorial(n):
    def factorial(num):
        if num <= 1:
            return 1
        result = 1
        for i in range(2, num+1):
            result *= i
        return result

    def get_digits(num):
        if num == 0:
            return [0]
        digits = []

        while num > 0:
            digits.append(num % 10)
            num = num // 10
        return digits

    def is_digit_factorial_number(num):
        if num <= 2:
            return False

        digits = get_digits(num)
        factorial_sum = sum(factorial(d) for d in digits)
        return factorial_sum == num

    total = 0
    for i in range(3, n+1):
        if is_digit_factorial_number(i):
            total += i

    return total
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_6_solved = True
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
digits_factorial(1000)
```
