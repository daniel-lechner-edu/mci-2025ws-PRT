# 1.2 Erstellen einer Backus Normalform (25 %)

Erstellen Sie eine Backus Normalform (BNF), welche die folgenden drei URLs abdeckt:

```https://mars.mci4me.at:8000/test/test2/test3
http://www.google.com
https://www.mci.edu/en/university/the-mci/team-faculty
```

## Hinweise:

- `"/test/test2/test3"` bzw. `"en/university/the-mci/team-faculty"` beschreiben den Serverpfad (path). Dieser kann beliebig lang sein und besteht immer aus einem führenden Schrägstrich (/) und einem string (= Zeichenkette).
- `"http"` bzw. `"https"` bezeichnen das Protokoll (protocol).
- `":8000"` bezeichnet den angesteuerten Port (port). Dieser ist optional und wird meistens nicht angeführt.
- Sie müssen keine BNF erstellen, welche sämtliche URLs abdeckt, sondern nur die drei oben angeführten.
- Für Ihre Lösung bietet es sich an, die markierten Begriffe als Klassen der BNF zu verwenden.

Laden Sie Ihre Lösung als PDF-Datei mit dem Namen BNF.pdf auf JupyterHub hoch. Vergessen Sie nicht, das Übungsblatt mithilfe der Submit-Funktion abzugeben!
