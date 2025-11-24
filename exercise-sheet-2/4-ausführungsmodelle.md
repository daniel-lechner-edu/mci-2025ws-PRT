# 2.4 Ausführungsmodelle (20 %)

Geben Sie zu jedem der folgenden Szenarien an, welches Ausführungsmodell Sie dafür einsetzen würden. Begründen Sie Ihre Wahl in wenigen Sätzen.

```python
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_4_solved = True
```

### Für Windows und für Linux soll ein Gerätetreiber für eine Webcam implementiert werden. Überlegen Sie sich noch zusätzlich, ob ein und derselbe Treiber für beide Betriebssysteme verwendet werden kann, oder ob für jedes Betriebssystem ein eigener Treiber implementiert werden muss (wenn ja, wieso).

Kompliliert - Treiber müssen direkt mit der Hardware kommunizieren können und müssen schnell sein. Deswegen brauchen wir hier nativen Code zb. C oder C++. Für jedes OS braucht man eigene Treiber. Windows und Linux nutzen hier komplett unterschiedliche Systeme. Hardware Ansteuerung ist zwar per se gleich, aber die Schnittstelle zum OS nicht.

### Es soll eine Simulations-Software zur Wettervorhersage implementiert werden. Diese Software besitzt sehr hohe Ressourcen-Anforderungen und sollte daher möglichst effizient und parallelisiert ausgeführt werden.

Kompiliert - Bei starten Ressourcenanforderungen braucht man oft maximale Performance. Komplierter Code (C/C++/Go/Rust) ist am schnellsten und lässt sich dennoch gut parallelisieren. Interpreter wären zu langsam.

### Es soll ein Embedded System zur Steuerung eines Personenaufzugs implementiert werden. Dabei gilt zu beachten, dass die vorhandenen Ressourcen durch die Hardware stark limitiert sind.

Kompleliert - Embedded Devices haben viel zu wenig Speicher und Rechenleistung. Komplelierter Code braucht keinen Interpreter oder keine VM und ist am effizietesten. Zudem ist das Entzeitverhalten oft wichtig.

### Es soll eine E-Mail Anwendung implementiert werden, welche sowohl auf Windows, als auch auf Linux und macOS eingesetzt werden kann. Außerdem soll jeder Benutzer in der Lage sein, möglichst einfach die Anwendung eigenhändig auf seine Anforderungen anzupassen und neue Features zu implementieren.

Interpretiert - zb. Typescript / Elektron - Write Once, Run everywhere.

### Angetrieben vom Erfolg der E-Mail Anwendung von oberhalb, beschließt eine weitere Organisation eine ähnliche Software zu entwickeln. Diese soll ebenfalls auf allen gängigen Betriebssystemen laufen, zudem jedoch diverse Features enthalten, welche die Einhaltung des Betriebsgeheimnisses erfordern. Infolgedessen ist es notwendig, dass Reverse Engineering möglichst erschwert wird.

Kompeliert - Schneller und schwerer für reverse-engineeren als interpretierter Code, da der Quellcode quasi nicht "offen da liegt"
