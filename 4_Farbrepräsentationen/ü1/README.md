# Übung 1:  BGR zu HSV

In dieser Übung wird der HSV Farbraum betrachtet. Die Information der Farbe wird
durch die drei Werte  

 - H: Helligkeit (Hue)
 - S: Sättigung (Saturation)
 - V: Value (Helligkeit)
 
repräsentiert.

In der folgenden Abbildung wird der Farbraum visuell dargestellt:

![alt text](https://upload.wikimedia.org/wikipedia/commons/f/f1/HSV_cone.jpg)


## Aufgabe a)
In der Datei ``ü1.py`` wird ein Bild geladen. Nach dem Laden befindet sich das Bild
im BGR-Farbraum. Konvertieren Sie das Bild manuell und 
ohne Hilfe von OpenCV in den HSV Farbraum.

Sie können die Rechenvorschriften der Konvertierung von RGB zu HSV aus der [OpenCV-Dokumentation](https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html) 
nutzen. Beachten Sie, dass die Farbkanäle in OpenCV in BGR und nicht in RGB abgespeichert sind!


## Aufgabe b)
Konvertieren Sie das Bild mithilfe der OpenCV Funktion ```cv2.cvtColor()``` in den HSV
Farbraum. Vergleichen Sie das Ergebnis dann mit dem Ergebnis aus Aufgabenteil a).

Sind die Ergebnisse gleich? Wenn nicht, woran kann es liegen?





