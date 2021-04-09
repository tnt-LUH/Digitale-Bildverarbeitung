# Übung 1: Grundlagen Python

Das Erlernen der Programmiersprache Python gehört nicht zum Anspruch dieses Kurses. Trotzdem sollen einige grundlegende
Funktionen und Konventionen aus Python erläutert werden. Im Folgenden wird das simple Beispielprogramm erläutert:

````python
# Beispielprogramm
import numpy as np

print(np.pi)

variable1 = 10
variable2 = [variable1, variable1 + 10, variable1 + 20]

print(variable2[0])
print(variable2[1])
print(variable2[2])

for var in variable2:
    if (var / 10)  % 2 == 1:
        print("Die erste Ziffer Zahl %s ist ungerade!" % var)

````
## Imports
Es existieren viele vorgefertigte Pakete in Python. Sie können diese importieren, indem Sie ``import PAKET `` verwenden.
Im Beispielcode wird *numpy* importiert und mit dem Namen *np* versehen. Daraufhin können Sie auf Funktionen des Pakets
zugreifen, wie z.B. in Zeile 4 ``print(np.pi)``, in welcher der Werit von Pi ausgegben wird. Nutzen Sie Imports nach 
Möglichkeit immer zu Beginn ihres Skripts.

## Variablen
In Python können Sie Variablen definieren, ohne einen Typ anzugeben. Im folgenden werden einige Typen gezeigt:

````python
a = "Ein Text"  # string
b = 2           # int
c = 3.4         # float
d = [2, 3, 4]   # list
e = (2, 3, 4)   # tuple
````
Besondere Variablentypen sind Listen oder Tupel. Sie sind Container für mehrere andere Variablen. Auf die einzelnen
Elemente der Liste/Tupel kann mit einem Index zugegriffen werden:

````python
a = [2, 3, 4]   # list
b = a[0]        # Entspricht dem Wert 2
````

Die Indizierung beginnt bei dem Wert 0. 

## print()
Sie können Werte oder Texte ausgeben, indem Sie den Befehl ``print(IRGENDEINE_VARIABLE)`` verwenden. 
Sie müssen die Variablen vorher nicht zum Datentyp *string* konvertieren.

## Schleifen

Bitte recherchieren Sie zum Thema Schleifen unter [https://www.python-kurs.eu/schleifen.php](https://www.python-kurs.eu/schleifen.php).