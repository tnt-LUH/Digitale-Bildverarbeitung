# Übung 1: Rauschen

In der Vorlesung wurden Ihnen einige Bildsensoren vorgestellt. In dieser Übung sollen Sie Ihren eigenen Bildsensor verwenden:
Ihre Webcam. In dieser Übung sollen Sie erlernen, wie Sie mit OpenCV eine Kamera öffnen und das Bild anzeigen.
Daraufhin werden Sie ein technisches Problem bei der Aufnahme von Bilddaten kennenlernen: Das Rauschen.

## Aufgabe a)
Implementieren Sie in die Datei [a.py](a.py) folgende Schritte:
1. Öffnen Sie Ihre Webcam
2. Schneiden Sie ein Bildausschnitt mit 50x50 Pixels aus dem Bild aus
3. Zeigen Sie den Bildausschnitt auf den ganzen Bildschirm vergrößert an

Recherchieren Sie im Internet und/oder im Einführungskapitel nach den Funktionen `cv2.VideoCapture()`, `cv2.resize()` 
und `cv2.imshow()`. Eine Musterlösung finden Sie in der Datei [l_a.py](l_a.py).

Versuchen Sie den Inhalt vor der Kamera konstant zu halten. 

## Fragen:
- Bleibt das Bild konstant oder sehen Sie Rauschen?
- Wenn nein: Worin kann das Rauschen begründet liegen?
- Wozu kann das Rauschen führen?