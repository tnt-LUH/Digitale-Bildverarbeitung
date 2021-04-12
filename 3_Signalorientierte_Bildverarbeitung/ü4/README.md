# Übung 4: Notch-Filter im Frequenzraum

In dem Skript [a.py](a.py) wird das Bild von Lena eingeladen.
Gleichzeitig wird ein gestörtes Bild von Lena eingeladen. 
Dem Bild wurde ein Raster überlagert. 

Original | Gestört 
---|---
![](../../data/lena.png) | ![](../../data/lena_raster.png) 

## Aufgabe a)
Das Raster soll unter Benutzung des Frequenzbereiches auf einfache Weise für
den subjektiven Eindruck entfernt werden.

Gehen Sie dabei wie folgt vor:
1. Transformieren Sie die Bilder in den Frequenzbereich und betrachten Sie charakteristische
Unterschiede.
2. Maskieren Sie die gestörten Bereiche aus, in dem Sie geeigente Bereiche der Matrix auf Null
setzen. Die Zentren der Störungen liegen etwa bei (nach fftshift):

   - [85, 85]
   - [255, 85]
   - [425, 85]
   - [85, 255] 
   - [255, 425] 
   - [425, 255]
   - [85, 425] 
   - [425, 425]
3. Transformieren Sie das Bild in den Ortsbereich zurück.

Sie finden die Musterlösung in der Datei [l_a.py](l_a.py).