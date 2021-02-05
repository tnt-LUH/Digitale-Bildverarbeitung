# Übung 2:  Diskretisierung und Quantisierung

In dieser Übung wird Quantisierung und Diskretisierung von Bildern betrachtet. 


## Aufgabe a) Diskretisierung
In der Datei ``ü2a.py`` wird ein Bild geladen. Das Bild hat die Größe 1526 x 1600 (Breite x Höhe).

Diskretisieren Sie das Bild mit dem Faktor *k* **ohne** und **mit** Verwendung der Funktion `cv2.resize()`. Dabei kann 
*k* die Werte 4, 8, und 13.5 annehmen. Zeigen Sie die Bilder für den direkten Vergleich an! Achten Sie dabei darauf,
dass die Bilder in der gleichen Größe dargestellt werden.


## Aufgabe b)
In der Datei ``ü2b.py`` wird ein Bild geladen. Das Bild ist im BGR-Farbraum repräsentiert und hat eine 8-Bit Quantisierung 
(Wertebereich {0, ..., 255}. 

Führen Sie folgende Schritte durch:
 1. Quantisieren Sie das Bild in den Wertebereich {0, ..., 127}
 2. Quantisieren Sie das Bild aus Schritt 1 in den Wertebereich {0, ..., 3}
 3. Quantisieren Sie das Bild aus Schritt 2 zurück in den Wertebereich {0, ..., 255}

Zeigen Sie die Bilder aus allen Schritten für den direkten Vergleich an:
 
 - Wie bewerten Sie die Qualität der Bilder?
 - Was fällt auf?




