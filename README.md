# Rozwiązywanie labiryntu za pomocą algorytmu QLearning
Program generuje losowy kwadratowy labirynt (tak aby istniała ścieżka między początkiem, a końcem) i rozwiązuje go przy pomocy algorytmu Qleaning.
Aby program zaczął działać należy uruchomić plik main.py z ewentualnymi flagami zmieniającymi działanie programu
### Znaczenie flag:
- -s, --size - rozmiar labiryntu (size x size), domyślnie = 8
- -mr, --maze-ratio - stosunek przeszkód do całej powierzchni labiryntu, domyślnie = 0.5
- -sx, --start-x - współrzędna x punktu startowego, domyślnie = 0
- -sy, --start-y - współrzędna y punktu startowego, domyślnie = 0
- -fx, --finish-x - współrzędna x punktu końcowego, domyślnie = 7
- -fy, --finish-y - współrzędna y punktu końcowego, domyślnie = 7
- -i, --iterations - liczba iteracji algorytmu Qlearning, domyślnie = 1000
- -lr, --learning-rate - współczynnik uczenia algorytmu, domyślnie = 0.9
- -dr, --discount-rate - współczynnik dyskontowania algorytmu, domyślnie = 0.9
- -er, --exploration-rate - stosunek eksploracji do eksploatacji, domyślnie = 0.1
- -ed, --exploration-decrease - spadek stosunku eksploracji po każdej iteracji, domyślnie = 0
- -me, --min-exploration-rate - minimalna wartość stosunku eksploracji, domyślnie = 0
