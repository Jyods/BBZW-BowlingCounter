# Testprotokoll für Bowling-Score-Berechnung

## Testdurchführung 08.12.2023, 19:56

### Testfall 1: Normale Punkteberechnung (TC001)
- **Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 1, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.
- **Ergebnis:** Die berechneten Punkte entsprechen der Summe der Wurfwerte.
- **Bestanden:** Ja

### Testfall 2: Strike gefolgt von Spare (TC002)
- **Ausgangslage:** Liste von Wurfwerten [10, 5, 5, 3, 4, 2, 7, 1, 8, 0, 6, 2, 9, 0, 7, 3, 10, 3, 6]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.
- **Ergebnis:** Die berechneten Punkte sollten 104 sein.
- **Bestanden:** Ja

### Testfall 3: Alle Strikes (TC003)
- **Ausgangslage:** Liste von Wurfwerten [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.
- **Ergebnis:** Die berechneten Punkte sollten 300 sein.
- **Bestanden:** Ja

### Testfall 4: Alle Spares (TC004)
- **Ausgangslage:** Liste von Wurfwerten [5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 5, 5, 8, 2, 4, 6, 7, 3, 9, 1, 10]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.
- **Ergebnis:** Die berechneten Punkte sollten 173 sein.
- **Bestanden:** Ja

### Testfall 5: Ungültiger Wurfwert (TC005)
- **Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 11, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.
- **Ergebnis:** Die Funktion löst eine ValueError-Ausnahme aus.
- **Bestanden:** Ja

### Testfall 6: Gültiger maximaler Wurf (TC006)
- **Ausgangslage:** Liste von Wurfwerten [1, 2, 10, 9, 10, 10, 20, 0, 19, 1]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten und maximalem Pins.
- **Ergebnis:** Die berechneten Punkte sollten 121 sein.
- **Bestanden:** Ja

### Testfall 7: Ungültiger maximaler Wurf (TC007)
- **Ausgangslage:** Liste von Wurfwerten [1, 2, 5, 9, 1, 2, 5, 0, 2, 1]
- **Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten und ungültigem maximalem Pins.
- **Ergebnis:** Die Funktion löst eine ValueError-Ausnahme aus.
- **Bestanden:** Ja

## Zusammenfassung
Alle Testfälle wurden erfolgreich durchgeführt und bestanden.
