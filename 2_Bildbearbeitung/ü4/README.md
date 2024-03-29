# Übung 4: Filterkern

Ein Filterkern ist eine n-dimensionale Matrix, mit der üblicherweise eine lokale und lineare Operation auf Pixel im 
Eingangsbild angewendet wird. In dieser Übung sollen Aufgaben mit Filterkernen manuell und mit Python gelößt werden.

## Aufgabe a) Separierung
Unter Umständen ist ein 2-dimensionaler Filterkern separierbar, d.h. er durch zwei 1-dimensonale Filterkerne dargestellt
werden.  

Nehmen Sie die bereits separierten Filterkerne
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;F_a&space;=&space;\begin{bmatrix}1&space;&&space;4&space;&&space;1&space;\\\end{bmatrix}&space;\quad&space;\text{und}\quad&space;F_b&space;=&space;\begin{bmatrix}&space;-1\\&space;0\\1\end{bmatrix}&space;" title="\bg_white F_a = \begin{bmatrix}1 & 4 & 1 \\\end{bmatrix} \quad \text{und} F_b = \begin{bmatrix} -1\\ 0\\1\end{bmatrix} " />
</p>
und erstellen den ursprünglichen Filterken, sowohl "von Hand" als auch in einem Python Skript.


Betrachten und separieren Sie zusätzlich den Filterkern 
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;\inline&space;F_C&space;=&space;\begin{bmatrix}-2&space;&&space;-3&space;&&space;-2&space;\\0&space;&&space;0&space;&&space;0&space;\\2&space;&&space;3&space;&&space;2&space;\\\end{bmatrix}&space;&space;" title="\bg_white \inline F_C = \begin{bmatrix}-2 & -3 & -2 \\0 & 0 & 0 \\2 & 3 & 2 \\\end{bmatrix} " />
</p>

wenn möglich (manuell und in Python)! Die Lösung findet sich in der Datei [l_a.py](l_a.py).

## Aufgabe b)
Stellen Sie sich vor, Sie wenden die separierten oder nicht separierten Filterkerne auf ein durchschnittliches Bild an.
Wie viele Rechenoperationen pro Pixel führen Sie im Durchschnitt pro Pixel aus, wenn sie

 - einen separierten 3x3 Filterkern
 - einen nicht separierten 3x3 Filterkern 
 
 verwenden. Die Musterlösung befindet sich in der Datei [l_b.md](l_b.md).
 
## Aufgabe c) 
Laden Sie ein beliebiges Bild ein und verwenden Sie die OpenCV-Methode *cv2.filter2D()* um Schärfefilter, Mittelwert-Filter und
Kantenfilter auf das Bild anzuwenden. Die Musterlösung befindet sich in der Datei [l_c.py](l_c.py).

## Aufgabe d) 
Modifizieren Sie die Aufgabe c), indem Sie nur den Mittelwert-Filter verwenden und diesen vergrößern. Verwenden Sie 
verschiedene Boundary Optionen durch das Argument *borderType* in der Funktion *cv2.filter2D()* und betrachten Sie das
Ergebnis. Vergleichen Sie die verschiedenen Optionen *cv2.BORDER_REFLECT*, *cv2.BORDER_REPLICATE* und *cv2.BORDER_CONSTANT*.
Visualisieren Sie weiterhin die Optionen, indem Sie einen Rand mit der Funktion *cv2.copyMakeBorder()* zu dem Bild
hinzufügen. Die Musterlösung befindet sich in der Datei [l_d.py](l_d.py).
