# Übung 6: Unitäre Transformation

In dem Skript [a.py](a.py) wird das Bild von Lena eingeladen.

![](../../data/lena.png) 

## Aufgabe a) Haar-Transformation
Das Bild soll in die hohen tiefen Frequenzen mithilfe der Haar-Transformation zerlegt werden.
Erstellen Sie dafür eine Haar-Koeffizientnmatrix der Größe 512x512 mit der Berechnungsvorschrift 

<img src="https://latex.codecogs.com/svg.image?H^{(N)}_{ij}:=\begin{cases}\frac{1}{\sqrt{2}},&space;&&space;\text{if}\&space;i\leq&space;\frac{N}{2},&space;j\in&space;\{2i-1,&space;\}&space;&space;\\\frac{1}{\sqrt{2}},&space;&&space;\text{if}\&space;i>\frac{N}{2},&space;j=2(i-\frac{N}{2})-1&space;\\-\frac{1}{\sqrt{2}},&space;&&space;\text{if}\&space;i>\frac{N}{2},&space;j=2(i-\frac{N}{2})\end{cases}" title="" />

und wenden Sie diese auf das Bild mithilfe von

<img src="https://latex.codecogs.com/svg.image?I'=HI">

an. Zeigen Sie das Bild, und geben Sie einige interessante Koeffizienten aus H an. Prüfen Sie Ihre Berechnungen, 
indem Sie die Rücktransformation mithilfe von

<img src="https://latex.codecogs.com/svg.image?I=H^T(HI)">

anwenden und prüfen, ob Änderungen im Bild vorhanden sind.

Sie finden die Musterlösung in der Datei [l_a.py](l_a.py).