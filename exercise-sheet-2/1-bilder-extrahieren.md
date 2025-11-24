# 2.1 - Bilder extrahieren (40 %)

Sie möchten einen web crawler für eine Suchmaschine implementieren, welcher die Bilder von Webseiten speichert. Dabei soll nicht das Bild selbst heruntergeladen werden, sondern nur dessen Beschreibung, Dateityp und Link. Um diese Anforderung zu erfüllen, soll zuerst kurz darauf eingegangen werden, wie Bilder auf Webseiten dargestellt werden.

Webseiten werden mithilfe der Auszeichnungssprache HTML erzeugt, welche sogenannte HTML-Tags nutzt, um die Seitenstruktur aufzubauen. Bilder werden durch einen img-Tag repräsentiert, welcher folgendermaßen aussieht:

Beispiel: `<img src="img_chania.jpg" alt="Flowers in Chania">`
Erklärung: Der Tag wird durch eine Spitzklammer (Kleiner-Zeichen) geöffnet und mit dem Tagnamen img als Bild Identifiziert. Attribute (src und alt) stehen immer alleine - sie sind also durch Leerzeichen getrennt). Die Zuweisung eines Wertes zum Attribut erfolgt mit einem =. Bei den Werten handelt es sich um Strings (= Zeichenketten), was durch die Anführungszeichen (") festgehalten wird. Am Ende wird der Tag durch eine Spitzklammer geschlossen.

Das Attribut src verweist auf den Speicherort der Bilddatei, welche sich auf dem lokalen Webserver oder irgendwo im Internet befinden kann. Ganz am Ende des Links befindet sich immer die Dateiendung (in diesem Fall jpg), welche durch einen Punkt vom Rest der Adresse getrennt wird.

Das Attribut alt enthält eine alternative Beschreibung. Diese wird angezeigt, wenn die Quelldatei aus src nicht gefunden werden kann oder wenn die Seite durch einen Screenreader für Menschen mit eingeschränktem Sehvermögen vorgelesen wird.

## Ihre Aufgabe:

Ihr web crawler wird die Quelldateien von Webseiten analysieren und soll nun folgende Informationen von Bildern festhalten:

- Die Beschreibung (aus dem alt-Attribut)
- Das Dateiformat (die Dateiendung der Bilddatei)
- Den Link zur Bilddatei (aus dem src-Attribut)
- Setzen Sie diese Anforderungen mithilfe von Regular Expressions und deren Capturing Groups um.

Hinweise:

Sie müssen keinen web crawler entwickeln, sondern nur die Regular Expression für die oben beschriebene Aufgabe.
Sie können davon ausgehen, dass am Ende des Links immer ein Punkt und die Dateieindung (z. B. `.jpg` oder `.gif`) steht.
Wenn ein img-Tag kein alt-Attribut oder dieses einen leeren String (`alt=""`), soll das entsprechende Element nicht festgehalten werden - wir möchten nur Bilder mit Alternativbeschreibungen speichern!
Die Reihenfolge von src und alt ist beliebig - das oben beschriebene Bild könnte also auch so dargestellt werden:
`<img alt="Flowers in Chania" src="img_chania.jpg">`
Das Angaben zum img-Tag in HTML wurden zum Zwecke dieser Aufgabe vereinfacht.

## Antwort

```python

# Beantworten Sie die Frage, indem Sie den korrekten String für die RegEx als Wert der Variable 'exercise2_1'
# angeben. Eine Beispielantwort sieht so aus:
#
#         exercise_2_1_result = r"(\d{3}) (.*)"
#
# Bitte vergessen Sie nicht, Ihre Antwort mit Anführungszeichen zu umgeben und vor das erste Anführungszeichen
# ein 'r' zu schreiben, so wie im obigen Beispiel zu sehen ist.
#
# Für Interessierte: das 'r' vor dem Anführungszeichen kennzeichnet in Python einen sog. Raw String (siehe
# https://www.journaldev.com/23598/python-raw-string). Dadurch muss man den Backslash \ nicht zusätzlich escapen.

# Datentyp: string

src_pattern = r'src="([^"]+\.(\w+))"'
alt_pattern = r'alt="([^"]+)"'
spacing = r'\s+'

exercise_2_1_result = r'<img\s+(?:' + src_pattern + spacing + alt_pattern + '|' + alt_pattern + spacing + src_pattern + r')[^>]*>'

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_1_solved = True
```
