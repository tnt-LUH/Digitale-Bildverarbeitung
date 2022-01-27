# Lösung b): Klassifikation von Merkmalen

Basierend auf den Merkmalen in Teilaufgabe a) können einige Regelen für die Klassifikation von Objekten erstellt werden. 
Diese Lösung ist eine von vielen möglichen Lösungen und bezieht sich auf die Ausgabe aus Aufgabe a):

````shell
Image: img1
    h = 119
    w = 60
    height_over_width = 1.9833333333333334
    perimeter = 535.0
    area = 2925.0
    roundness = 4.092521367521368
Image: img2
    h = 96
    w = 53
    height_over_width = 1.8113207547169812
    perimeter = 494.0
    area = 1981.0
    roundness = 4.6444977284199895
Image: img3
    h = 98
    w = 117
    height_over_width = 0.8376068376068376
    perimeter = 1120.0
    area = 2489.0
    roundness = 12.093210124548012
Image: img4
    h = 73
    w = 56
    height_over_width = 1.3035714285714286
    perimeter = 631.0
    area = 884.0
    roundness = 11.510039592760181
Image: img5
    h = 48
    w = 50
    height_over_width = 0.96
    perimeter = 140.0
    area = 1960.0
    roundness = 0.875
Image: img6
    h = 49
    w = 56
    height_over_width = 0.875
    perimeter = 382.0
    area = 2111.0
    roundness = 2.3750592136428232

Process finished with exit code 0

````

- **Menschen** sind im stehenden Zustand ca. doppelt so hoch wie breit. Daher sollte bei einem Menschen *height_over_width* ca. 2 sein. Zusätzlich sollte die *roundness* deutlich ungleich 1 sein.
- **Bälle** sind unabhängig von ihrer Größe rund. Die *roundness* sollte daher in der Nähe von 1 liegen.
- **Fenster** haben meistens aufgrund der "Kacheln" eine geringe Fläche, verglichen zu dem Umfang.


Diese Regeln müssen nicht auf jedes Objekt zutreffen. Sie sollen lediglich veranschaulichen, wie Regeln für einen Klassifikator
aus Merkmalen erstellt werden können. 