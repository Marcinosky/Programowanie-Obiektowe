def znajdz(bigtab,tab):
    wynik = [0,0,0,0]                   # trafienia [szostki, piatki, czworki, trojki]
    for a in range(len(bigtab)):    
        suma = 0
        for i in range(6):
            for j in range(6):
                if(bigtab[a][2][i] == los[j]): suma += 1
        if(suma == 6): wynik[0] += 1   
        elif(suma == 5): wynik[1] += 1  
        elif(suma == 4): wynik[2] += 1   
        elif(suma == 3): wynik[3] += 1
    return(wynik)
    
print('Program napisany na zaliczenie z przedmiotu Jezyki Skryptowe\nNapisal Seweryn Marcinowski index 151921\n')

plik = open('pliki/dl.txt')
bd = plik.readlines()                     #
for i in range(len(bd)):                  #     czytanie 
    bd[i] = bd[i].split()                 # zawartości pliku
    bd[i][2] = bd[i][2].split(',')        #
    for j in range(6):
        bd[i][2][j] = int(bd[i][2][j])    # zamiana typu string na int
plik.close()

while True:                               # alternatywa do while  
    los = [0,0,0,0,0,0]

    print('Wprowadź swoje liczby: ')
    while True:                               
        for i in range(6):                   
            while True:                           
                los[i] = int(input(str(i+1) + ": "))
                if(los[i]>=1 and los[i]<=49): break                                 # sprawdzenie (1-49)
        if(los[0] != los[1] != los[2] != los[3] != los[4] != los[5]): break         # sprawdzenie braku powtórzeń

    znalezione = znajdz(bd, los)

    print('Od 27.01.1957 roku twoje liczby trafily ', znalezione[0], ' szostek, ', znalezione[1], ' piatek, ', znalezione[2], 'czworek i ', znalezione[3], ' trojek.')
    if(input('Kliknij N jeśli chcesz wyjść z programu ') == 'N'): break