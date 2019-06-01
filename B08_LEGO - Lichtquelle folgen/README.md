# Basisaktivität 08 (B18): Mindstorms bewegt sich auf Lichtquelle zu

## Problemstellung
Der Mindstorms soll sich mithilfe des Farbsensors auf eine Lichtquelle zubewegen.

Die Lichtquelle muss zuvor nicht lokalisiert werden, sie befindet sich bereits im Sensorbereich des Roboters.

## Lösungsansatz
Der Roboter fährt mit eine leichten Rechtskurve nach vorne und misst konstant die aktuelle Lichtstärke. Sobald die Lichtstärke nicht mehr zu, sondern wieder abnimmt, ändert er seinen Pfad auf eine leichte Linkskurve. Dieses Verhalten wird so lange wiederholt, bis er die Lichtquelle erreicht hat.
