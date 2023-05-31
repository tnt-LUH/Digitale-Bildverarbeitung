# Übung 5: Homomorphe Filterung

In dem Skript [a.py](a.py) wird das Bild *I*

![](../../data/car2.png) 

geladen. Das Bild zeigt eine schlecht belichtete Szene, in der Details nicht
gut zu erkennen sind. In dieser Übung soll der Kontrast verbessert werden, damit
mehr Details erkennbar sind.

## Aufgabe a)


Wenden Sie die Homomorphe Filterung auf das Bild *I* an, indem Sie folgende Schritte implementieren:

1. Logarithmieren Sie die Werte in Grauwerte in *I*
2. Transformieren Sie *I* in den Frequenzbereich
3. Unterdrücken Sie niedrige Frequenzen durch die Funktion H(k,l)<p align="center"><img src="https://latex.codecogs.com/svg.image?H(k,l)=\begin{cases}&space;1,&&space;k=0&space;\&space;\cap&space;\&space;l=0&space;\\&space;\gamma_1&space;-&space;(\gamma_1&space;-&space;\gamma_2)e^{(-\frac{k^2&plus;l^2}{\gamma_3})}&space;&&space;\text{sonst}\end{cases}&space;" title="" /></p>
5. Transformieren Sie *I* zurück in den Bildbereich
6. Kehren Sie die Logarithmierung aus Schritt 1. durch die Exponentialfunktion um

Der erste Teil der Aufgabe ist in der Datei [a.py](a.py) zu finden.

Sie finden die Musterlösung in der Datei [l_a.py](l_a.py).

**Hinweis:** Arbeiten Sie mit einem Wertebereich zwischen 0 und 1!
