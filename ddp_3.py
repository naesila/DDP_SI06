#Soal 01
Nama= "Naesila"
Nim= "0110124113"
Rombel= "Si06"
No_telp= "6281514124732"
alamat= """Kp.Pabuaran Desa Urug
        Kec.Sukajaya Kab.Bogor"""

print ("Nama:", Nama)
print ("Nim:", Nim)
print ("Rombel:", Rombel)
print ("No_telp:", No_telp)
print ("alamat:", alamat)


#Soal02
Nama= "Aghisnafillah"
Nim= "0110124062"
Rombel= "Si06"
No_telp= "6285891980804"
alamat= """Depok, margonda,
        jln.stm mandiri Rt01/09"""

print ("Nama:", Nama)
print ("Nim:", Nim)
print ("Rombel:", Rombel)
print ("No_telp:", No_telp)
print ("alamat:", alamat)

#Soal03
#rumus = (tinggi badan - 100)-(tinggi badan - 100) * 0.1
TB=int(input('masukan tinggi badan :'))
bb_ideal=(TB - 100) - (TB - 100) *0.1

print('berat badan ideal adalah :',bb_ideal)

#soal04
celcius = int(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9/5) + 32

print(celcius, "derajat Celcius sama dengan", fahrenheit, "derajat Fahrenheit.")


#soal05
phi = 3.14
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas_alas = phi * jari_jari * jari_jari
luas_selimut = 2 * phi * jari_jari * tinggi
luas_permukaan = 2 * luas_alas + luas_selimut
keliling_alas = 2 * phi * jari_jari

print("Luas alas tabung:", luas_alas)
print("Luas selimut tabung:", luas_selimut)
print("Luas permukaan tabung:", luas_permukaan)
print("Keliling alas tabung:",keliling_alas)