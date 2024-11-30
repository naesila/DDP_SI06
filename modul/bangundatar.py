import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')

def lp_panjang(panjang, lebar):
    luas = panjang*lebar
    print(f'Luas Persegi Panjang {panjang} * {lebar} = {luas}')
    print(f'Luas Persegi Panjang adalah {luas}')  

def l_segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f'Luas Segitiga {1/2} * {tinggi} = {luas} ')
    print(f'Luas Segitiga adalah {luas}')

def l_lingkaran(r1, r2):
    luas = 3.14 * r1 * r2
    print(f'Luas Lingkaran {3.14} * {r1} * {r2} = {luas}')
    print(f'Luas Lingkaran adalah {luas}')


def l_jajargenjang(alas, tinggi):
    luas = alas*tinggi
    print(f'Luas Jajar Genjang {alas} * {tinggi} = {luas}')
    print(f'Luas Jajar genjang adalah {luas}')