#tugas1
angka =int(input("masukan angka :"))
ganjil = "Bilangan Ganjil"
genap = "Bilangan genap"

if angka % 2 == 0:
   print("bilangan genap")
elif angka % 2 != 0:
   print("bilangan ganjil")
else:
   print("Input tidak valid")
print("==========no 1=============")

#tugas2
nilaiujian = int(input("Masukan nilai ujian :"))

nilaiujian = 80

if 80 >= 75: #true
   print("Lulus")
else :
   print("Tidak Lulus")
print("======no 2=======")

#tugas3
usia = int(input("Masukan usia anda :"))

if usia >=18:
   print("Dewasa")
elif usia <= 18 and usia > 13:
   print("remaja")
else :
   print("Anak-anak")
print("=====no 3========")

#tugas4
statusAnggota= input("Masukkan Status anggota :")

if statusAnggota == "Gold" or statusAnggota =="Silver":
    print("Selamat anda mendapatkan Diskon")
elif statusAnggota == "Bronze":
    print("Maaf anda tidak mendapatkan diskon")
else:
    print("Input tidak valid")
print("=========no 4=========")

#tugas5:
jumlah_pembelian = int(input("Masukkan Jumlah pembelian: "))
harga_item = 1000
harga_diskon = harga_item * jumlah_pembelian * (10/100)
harga_total = harga_item * jumlah_pembelian
totaldengandiskon = harga_total - harga_diskon

print (f"Anda mendapat diskon 10%, harga per item {harga_item} jadi total yang harus dibayar {totaldengandiskon}") if jumlah_pembelian > 100 else print(f"Harga per item {harga_item}, jadi total yang harus dibayar adalah {harga_total}")
print("=========no 5==========")