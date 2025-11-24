# 1.4 Regular Expressions zur Eingabeüberprüfung (25 %)

Sie wurden zur Erstellung eines Onlineshops beauftragt, bei welchem sich Kunden mit ihrer Email-Adresse registrieren können. Um fehlerhafte Einträge gar nicht erst in die Datenbank aufzunehmen, soll bei der Eingabe überprüft werden, ob es sich um eine gültige Email-Adresse handelt. Lösen Sie dies mithilfe einer Regular Expression.

Um die Aufgabe besser verstehen zu können, folgt zunächst eine kurze Einführung in die Syntax von Email-Adressen.

Eine Email-Adresse muss auf eine Domain verweisen, was durch das @-Symbol erreicht wird. Die Domain (alles hinter dem @-Symbol) besteht wiederum aus einem Hostnamen (z.B. mci4me), einer Top-Level-Domain (z.B. at) und ggf. einer Second-Level-Domain (z.B. bei .co.uk -> .co stellt in diesem Fall die Second-Level-Domain dar). Die Second-Level-Domain ist also optional und muss nicht zwangsläufig vorkommen! Sowohl Top-, als auch Second-Level-Domain sind strikt nicht-numerisch und bestehen daher ausschließlich aus lateinischen Kleinbuchstaben von a bis z (keine Umlaute, kein ß). Der Hostname unterliegt folgenden Restriktionen:

- Groß- und Kleinbuchstaben (keine Umlaute, kein ß) dürfen verwendet werden.
- Zahlen von 0-9 dürfen verwendet werden.
- Bindestriche (-) dürfen verwendet werden, sofern diese NICHT zu Beginn oder am Ende des Hostnamens stehen.
- Zusammenfassend besteht die Domain demnach aus drei Teilen - dem Hostnamen (mci4me), einer Second-Level-Domain (.co) und einer Top-Level-Domain (.uk). Die komplette Domain, inklusive dem @-Symbol würde also so lauten: @mci4me.co.uk. Wie aus dem Beispiel schön hervorgeht können Zahlen lediglich im Hostnamen vorkommen, nicht aber in der Second- bzw. Top-Level-Domain.

Beim lokalen Teil der Email-Adresse (vor dem @-Symbol) sind folgende Zeichen zulässig:

- Groß- und Kleinbuchstaben (keine Umlaute, ß)
- Zahlen von 0-9
- Diese Sonderzeichen: &+-=\_~
- Punkte, sofern diese NICHT zu Beginn oder am Ende des lokalen Teils stehen

Hinweis: Die oben beschriebene Syntax spiegelt nicht exakt die Realität wieder, sondern eine Vereinfachung zum Zwecke dieser Übungsaufgabe. Detaillierte Informationen zur "Beschaffenheit" von Email-Adressen finden Sie hier.

## Antwort

```python
# Beantworten Sie die Frage, indem Sie den korrekten String für die RegEx als Wert der Variable
# 'exercise_1_4_result' angeben. Eine Beispielantwort sieht so aus:
#
#         exercise_1_4_result = r"(\d{3}) (.*)"
#
# Bitte vergessen Sie nicht, Ihre Antwort mit Anführungszeichen zu umgeben und vor das erste Anführungszeichen
# ein 'r' zu schreiben, so wie im obigen Beispiel zu sehen ist.
#
# Für Interessierte: das 'r' vor dem Anführungszeichen kennzeichnet in Python einen sog. Raw String (siehe
# https://www.journaldev.com/23598/python-raw-string). Dadurch muss man den Backslash \ nicht zusätzlich escapen.

# Datentyp: string

#

local_part = r"^[A-Za-z0-9&+\-=_~]+(\.[A-Za-z0-9&+\-=_~]+)*"
hostname = r"[A-Za-z0-9]+([A-Za-z0-9\-]*[A-Za-z0-9])?"
second_level = r"(\.[A-Za-z0-9]+)?"
top_level = r"\.[a-z]+"

exercise_1_4_result = rf"^{local_part}@{hostname}{second_level}{top_level}$"


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_4_solved = True
```
