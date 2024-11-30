import math

def l_tabung(jari2, tinggi):
    luas = 2*math.pi*(jari2 + tinggi)
    print(f'Luas Tabung adalah = {luas}')

def l_bola(Jari2):
    luas = 4*math.pi*(Jari2)
    print(f'Luas Bola adalah = {luas}')

def l_balok(panjang, lebar, tinggi):
    luas = 2*(panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
    print(f'Luas Balok adalah = {luas}')

def l_kubus(sisi):
    luas = 6 * sisi * sisi
    print(f'Luas Kubus {6} * {sisi} * {sisi} = {luas}')
    print(f'Luas Kubus adalah {luas}')

def l_prisma(luasalas, kelilingalas, tinggi):
    luas = 2*luasalas + kelilingalas * tinggi
    print(f'Luas Prisma {2} * {luasalas} + {kelilingalas} * {tinggi}')
    print(f'Luas Prisma adalah {luas}')



    
    