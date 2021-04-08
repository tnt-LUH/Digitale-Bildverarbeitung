# Übung 3:  Diskretisierung und Quantisierung

In dieser Übung wird die Quantisierung und Diskretisierung von Bildern betrachtet. In dn folgenden Abbildungen sind beide
Methoden visualisiert.

Quantisierung | Diskretisierung
:---:|:---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Quantized.signal.svg/2880px-Quantized.signal.svg.png) | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Zeroorderhold.signal.svg/2880px-Zeroorderhold.signal.svg.png)
[Link zum Bild](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Quantized.signal.svg/2880px-Quantized.signal.svg.png) | [Link zum Bild](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Zeroorderhold.signal.svg/2880px-Zeroorderhold.signal.svg.png)


## Aufgabe a) Diskretisierng
In der Datei *a.py* wird ein Bild geladen. Das Bild hat die Größe 1526 x 1600 (Breite x Höhe).

Diskretisieren Sie das Bild mit dem Faktor *k* **ohne** und **mit** Verwendung der Funktion `cv2.resize()`. Dabei kann 
*k* die Werte 4, 8, und 13.5 annehmen. Zeigen Sie die Bilder für den direkten Vergleich an! Achten Sie dabei darauf,
dass die Bilder in der gleichen Größe dargestellt werden.


## Aufgabe b) Quantisierung
In der Datei *b.py* wird ein Bild geladen. Das Bild ist im BGR-Farbraum repräsentiert und hat eine 8-Bit Quantisierung 
(Wertebereich {0, ..., 255}. 

Führen Sie folgende Schritte durch:
 1. Quantisieren Sie das Bild in den Wertebereich {0, ..., 127}
 2. Quantisieren Sie das Bild aus Schritt 1 in den Wertebereich {0, ..., 3}
 3. Quantisieren Sie das Bild aus Schritt 2 zurück in den Wertebereich {0, ..., 255}

Zeigen Sie die Bilder aus allen Schritten für den direkten Vergleich an:
 
 - Wie bewerten Sie die Qualität der Bilder?
 - Was fällt auf?




