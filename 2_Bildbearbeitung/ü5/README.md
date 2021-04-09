# Übung 5: Nichtlineare Filter

In dieser Übung wird der nichtlineare Median-Filter behandelt. Der Median-Filter ist ein Sonderfall des Rangfolge-Filters.
Bei einem Rangfolge-Filter werden die Werte des zu untersuchenden Bildausschnitts aufsteigend sortiert.
Je nach Filter-Definition wird dann der n-te Wert der Folge als neuer Pixelwert definiert. Sonderfälle des Rangfolge-Filters sind:
- Maximum-Filter: Letzter Wert der Folge
- Minimum-Filter: Erster Wert der Folge
- Median-Filter: Wert der mittleren Position der Folge

## Aufgabe a)
Gegeben ist folgender Bildausschnitt:
<p align="center">
<img src="https://latex.codecogs.com/svg.image?I&space;=&space;\begin{bmatrix}1&space;&4&space;&space;&6&space;&space;\\&space;3&&space;2&space;&&space;1&space;\\&space;6&&space;&space;8&&space;&space;2\end{bmatrix}&space;" title="I = \begin{bmatrix}1 &4 &6 \\ 3& 2 & 1 \\ 6& 8& 2\end{bmatrix} " />
</p>

Geben Sie den Mittelwert und Median des Ausschnitts an!
Die Lösung finden Sie in der Datei [l_a.py](l_a.py).

## Aufgabe b)
Starten Sie das Program [b.py](b.py) um ein verrauschtes Bild zu erhalten und filtern Sie es 
mit der OpenCV-Filterfunktion *cv2.medianBlur(). Führen Sie die Filterung mit den Filtergrößen: 3x3, 5x5,
9x9. Vergleichen Sie die Ergebnisse durch Visualisierung des Ergebnisses mit *cv2.imshow()*.

Die Lösung finden Sie in der Datei [l_b.py](l_b.py).
