# Übung 3: Fouriertransformation

In dieser Übung soll die Fouriertransformation betrachtet werden.

## Aufgabe a) Rauschen im Orts- und Frequenzbereich
Um den Umgang mit Orts- und Frequenzbereich in Matlab zu verdeutlichen und die Grundlage
für die Folgeaufgaben zu stellen, soll ein Programm geschrieben werden, das die folgenden Schritte
durchführt:

1. Öffnen Sie das Skript [a.py](a.py)
2. Transformieren Sie die Bilder *img* und *img_noise* mit ``np.fft.fft2(img)`` in den Frequenzbereich.
3. Berechnen Sie den Betrag/Amplitude der Transformierten und stellen Sie diese als Bild dar.
4. Worin unterscheiden sich die Bilder?

Die Musterlösung befindet sich in der Datei [l_a.py](l_a.py).

**Hinweise:**
- Mit der Funktion ``np.fft.fftshift(IMAGE)`` wird der Gleichanteil des Frequenzbereiches in die Mitte
des Bildes gelegt.
- Zur besseren Visualisierung des Frequenzbereiches ist es empfehlenswert, die anzuzeigenden Werte mit einem Faktor
  zu reduzieren. Das kann z.B. ``magnitudes = magnitudes / 100000`` sein.
  
## Aufgabe b) Amplituden und Phasenspektrum vertauschen

In der Datei [b.py](b.py) werden zwei Bilder geladen. Transformieren Sie sie in den Frequenzbereich und tauschen Sie die 
Winkel und Amplituden. Stellen Sie die Bilder vor und nach dem Tausch dar!

Die Musterlösung befindet sich in der Datei [l_b.py](l_b.py).
