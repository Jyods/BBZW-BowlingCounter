# Testkonzept für Bowling-Score-Berechnung

## Ziel
Das Ziel dieses Tests ist es, sicherzustellen, dass die Bowling-Score-Berechnungsfunktion ordnungsgemäß arbeitet und korrekte Punktzahlen für verschiedene Wurfszenarien zurückgibt.

## Testumgebung
- Programmiersprache: Python
- Testframework: unittest
- Testobjekt: Bowling-Score-Berechnungsfunktion in der Datei "Counter.py"

## Testfälle

### Testfall 1: Normale Punkteberechnung (TC001)
- **Beschreibung:** Überprüft die korrekte Berechnung der Punkte für normale Würfe.
- **Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 1, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
- **Erwartetes Ergebnis:** Die berechneten Punkte sollten der Summe der Wurfwerte entsprechen.

### Testfall 2: Strike gefolgt von Spare (TC002)
- **Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei einem Strike, der von einem Spare folgt.
- **Ausgangslage:** Liste von Wurfwerten [10, 5, 5, 3, 4, 2, 7, 1, 8, 0, 6, 2, 9, 0, 7, 3, 10, 3, 6]
- **Erwartetes Ergebnis:** Die berechneten Punkte sollten 104 sein.

### Testfall 3: Alle Strikes (TC003)
- **Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei aufeinander folgenden Strikes.
- **Ausgangslage:** Liste von Wurfwerten [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
- **Erwartetes Ergebnis:** Die berechneten Punkte sollten 300 sein.

### Testfall 4: Alle Spares (TC004)
- **Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei aufeinander folgenden Spares.
- **Ausgangslage:** Liste von Wurfwerten [5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 5, 5, 8, 2, 4, 6, 7, 3, 9, 1, 10]
- **Erwartetes Ergebnis:** Die berechneten Punkte sollten 173 sein.

### Testfall 5: Ungültiger Wurfwert (TC005)
- **Beschreibung:** Überprüft die Behandlung eines ungültigen Wurfwerts.
- **Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 11, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
- **Erwartetes Ergebnis:** Die Funktion sollte eine ValueError-Ausnahme auslösen.

### Testfall 6: Gültiger maximaler Wurf (TC006)
- **Beschreibung:** Überprüft die korrekte Berechnung von Punkten mit einem gültigen maximalen Wurfwert.
- **Ausgangslage:** Liste von Wurfwerten [1, 2, 10, 9, 10, 10, 20, 0, 19, 1]
- **Erwartetes Ergebnis:** Die berechneten Punkte sollten 121 sein.

### Testfall 7: Ungültiger maximaler Wurf (TC007)
- **Beschreibung:** Überprüft die Behandlung eines ungültigen maximalen Wurfwerts.
- **Ausgangslage:** Liste von Wurfwerten [1, 2, 5, 9, 1, 2, 5, 0, 2, 1]
- **Erwartetes Ergebnis:** Die Funktion sollte eine ValueError-Ausnahme auslösen.

## Testdurchführung
Die Testfälle werden durch automatisierte Unittests in Python unter Verwendung des unittest-Frameworks durchgeführt.

## Testabschluss
Die Testergebnisse werden überprüft, und das Testkonzept wird als erfolgreich abgeschlossen betrachtet, wenn alle Testfälle erfolgreich bestanden wurden.
