# Übung 4: Filterkern

Ein Filterkern ist eine n-dimensionale Matrix, mit der üblicherweise eine lokale und lineare Operation auf Pixel im 
Eingangsbild angewendet wird. In dieser Übung sollen Aufgaben mit Filterkernen manuell und mit Python gelößt werden.

## Aufgabe a) Separierung
Unter Umständen ist ein 2-dimensionaler Filterkern separierbar, d.h. er durch zwei 1-dimensonale Filterkerne dargestellt
werden.  

<img src="https://latex.codecogs.com/svg.image?\bg_white&space;F_a&space;=&space;\begin{bmatrix}1&space;&&space;4&space;&&space;1&space;\\\end{bmatrix}&space;\quad&space;\text{und}&space;F_b&space;=&space;\begin{bmatrix}&space;-1\\&space;0\\1\end{bmatrix}&space;" title="\bg_white F_a = \begin{bmatrix}1 & 4 & 1 \\\end{bmatrix} \quad \text{und} F_b = \begin{bmatrix} -1\\ 0\\1\end{bmatrix} " />

![](https://latex.codecogs.com/svg.image?%5Cbg_blue%20F_a%20=%20%5Cbegin%7Bbmatrix%7D1%20&%204%20&%201%20%5C%5C%5Cend%7Bbmatrix%7D%20%5Cquad%20%5Ctext%7Bund%7D%20F_b%20=%20%5Cbegin%7Bbmatrix%7D%20-1%5C%5C%200%5C%5C1%5Cend%7Bbmatrix%7D%20)