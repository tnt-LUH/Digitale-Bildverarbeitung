# Lösung Aufgabe c)

## Wie kann man sich die verschiedenen anen Transformationsmatrizen herleiten?
Für den Fall das die Abbildung linear ist, muss die Abbildung lediglich auf den Basisbildern
bestimmt werden. Zum Beispiel für die Basis `(1, 0)` und `(0, 1)` berechnet man die transformierten
Vektoren v1 und v2. Dann ist die Transformationsmatrix gegeben durch `T(p) = (v1, v2) p`. Bei
affinen Abbildungen kommt ensprechend noch eine Translation dazu. Wichtig für die Herleitung
der Transformationen sind daher Basiswechsel aus der linearen Algebra.

## Diskutieren Sie Vor- und Nachteile von Forward und Backwardmapping

Vorteile Backwardmapping:
- Geschwindigkeitsvorteil wenn lediglich ein bestimmter Bereich von Interesse ist. Dieser kann
direkt berechnet werden.
- Keine Löcher, keine Überlappungen im Ergebnisbild.

Vorteile Forwardmapping:
- Eventueller Vorteil da die Inverse der Transformation nicht bestimmt werden muss.

Nachteile:
- Es kann zu ÜUberlappung kommen. Mehrere Eingangspixel landen teilweise im gleichen Ergebnispixel.
(Hier muss aus diesen Werten ein finaler Wert interpoliert werden) Interpolation
erst nach kompletter Transformation möglich. Beim Backward-Mapping wird für jede Position
direkt eine Interpolation berechnet.