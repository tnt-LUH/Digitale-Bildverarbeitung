# CV-Application

Die CV-App ist eine Applikation, mit der eine virtuelle Webcam generiert wird. Dafür wird eine reale Kamera 
ausgelesen. Der Inhalt des Videostreams wird dann durch CV-Algorithmen be- und/oder verarbeitet und dann an eine neue,
virtuelle Kamera weitergeleitet. Diese virtuelle Kamera kann dann von anderen Programmen wie eine normale Kamera 
ausgelesen werden.


## Anleitung

Für die Nutzung der virtuellen Kamera ist ein  zusätzlicher Treiber notwendig. Je nachdem welches Betriebssystem Sie 
nutzen, kann dieser variieren. Die nötige Treiber Installation finden Sie unter
 [https://github.com/letmaik/pyvirtualcam](https://github.com/letmaik/pyvirtualcam).

Führen Sie die Datei `main.py` in PyCharm aus oder führen Sie das Skript aus diesem Directory mit dem Befehl

```bash
python main.py --camera=0 --mode=virtual_cam --video=PFAD_ZU_EINEM_VIDEO
```

direkt im Terminal aus. Der Parameter `--camera` wählt dabei die gewünschte Kamera aus (Aufzählung beginnend bei 0). 
Sollten Sie keine Kamera zur Verfügung haben, können Sie auch -1 wählen, um ein vorgefertigtes Video zu verwenden.
Mit dem Argument `--video` können Sie ein Pfad zu einem Video angeben, falls sie `--camera=-1` angegeben haben.
Der Parameter `--mode` wählt den Modus des Programs aus. Sie können zwischen *virtual_cam* (erstellen einer virtuellen 
Kamera) oder *screen* (Darstellung des Videostreams auf dem Screen) wählen. Wenn Sie Parameter nicht auswählen, werden
die default Werte, wie in ``main.py`` definiert gewählt. Sollten Sie die Applikation in PyCharm nutzen, werden keine
Parameter ausgewählt, sodass Sie die Parameter in der Datei `main.py` anpassen müssen.

## Eigene CV Algorithmen
 
## Anforderungen
Getestet mit Python Versionen:
 - 3.6
 
Gestet auf Betriebssystemen:
 - Windows 10   
 -OpenSuse (pyvirtualcam funktioniert nicht!)
    