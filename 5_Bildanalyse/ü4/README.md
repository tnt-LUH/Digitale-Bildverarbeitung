# Übung 4: Region Growing
Gegeben ist der folgende Bildausschnitt:

<p align="center">
  <img src="data/a.png">
</p>


<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{bmatrix}64&space;&179&space;&54&space;&164&space;&248&space;&94&space;&77&space;&55&space;\\208&space;&170&space;&233&space;&134&space;&222&space;&179&space;&178&space;&77&space;\\34&space;&154&space;&182&space;&69&space;&10&space;&228&space;&172&space;&178&space;\\224&space;&112&space;&89&space;&118&space;&202&space;&219&space;&63&space;&102&space;\\78&space;&251&space;&65&space;&255&space;&249&space;&79&space;&72&space;&150&space;\\160&space;&164&space;&202&space;&252&space;&56&space;&178&space;&208&space;&200&space;\\208&space;&0&space;&83&space;&172&space;&30&space;&210&space;&97&space;&255&space;\\100&space;&20&space;&187&space;&235&space;&40&space;&156&space;&92&space;&54&space;\end{bmatrix}&space;" title="\begin{bmatrix}64 &179 &54 &164 &248 &94 &77 &55 \\208 &170 &233 &134 &222 &179 &178 &77 \\34 &154 &182 &69 &10 &228 &172 &178 \\224 &112 &89 &118 &202 &219 &63 &102 \\78 &251 &65 &255 &249 &79 &72 &150 \\160 &164 &202 &252 &56 &178 &208 &200 \\208 &0 &83 &172 &30 &210 &97 &255 \\100 &20 &187 &235 &40 &156 &92 &54 \end{bmatrix} " />
</p>

## Aufgabe a)
Wenden Sie auf diesen Bildausschnitt das Region Growing Verfahren sowohl für die 4-
Nachbarschaft als auch für die 8-Nachbarschaft an. Der Seed-Punkt ist in der ersten Reihe, Spalte 5. Verwenden Sie als Homogenitätskriterium den Abstand zum mittleren Grauwert
der Region und als Schwellwert 30.
