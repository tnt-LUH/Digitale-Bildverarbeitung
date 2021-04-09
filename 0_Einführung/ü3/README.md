# OpenCV in Python
Die beliebte Bildverarbeitungs-Software OpenCV existiert auch in Python. In dieser Übung sollen Sie einige Befehle
erlernen, um grundlegende Funktionen mit OpenCV zu schreiben. 

Um OpenCV zu nutzen, müssen Sie zuerst das Paker *cv2* installieren. Wenn Sie dieses Repository installiert haben,
ist das bereits geschehen. Es wird für die folgenden Schritte davon ausgegangen, das *cv2* bereits installiert ist.
Importieren Sie zu Beginn Ihres Skriptes das OpenCV Paket mit dem Befehl

````python
import cv2
````

Nun können Sie alle Funktionen von OpenCV mit dem vorangestellten Kürzel ``cv2.EIN_BEFEHL()`` nutzen.

## Bild laden
Bilder werden als MxN Matrizen (Grau- und Binärbilder) oder als MxNx3 Arrays (RGB-Farbbilder)
gespeichert und interpretiert. Um ein Bild einzulesen, wird die Funktion ``cv2.imread(PFAD_ZUM_BID)`` aufgerufen
und der Dateiname als Parameter in den Klammern übergeben.
````python
I = cv2.imread('myimage.bmp')  # Farbbild einlesen
````
Mit dem Befehl ``Ì.shape`` kann die Größe einer Matrix bestimmt werden.
````python
m, n, k = I.shape  # Größe ansehen
````
Bei einer Bildmatrix: Der erste Index ist der Zeilenindex (Bildkoordinaten: y-Achse), der zweite
Index ist der Spaltenindex (Bildkoordinaten: x-Achse), wobei der Punkt (0,0) dem linken oberen
Bildpunkt entspricht. Der dritte Index ist der Farbkanal.

## Bild anzeigen
Zum Anzeigen eines Bildes steht die Funktion ``cv2.imshow()`` zur Verfügung. Der Name des Fensters und die Bildvariable wird als
Parameter übergeben. Ein neues Fenster öffnet sich und zeigt das Bild an.

````python
cv2.imshow("Fenstername", I)  #Bild anzeigen
cv2.waitKey(0)  # Auf Tastendruck warten
````
Der Befehl ``cv2.waitKey(TIME)`` wird benötigt, damit das Programm auf eine Aktion des Benutzers wartet. Wenn der Parameter
dabei 0 ist, wartet das Programm unendlich lange auf den nächsten Tastendruck des Nutzers.

## Bild speichern
Zum Abspeichern der Bilddaten steht die Funktion ``cv2.imwrite(SPEICHER_PFAD, BILD)`` zur Verfügung. Die Bildvariable wird
als zweite Parameter und der Dateiname in Hochkommata als erster Parameter übergeben.
````python
cv2.imwrite('newimage.bmp', I)  # Bilddaten abpeichern
````
Wenn die Verzeichnisstruktur nicht angegeben wird, speichert Python die Datei im aktuellen
Arbeitsverzeichnis.

# Aufgabe a)
Implementieren und testen Sie alle Funktion in einem neuen Skript [a.py](a.py)!