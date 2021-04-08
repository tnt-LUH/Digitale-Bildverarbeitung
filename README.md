![alt text](./data/tnt_banner.svg)

# Digitale Bildverarbeitung

Sehr geehrte Studierende,

dieses Github-Repository bietet Ihnen praktische Übungsmaterialien zur 
Vorlesung "Digitale Bildverarbeitung" des [Instituts für Informationsverarbeitung](https://www.tnt.uni-hannover.de/en/)
an der [Leibniz Universität Hannover](https://www.uni-hannover.de/).

Die Übungsmaterialien sollen die erlernten theoretischen Grundlagen
festigen und zusätzlich einen Einblick in die angewandte Praxis 
moderner Bildverarbeitung geben. Den Studierenden wird mit
Programmierübungen gezeigt, wie einfache, aber auch komplexe Aufgaben
mithilfe von Grundlagen der Digitalen Bildverarbeitung gelößt werden 
können. In den nächsten Abschnitten wird ein kurzer Überblick über
die Struktur und Inhalte dieses Online-Kurses gegeben.

Die Autoren dieser Übungen würden sich freuen, wenn dieses Repository
das Interesse von Studierenden an der Bildverarbeitung wecken könnte,
dass über den Erwerb von Leistungspunkten hinaus geht.

Gez. die Autoren

---

## Struktur
Dieses Repository ist unterteilt in die Themenbereiche

 0. Einführung
 1. Grundlagen
 2. Bildbearbeitung
 3. Signalorientierte Bildverarbeitung
 4. Farbrepäsentationen
 5. Bildanalyse
 
welche jeweils mit Übungsaufgaben, Lösungen sowie begleitendem Material
ausgestattet sind.

Zusätzlich sind die Ordnerstrukturen
 - *CV-App*: 
   Pipeline für die Anwendung von BV Videokonferenzen
 - *data*: Daten für die Verarbeitung, z.B. Bilder
 - *utilities*: Allgemeine Hilfsskripte und Tools
 - *Sandkasten*: Ort, um eigene Dinge auszuprobieren
 
vorhanden. Die **CV-App** nimmt dabei eine besondere Position ein, da
den Studierenden hier mit einer Interaktiven Appliaktion der praktische
Nutzen von Bildverarbeitung demonstriert wird und ebenfalls Material 
für fortgeschrittene Programmierübungen gegeben wird, welche hier nicht
explizit behandelt werden.

---

Das Erlernen der Fertigkeiten aus der Vorlesung wird mit Übungen unterstützt.
Eine herkömmliche Übung bietet den Studierenden eine oder mehrere zu lösende 
Aufgaben. Übungen sind in einem eigenen Unterordner wie z.B. **ü1** angelegt. Die Aufgaben sind in
der **README.md** beschrieben und sollen in der entsprechenden Datei mit Dateinamen wie `a.py` gelößt werden.
Zu jeder Übung gibt es eine Lösungsdatei mit einer
(von möglicherweise vielen!) Musterlösung. Die Lösungen sind mit der
Bennenung von z.B. `l_a.py` gekennzeichnet. 

---

Im folgenden werden die Themenschwerpunkte des Kurses kurz erläutert.

### 0. Einführung
Der Themenbereich **Einführung** hilft den Studierenden bei der Installation,
Einrichtung und der ersten Nutzung der Arbeitsumgebungumgebung für diesen 
Kurs. Es wird noch nicht auf den Themenkomplex Bildverarbeitung 
eingegangen. 

Das Kapitel ist für Neulinge in den folgenden Bereichen zu empfehlen:

 - **Installation Python und/oder PyCharm**
 - **Programmierung Python**
 - **OpenCV und Numpy**

### 1. Grundlagen
Um mit Methoden der Digitalen Bildverarbeitung zu arbeiten, lohnt sich ein Blick auf die Grundlagen.
Das Unterverzeichnis *1_Grundlagen* bietet Aufgaben zum Themengebiet "Grundlagen" in der Vorlesung. 
Dabei sollen ins besondere die Themen

- **Das menschliche visuelle System**
- **Technische Bilderfassung/Sensoren**
- **Das Digitale Bild**

mit zusätzlichem Material unterstützt werden.

### 2. Bildbearbeitung
In diesem Kapitel werden Ihnen verschiedene Klassen von Operationen und Methoden erläutert und mit Beispielen 
exemplarisch dargestellt. Die Übungen zeigen Beispiele zu den Themen 
- **Punktoperationen (Intensitätstransformationen)**
- **Lokale Operationen (Filterung)**
- **Globale Operationen**
- **Geometrische Transformationen**

### 3. Signalorientierte Bildverarbeitung

Bilder werden üblicherweise als örtlich-/zeitliches Signal betrachtet. In der Digitalen Bildverarbeitung werden Bilder
häufig auch in anderer Signalform betrachtet, z.B. im Frequenzraum. Die Grundlagen der signalorientierten Bildverarbeitung 
werden in diesem Kapitel behandeln. Die Aufgaben in diesem Unterverzeichnis geben dazu Informationen und Beispiele zu den Themen

- **Das Bild als Signal**
- **Grundlagen unitäre Transformation**
- **Fourier-Transformation**
- **LSI‐Systeme, Faltung und Fourier‐Transformation**
- **Abtastung und Rekonstruktion, Abtasttheorem**
- **Filterung des Bildes**
- **Unitäre Transformationen: DCT, Hadamard‐, Haar‐, Wavelet‐Transformation**
- **Bildpyramiden und Multiresolutiondarstellung**

### 4. Farbrepäsentationen
Die Wahrnehmung von "Farbe" wird in technischen Anwendungen in verschiedenen Formen dargestellt und codiert. Zu
den Grundlagen der Farbrepräsentationen werden in diesem Kapitel Aufgaben und Beispiele bereitgestellt. 
Die Aufgaben behandeln die Themengebiete

- **Additive Subtraktive Farbmischung**
- **Farbempfinden und technische Repräsentation von Farbe**
- **Farbmodelle/Farbräume und Konvertierung**
- **Weißabgleich**

### 5. Bildanalyse
Ein Ziel der Digitalen Bildverarbeitung ist die Extrahierung von Informationen aus Bilddaten, um nachfolgende Aufgaben
zu lösen. In diesem Kapitel werden einige Beispiele und Aufgaben zur Bildanalyse bereitgestellt. Dabei werden die Themen

- **Diskrete Geometrie und Analyse von Binärbildern**
- **Bildsegmentierung**
- **Template-Matching und Korrelation**
- **Hough**

behandelt.

---

## FAQ, Kommentare und Hinweise
 - Dieses Repository hat keinen Anspruch auf Vollständigkeit
 - Hauptsprache der Kurses ist Deutsch
 - Interessierte dürfen eigene Übungen erstellen und per Pull-Request
 in das Repository einpflegen. Vielen Dank für das Engagement!
 - Viel Spaß beim Lernen!
