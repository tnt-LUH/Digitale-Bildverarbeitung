# Übung 2: BGR zu HSV

In dieser Übung wird der HSV Farbraum betrachtet. Die Information der Farbe wird
durch die drei Werte  

 - H: Helligkeit (Hue)
 - S: Sättigung (Saturation)
 - V: Value (Helligkeit)
 
repräsentiert.

In der folgenden Abbildung wird der Farbraum visuell dargestellt:

![alt text](https://upload.wikimedia.org/wikipedia/commons/f/f1/HSV_cone.jpg)


## Aufgabe a)
Lesen Sie Ihre Kamera aus und geben Sie das Bild "live" wieder.
Konvertieren Sie den eingelesenen Videostream aus Aufgabe in den HSV Farbraum. 
Reduzieren Sie die Helligkeit, indem Sie einen der drei Farbkanäle um 30% reduzieren. 
Konvertieren Sie das Bild daraufhin zurück in den RGB Farbraum. 

Die Lösung findet sich in der Datei [l_a.py](l_a.py).

## Aufgabe b)
Modifizieren Sie Aufgabe a) so, dass die Helligkeit zyklisch zwischen 0% und 100%
variiert.  
Die Lösung findet sich in der Datei [l_a.py](l_b.py).




