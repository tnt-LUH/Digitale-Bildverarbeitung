# Übung 3:  Geometrische Transformationen

Geometrische Transformationen können auf Bilder angewendet werden, um den Wert eines Pixels im Eingangsbild auf eine
andere Position im Ausgangsbild abzubilden.

Geometrische Transformationen können unterschieden werden in 

|Name| Freiheitsgrade| Beispiel| 
|:---:|:---:|:---:|
|Translation|2||
|Rigide/Euklidische Transformation|3||
|Ähnlichkeits- Transformation|4||
|Affine Transformation|6||
|Projektive Transformation|8||

Zusätzliche Informationen über die Implementierung in OpenCV können Sie hier finden: [https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html](https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html)

## Aufgabe a)
Eine häufig verwendete Transformation ist die Skalierung, Diese sollen Sie nun implementieren. Arbeiten Sie dazu die 
Fragen bzw. Teilschritte in *a.py* ab. Die entsprechende Lösung finden Sie in *l_a.py*.

## Aufgabe b)

Betrachten Sie das folgende Eingangsbild sowie die daraus resultierenden Ausgangsbilder.

**Eingangsbild:**
 
![](./data/normal.jpg)

**Ausgangsbilder:**

![](./data/center-rotated.jpg) 
![](./data/rotated.jpg) 
![](./data/shear.jpg) 

Gebeben sind folgende Transformationsforschriften:

```python
 I_in = [
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
    [100, 100, 100, 100, 100],
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
 ]
```

Wenden Sie die Transformationen in der Datei *b.py* auf das Eingangsbild an und finden Sie so heraus, welche
Transformation zu welchem Ausgangsbild gehört. Die Lösung findet sich in der Datei *l_b.py*.  

## Aufgabe c)
Weitere Fragen:
 - Wie kann man sich die verschiedenen affinen Transformationsmatrizen aus a) herleiten ?
 - Diskutieren Sie Vor- und Nachteile von Forward und Backwardmapping!
