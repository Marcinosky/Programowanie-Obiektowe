
"""
Stwórz prost ˛a klas ˛e Ball. Niech zawiera atrybuty, które definiuj ˛a:
	• liczb ˛e, która jest umieszczona na kuli;
	• wartość typu boolean, która określa, czy kula została dodatkowo doci ˛ażona.

Stwórz klas ˛e LotteryMachine. Powinna zawierać list ˛e złożon ˛a z 49 różnych kul, każda
z nich o innym numerze, 6 z nich to kule oszukane, dodatkowo obci ˛ażone. Ma zawierać
dwie publiczne metody:
	• start() – rozpoczyna proces losowania;
	• stop() - kończy proces losowania i zwraca 6 pierwszych kul z listy.

Sam proces losowania zamieść w prywatnej metodzie o dowolnej nazwie. Losowanie
ma si ˛e odbywać według nast ˛epuj ˛acych założeń:
	• pomi ˛edzy wywołaniami metod stop() oraz start() co 10 ms ma nast ˛epować
	zmiana ułożenia kul na liści;
	• w ramach tej zmiany dwie losowo wybrane kule maj ˛a zostać zamienione miejscami, a wszystkie kule oszukane maj ˛a zostać przesuni ˛ete o jedno miejsce "w gór ˛e"
	(tj. w kierunku pocz ˛atku) listy.

Stwórz klas ˛e LottoPresenter, której zadaniem b ˛edzie: przywitanie widzów (wypisz
tekst przy użyciu funkcji print()), ustalenie czasu trwania losowania (czas trwania
losowania wczytuj z konsoli), uruchomienie metody start() klasy LotteryMachine,
wywołanie metody stop() klasy LotteryMachine po upływie ustalonego czasu, prezentacja wyników losowania.
Klasa LottoPresenter powinna zawierać metod ˛e main() - steruj ˛ac ˛a programem. Zaprezentuj wynik losowania dla kilku różnych czasów losowania.

Proponowany podział pracy: pierwsza osoba - klasy Ball oraz LotteryMachine, druga osoba - klas ˛e LottoPresenter oraz program testuj ˛acy.
"""

import lotterymachine
import lotto_presenter
from time import sleep

if __name__ == '__main__':

    test = lotto_presenter.LottoPresenter()
    test.main()
