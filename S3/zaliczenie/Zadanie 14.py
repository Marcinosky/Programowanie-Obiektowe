import matplotlib.pyplot as plt
from sys import implementation
from time import perf_counter
import random
from pathlib import Path

X, Y = 1000, 500        #globalne wymiary pliku arrays.txt (przy zmianie wartości pamiętaj o usunięciu pliku arrays.txt)

def tworzenie():
    Path("pliki").mkdir(parents=True, exist_ok=True)
    try:
        plik = open("pliki/arrays.txt", "x")
        for i in range(X):
            for j in range(Y):
                plik.write(str(random.randint(-2000,2000))+" ")
            plik.write('\n')
        plik.close()
    except FileExistsError:
        print('Wykryto stworzony plik, jesli chcesz sprawdzic dzialanie programu na nowym pliku, usun arrays.txt')

#algorytmy sortowania

def bubble_sort(tab,n):
    t1_start = perf_counter()
    for i in range(n-1):
        for j in reversed(range(i+1, n)):
            if(tab[j]<tab[j-1]):
                tab[j],tab[j-1]=tab[j-1],tab[j]
    t1_stop = perf_counter()
    return t1_stop-t1_start
    

def selection_sort(tab,n):
    t1_start = perf_counter()
    for i in range(n-1):
        k=i
        for j in range(i+1, n):
            if(tab[j]<tab[k]):
                k=j
        tab[i],tab[k]=tab[k],tab[i]
    t1_stop = perf_counter()
    return t1_stop-t1_start

def insertion_sort(tab,n):
    t1_start = perf_counter()
    for i in range(2, n):
        x = tab[i]
        tab[0] = x
        j = i-1
        while(x<tab[j]):
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = x
    t1_stop = perf_counter()
    return t1_stop-t1_start

def rysuj(plik,sort):
    tab = plik.read().splitlines()
    for i in range(len(tab)):     
        tab[i] = float(tab[i])
    title = 'Wykres czasu do wykonania algorytmu sortowania ' + sort
    plt.plot(tab)
    plt.title(title)
    plt.ylabel('Czas wykonania [s]')
    plt.show()

#początek

print('Program napisany na zaliczenie z przedmiotu Jezyki Skryptowe\nNapisal Seweryn Marcinowski index 151921\n')

tworzenie()                         #wywołanie tworzenia pliku arrays.txt

#główna część programu

plik = open('pliki/arrays.txt')
plik_b = open('pliki/babelkowe.txt','w')
plik_s = open('pliki/wybieranie.txt','w')
plik_i = open('pliki/wstawienie.txt','w')

timesb,timess,timesi=0,0,0          #wywołanie sumatora czasu wykonania

for a in range(X):
    ogtab = plik.readline().split() 
    for i in range(len(ogtab)):     #zmiana typu liczb w tabeli
        ogtab[i] = int(ogtab[i])    #ze string na integer
    
    tabb, tabs, tabi = ogtab.copy(), ogtab.copy(), ogtab.copy()
     
    timeb = bubble_sort(tabb,Y)
    times = selection_sort(tabs,Y)
    timei = insertion_sort(tabi,Y)
    
    plik_b.write(str(timeb) + "\n")
    plik_s.write(str(times) + "\n") #zapisywanie wszystkich czasow do pliku
    plik_i.write(str(timei) + "\n")
    
    timesb += timeb
    timess += times         #sumowanie sredniego czasu
    timesi += timei

plik.close()
plik_b.close()
plik_s.close()
plik_i.close()

#wyjście programu

plik_b = open('pliki/babelkowe.txt')
plik_s = open('pliki/wybieranie.txt')
plik_i = open('pliki/wstawienie.txt')

print("Sredni czas wykonania algorytmu sortowania babelkowego wynosi ", round(timesb/X,5), " sekund.")
rysuj(plik_b,'babelkowego')
print("Sredni czas wykonania algorytmu sortowania przez wybieranie wynosi ", round(timess/X,5), " sekund.")
rysuj(plik_s,'przez wybieranie')
print("Sredni czas wykonania algorytmu sortowania przez wstawienie wynosi ", round(timesi/X,5), " sekund.")
rysuj(plik_i,'przez wstawienie')

plik_b.close()
plik_s.close()
plik_i.close()