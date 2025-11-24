# 1.1 Backus Normalform (25 %)

Welche der untenstehenden Möglichkeiten wird von der folgenden Backus Normalform abgedeckt?

```
<mathFunction> ::= <string> "(" <number> <operation> <number> ")"
<functionName> ::= <string> | <string> "." <string>
<string> ::= <char> | <char> <string>
<char> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<operation> ::= "+" | "-" | "*" | "/"
<number> ::= <integer> | <float>
<integer> ::= <digit> | <digit> <integer>
<float> ::= <integer> "." <integer>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

Optionen:

```txt
a) print(4+9)
b) calc(13/7)
c) abs(12)
d) math.sqrt(62+2)
e) abs(23-65)
f) quadriere(19*7)
g) groesserHundert(13.37+86.63)
h) dividiertDurch0(12*3)
```

# Antwort

```
# Beantworten Sie die Frage, indem Sie die KORREKTEN Antworten in die unten stehende Liste einfügen.
# Sind Ihrer Meinung nach die Antworten 'a', 'c' und 'e' korrekt, so sollte das Ergebnis **genau so** aussehen:
#
#         exercise_1_1_result = ["a", "c", "e"]
#
# Bitte vergessen Sie nicht, die einzelnen Antworten mit Anführungsstrichen zu umgeben
# und durch Beistriche zu trennen, so wie es im obigen Beispiel zu sehen ist.

# Datentyp: list of strings
exercise_1_1_result = ["a", "b", "e", "f", "g", "h"]

# c -> fehlender operator
# d -> punkt im func name

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_1_solved = True
```
