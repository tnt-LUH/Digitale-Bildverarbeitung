# CV-Application
Original             | Geom. Transformation | Chrominanz
:-------------------------:|:-------------------------:|:-------------------------:
![](./data/cv1.png)  |  ![](./data/cv2.png) | ![](./data/cv3.png)

Die CV-App ist eine Applikation, mit der eine Bildverarbeitungs-Pipeline generiert werden kann. Die Pipeline ließt eine 
vorhandene Webcam aus. Der Inhalt dieses Videostreams wird dann durch CV-Algorithmen be- und/oder verarbeitet und angezeigt.
Optional kann der so erzeugte Videostream an eine virtuelle Kamera weitergeleitet werden. Diese virtuelle Kamera kann 
dann von anderen Programmen (z.B. für Videokonferenzen) wie eine normale Webcam ausgelesen werden.

Zwei einfache Algorithmen wie die geometrische Transformation oder die Entfernung der Luminanz sind in oberen 
Abbildungen dargestellt.


## Anleitung
### Treiber virtuelle Kamera
Die Grundfunktion der CV-App ist einsatzbereit, sobald dieses Repository erfolgreich installiert ist. Sie können Ihre
Webcam einlesen und CV-Algorithmen auf den Videostream anwenden. 
Für die Nutzung der virtuellen Kamera ist ein  zusätzlicher Treiber notwendig. Je nachdem welches Betriebssystem Sie 
nutzen, kann dieser variieren. Die nötige Treiber Installation finden Sie unter
 [https://github.com/letmaik/pyvirtualcam](https://github.com/letmaik/pyvirtualcam).

### Bedienung des Programms
Führen Sie das Skript `main.py` aus diesem Verzeichnis mit dem Befehl

```bash
python main.py --camera=0 --mode=virtual_cam --video=PFAD_ZU_EINEM_VIDEO
```

im Terminal aus. Dabei stehen Ihnen einige optionale Parameter zur Verfügung. Wenn Sie die Parameter nicht angeben,
werden die Default-Werte verwendet. Die Bedeutung der Parameter sowie die Default-Werte finden Sie in der folgenden 
Tabelle.

**Parameter** | **Default-Wert** | **Beschreibung**
:---:|:---:|:---:|
--camera| 0 | OpenCV ID der Kamera. Wenn -1 angegeben ist, wird anstelle einer Kamera ein Video in Dauserschleife gespielt. 
--mode| *virtual_cam* | Entweder *virtual_cam* (mit virtueller Kamera und Bildschirmausgabe) oder *screen* (nur Bildschirmausgabe)
--video | - | Gibt den Pfad zum Video an, wenn --camera=-1 ist

**Hinweise:** 
- Sollten Sie keine Kamera zur Verfügung haben, können Sie *--camera=-1* wählen, um ein Video zu verwenden
- Die Default-Werte sind in `main.py` definiert und können dort angepasst werden

Nachdem Sie das Programm erfolgreich gestartet haben, sollten Sie das Bild der Kamera in einem neu geöffneten Fenster
sehen. Zu Beginn der Programmausführung wird kein CV-Algorithmus auf das Bild angewendet (Eingangsbild=Ausgangsbild). 
Sie können verschiedene Funktionen bzw. Algorithmen durch betätigen verschiedener Tasten aktivieren. Als Standard sind 
einige Funktionen auf den Tasten *1* bis *10* vorprogrammiert. Es ist ebenfalls möglich, mit Maus-Aktionen mit der
Pipeline zu interagieren. 

Mit den Tasten **f** und **e** können Sie den Auto**f**okus bzw. Auto**e**xposure aktivieren oder deaktivieren.

**Hinweise:**
- Sie können nur mit der App interagieren, wenn das Programmfenster im Vordergrund ist! 
- Autofokus und Autoexposure sind für viele Webcams nicht supported!

## Eigene CV Algorithmen
Für die Implementierung eigener Algorithmen sind nur Dateien in dem Unterverzeichnis *.algorithms* notwendig. Öffnen 
Sie sich in das Verzeichnis und lesen die folgenden Abschnitte
 
### Eigenen "Algorithm" erstellen

In dem Ordner *algorithms* sind mehrere Beispiele für Algorithmen gegeben.

### Verlinken des eigenen Algorithmus zu einer Taste
Ihr Algorithmus *YourAlgorithm* kann nun zu einer Taste verlinkt werden. Der folgende Code entspricht in etwa dem Inhalt
der Datei *\_\_init\_\_.py*. Ihr Algorithmus ist in dem Beispiel an die Taste *3* verlinkt. Um weitere Algorithmen zu 
verlinken müssen Sie lediglich einen weiteren Import und einen Eintrag in das algorithmus-dictionary hinzufügen.

```python
class Algorithm:

    def process(self, img):
        return img

    def mouse_callback(self, event, x, y, flags, param):
        return

from .image_to_gray import ImageToGray
from .image_to_hue import ImageToHue
from .your_algorithm import YourAlgorithm

algorithms = dict()
algorithms["0"] = Algorithm
algorithms["1"] = ImageToGray
algorithms["2"] = ImageToHue
algorithms["3"] = YourAlgorithm
```
 
## Anforderungen
Hardware:
 - Webcam, die von OpenCV eingelesen werden kann

Getestet mit Python Versionen:
 - 3.6
 
Gestet auf Betriebssystemen:
 - Windows 10   
 - OpenSuse (pyvirtualcam funktioniert nicht!)
    