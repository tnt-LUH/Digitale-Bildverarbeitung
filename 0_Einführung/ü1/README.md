# Übung 1: Grundlagen Python

Das Erlernen der Programmiersprache Python gehört nicht zum Anspruch dieses Kurses. Trotzdem sollen einige grundlegende
Funktionen und Konventionen aus Python erläutert werden. Im folgenden wir das simple Beispielprogramm erläutert

````python
# Beispielprogramm
import numpy as np

print(np.pi)

variable1 = 10
variable2 = [variable1, variable1 + 10, variable1 + 20]

for var in variable2:
    if (var / 10)  % 2 == 1:
        print("Die erste Ziffer Zahl %s ist ungerade!" % var)

````
## Imports
Es existieren viele vorgefertigte Pakete in Python. Sie können diese importieren, indem Sie ``import PAKET `` verwenden.
Im Beispielcode wird *numpy* importiert und mit dem Namen *np* versehen. Daraufhin können Sie auf Funktionen des Pakets
zugreifen, wie z.B. in Zeile 4 ``print(np.pi)``, in welcher der Werit von Pi ausgegben wird. Nutzen Sie Imports nach 
Möglichkeit immer zu Beginn ihres Skripts.

## print()
Sie können Werte oder Texte ausgeben, indem Sie den Befehl ``print(IRGENDEIN_WERT)`` verwenden.

