# Testkonzept für Bowling-Score-Berechnung

## Testfall 1
**ID:** TC001  
**Titel:** Normale Punkteberechnung  
**Beschreibung:** Überprüft die korrekte Berechnung der Punkte für normale Würfe.  
**Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 1, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.  
**Ergebnis:** Die berechneten Punkte sollten der Summe der Wurfwerte entsprechen.  
**Bestanden:** Ja/Nein  

## Testfall 2
**ID:** TC002  
**Titel:** Strike gefolgt von Spare  
**Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei einem Strike, der von einem Spare folgt.  
**Ausgangslage:** Liste von Wurfwerten [10, 5, 5, 3, 4, 2, 7, 1, 8, 0, 6, 2, 9, 0, 7, 3, 10, 3, 6]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.  
**Ergebnis:** Die berechneten Punkte sollten 104 sein.  
**Bestanden:** Ja/Nein  

## Testfall 3
**ID:** TC003  
**Titel:** Alle Strikes  
**Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei aufeinander folgenden Strikes.  
**Ausgangslage:** Liste von Wurfwerten [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.  
**Ergebnis:** Die berechneten Punkte sollten 300 sein.  
**Bestanden:** Ja/Nein  

## Testfall 4
**ID:** TC004  
**Titel:** Alle Spares  
**Beschreibung:** Überprüft die korrekte Berechnung von Punkten bei aufeinander folgenden Spares.  
**Ausgangslage:** Liste von Wurfwerten [5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 5, 5, 8, 2, 4, 6, 7, 3, 9, 1, 10]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.  
**Ergebnis:** Die berechneten Punkte sollten 173 sein.  
**Bestanden:** Ja/Nein  

## Testfall 5
**ID:** TC005  
**Titel:** Ungültiger Wurfwert  
**Beschreibung:** Überprüft die Behandlung eines ungültigen Wurfwerts.  
**Ausgangslage:** Liste von Wurfwerten [3, 5, 2, 4, 11, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten.  
**Ergebnis:** Die Funktion sollte eine ValueError-Ausnahme auslösen.  
**Bestanden:** Ja/Nein  

## Testfall 6
**ID:** TC006  
**Titel:** Gültiger maximaler Wurf  
**Beschreibung:** Überprüft die korrekte Berechnung von Punkten mit einem gültigen maximalen Wurfwert.  
**Ausgangslage:** Liste von Wurfwerten [1, 2, 10, 9, 10, 10, 20, 0, 19, 1]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten und maximalen Pins.  
**Ergebnis:** Die berechneten Punkte sollten 121 sein.  
**Bestanden:** Ja/Nein  

## Testfall 7
**ID:** TC007  
**Titel:** Ungültiger maximaler Wurf  
**Beschreibung:** Überprüft die Behandlung eines ungültigen maximalen Wurfwerts.  
**Ausgangslage:** Liste von Wurfwerten [1, 2, 5, 9, 1, 2, 5, 0, 2, 1]  
**Schritte:** Aufruf der Bowling-Score-Funktion mit den Wurfwerten und ungültigem maximalen Pins.  
**Ergebnis:** Die Funktion sollte eine ValueError-Ausnahme auslösen.  
**Bestanden:** Ja/Nein  
