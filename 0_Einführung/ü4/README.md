# Übung 4: Grundlagen

Machen Sie sich mit den Grundlagen aus den vorherigen Übungen 1 vertraut. Diese Grundlagen werden nun praktisch angewandt
Nutzen Sie für diese Übung keine Funktionen aus *OpenCV*!

## Aufgabe a) 
Führen Sie folgende Aufgabenschritte durch:

1. Erstellen Sie eine 10x10-Matrix mit den Werten von 0 bis 99 wie folgt:
<p align="center">
<img src="https://latex.codecogs.com/svg.image?M&space;=&space;\begin{bmatrix}&space;0&&space;&space;1&&space;\ldots&space;&&space;&space;8&&space;9&space;\\&space;10&&space;&space;11&&space;&space;&&space;&space;18&&space;&space;19\\&space;\vdots&space;&&space;\vdots&space;&space;&&space;\ddots&space;&space;&&space;\vdots&space;&space;&&space;\vdots&space;&space;\\&space;80&&space;&space;81&&space;\ldots&space;&&space;88&space;&&space;89&space;\\&space;90&&space;91&space;&&space;\ldots&space;&&space;98&space;&&space;99&space;\\\end{bmatrix}&space;" title="M = \begin{bmatrix} 0& 1& \ldots & 8& 9 \\ 10& 11& & 18& 19\\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 80& 81& \ldots & 88 & 89 \\ 90& 91 & \ldots & 98 & 99 \\\end{bmatrix} " />
</p>

2. Erzeugen Sie einen Zeilenvektor der Dimension 10. Alle Komponenten sollen den Wert 20 haben:

<p align="center">
<img src="https://latex.codecogs.com/svg.image?v&space;=&space;\begin{bmatrix}&space;20&&space;&space;20&&space;20&&space;20&&space;20&&space;20&&space;20&&space;20&&space;20&&space;20&space;\\\end{bmatrix}" title="v = \begin{bmatrix} 20& 20& 20& 20& 20& 20& 20& 20& 20& 20 \\\end{bmatrix}" />
</p>

3. Subtrahieren Sie die zweite Zeile der Matrix M vom eben erzeugten Vektor v.
4. Multiplizieren Sie den resultierenden Vektor vr als Spaltenvektor von rechts mit der Matrix M
5. Teilen Sie die Komponenten des entstandenen Vektors jeweils durch 100 und runden Sie das Ergebnis. 
6. Berechnen Sie das Maximum

Wie lautet das Ergebnis?

Die Musterlösung findet sich in [l_a.py](l_a.py)