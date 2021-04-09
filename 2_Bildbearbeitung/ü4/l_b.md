# Lösung zu Aufgabe b)
Zuerst soll der Rechenaufwand für einen Pixel betrachtet werden:

**Filterkern mit 3x3-Matrix für einen Pixel:**
- 9 x Multiplikation
- 8 x Addition 
- Insgesamt 17 x Rechenoperationen


**Filterkern mit separierten 3x1- bzw. 1x3-Vektoren für einen Pixel:**
- 12 x Multiplikation
- 8 x Addition Insgesamt
- 20 x Rechenoperationen

Berechnet man lediglich den Pixelwert in der Mitte, so ergibt sich kein Geschwindigkeitsvorteil.
Für das gesamte Bild ergibt sich jedoch ein Geschwindigkeitsvorteil pro Pixel, da die Zwischenergebnisse
aus der Filterung mit dem ersten Filterkern nicht neu berechnet werden müssen. Anstatt
9 Multiplikationen und 8 Additionen mit dem 3x3-Filterkern ergeben sich mit den separierten
Filterkomponenten durchschnittlich 6 Multiplikationen und 4 Additionen pro Pixel.

Gemittelte Anzahl Rechenoperationen pro Pixel für das gesamte Bild:

**Filterkern mit 3x3-Matrix für einen Pixel:**
- 9 x Multiplikation
- 8 x Addition 
- Insgesamt 17 x Rechenoperationen


**Filterkern mit separierten 3x1- bzw. 1x3-Vektoren für einen Pixel:**
- 6 x Multiplikation
- 4 x Addition Insgesamt
- 10 x Rechenoperationen
