# Übung 12: Automatische Schwellwertfindung nach Otsu

Sie haben folgendes Bild gegeben und sollen den Kamera-Mann und seine Kamera möglichst gut mit einem binären Schwellwert
segmentieren:
![](../../data/cameraman.png)

Hierzu soll das Verfahren von Otsu verwendet werden.

## a) Otsu

Berechnen Sie für jeden Schwellwert zwischen {0, ..., 255} die Mittelwerte und Varianzen der beiden Gaussverteilungen 

<p align="center">
<img src="https://latex.codecogs.com/svg.image?n_1(s)=\sum_{k=0}^sh(k)" title="\sum_1" />
<p>

<p align="center">
<img src="https://latex.codecogs.com/svg.image?n_2(s)=\sum_{k=s+1}^{255}h(k)" title="\sum_1" />
<p>

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\mu_1(s)=\frac{1}{n_1}\sum_{k=0}^sh(k)k" title="\sum_1" />
<p>

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\mu_2(s)=\frac{1}{n_2}\sum_{k=s+1}^{255}h(k)k" title="\sum_1" />
<p>

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\sigma_1(s)=\sqrt{\frac{1}{n_1}\sum_{k=0}^sh(k)(k-\mu_1)^2}" title="\sum_1" />
<p>

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\sigma_2(s)=\sqrt{\frac{1}{n_2}\sum_{k=s+1}^{255}h(k)(k-\mu_2)^2}" title="\sum_1" />
<p>

und maximieren Sie den Quotienten

<p align="center">
<img src="https://latex.codecogs.com/svg.image?Q(s)=\frac{\sigma(s)_{zw}^2}{\sigma(s)_{in}^2}=\frac{n_1(s)(\mu_1(s)-\mu)^2+n_2(s)(\mu_2(s)-\mu)^2}{n_1(s)\sigma_1(s)^2+n_2(s)\sigma_2(s)^2}" title="\sum_1" />
<p>

mit dem Mittelwert des Grauwertbildes 
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\mu=\frac{1}{n_1(255)}\sum_{k=0}^{255}h(k)k," title="\sum_1" />
<p>

sodass Sie den optimalen Schwellwert s bekommen.

Bitte führen Sie für die Bearbeitung der Aufgabe das Skript [a.py](a.py) fort. 
Die Lösung befindet sich in Datei [l_a.py](l_a.py).
