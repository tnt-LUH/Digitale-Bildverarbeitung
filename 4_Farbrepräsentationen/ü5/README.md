# Übung 4: Kettencode

Eine Variante für die Abbildung von Konturen is der Kettencode. Im folgenden sollten Bilder in den Kettencode codiert und
Kettencodes in Konturen decodiert werden.

Für die Codierung mit dem Kettencode soll folgende Zuordnung verwendet werden:
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;3&space;&&space;2&space;&&space;1&space;\\&space;4&space;&&space;&&space;0\\&space;5&space;&&space;6&space;&&space;7&space;\end{bmatrix}" />
</p>


Für die Codierung mit dem differentiellen Kettencode soll folgende Zuordnung verwendet werden:
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;&plus;3&space;&&space;&plus;2&space;&&space;&plus;1&space;\\&space;4&space;&&space;&&space;0\\&space;-3&space;&&space;-2&space;&&space;-1&space;\end{bmatrix}" />
</p>



## Aufgabe a) Kettencode

Erstellen Sie für das Bild 

![](./data/1.png)

einen Kettencode! Beginnen Sie mit dem Pixel oben links und dem Wert 0. 

## Aufgabe b) Kettencode

Erstellen Sie das Bild für den Kettencode

```[6 4 6 3 4 5 6 4 2 2 3 2 2 0 0 7 0 2 0 0 7 6]```


## Aufgabe c) Differentieller Kettencode

Erstellen Sie für das Bild aus Aufgabe a)
einen differenziellen Kettencode! Beginnen Sie mit dem Pixel oben links und dem Wert 0. 

## Aufgabe d) Differentieller Kettencode

Erstellen Sie das Bild für den differentiellen Kettencode

```[-2 -2 2 -3 1 1 1 -2 -2 0 1 -1 0 -2 0 -1 1 2 -2 0 -1 -1]```
