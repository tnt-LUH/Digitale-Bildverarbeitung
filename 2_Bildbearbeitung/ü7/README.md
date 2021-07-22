# Übung 7: Interpolation

In dieser Übung wird die *Nächste Nachbar (Nearest Neighbour) Interpolation* und die *Bilineare Interpolation* 
bei geometrischen Transformationen betrachtet.

Für diese Aufgabe haben Sie ein Bild bestehend aus vier Pixelwerten I_xy:

   - I_00 = 1
   - I_10 = 2
   - I_01 = 3
   - I_11 = 4 


## a) Interpolation beim Backward Mapping
Sie transformieren das Bild mithilfe der Transformationsvorschrift **T** beziehungsweise der dazugehörigen inversen 
Transformationsvorschrift mithilfe des Backward-Mappings. Die ursprüngliche Position I_xy auf dem Eingangsbild des Pixels I'_00 auf dem Ausgangsbild wird durch die die Inverse
Transformation gegeben. Berechnen Sie den Wert des Pixels I'_00 mithilfe der *Nächste Nachbar (Nearest Neighbour) Interpolation* und der *Bilineare Interpolation*, wenn die ursprüngliche Postition I_xy an den Koordinaten

 - (x=0.3 | y=0.8) 
 - (x=0 | y=1) 
 - (x=0.5 | y=0.5) 

liegt.

Sie können die Aufgabe handschriftlich oder mithilfe eines Skripts lösen. Die Lösung ist in der Datei [l_a.py](l_a.py) zu finden!


## b) Interpolation beim Forward Mapping
Sie transformieren das Bild mithilfe der Transformationsvorschrift **T** und des Forward-Mappings. Nach der Transformation ist die neue Position der gegeben
Pixel wie folgt:

 - I_00 = 1: (x=0.5 | y=0.5)   
 - I_10 = 2: (x=1.5 | y=0.5)
 - I_01 = 3: (x=0.5 | y=1.5)
 - I_11 = 4: (x=1.5 | y=1.5)
   
Interpolieren Sie die Werte auf dem Zielbild mithilfe der *Nächste Nachbar (Nearest Neighbour) Interpolation* und der *Bilineare Interpolation* für die folgenden Pixel:

 - I'_11
 - I'_00

Sie können die Aufgabe handschriftlich oder mithilfe eines Skripts lösen. Die Lösung ist in der Datei [l_b.py](l_b.py) zu finden!
