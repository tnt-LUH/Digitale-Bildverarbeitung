# Übung 6: Hough-Akkumulator

Betrachten Sie das folgende Binärbild:

![](data/houghImg.png)


Dabei sind die schwarzen Pixel als Kantenpixel zu verstehen. 
Im folgenden sollen Sie mittels der Hough-Transformation Linien im Binärbild finden. 
Bearbeiten Sie dazu folgende Aufgaben:

## a) Akkumulator

Nutzen Sie für die Hough-Transformation den folgenden Hough-Akkumulator mit der 
Parametrisierung **y=mx+n**. 

![](data/houghAcc.png)


Erstellen Sie die finale Akkumulator-Matrix H.

Die Lösung befindet sich in Datei [l_a.py](l_a.py).

## b) Parametrierung

Geben Sie die Parametrierung der Geraden an, 
fuer welche die Akkumulator-Matrix H den größten Wert hat.

Die Lösung befindet sich in Datei [l_b.py](l_b.py).
