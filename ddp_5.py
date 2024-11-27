pilih = int(input("""Selamat datang di aplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga
masukan pilihan anda : \n"""))

match pilih:
     case 1 :
         print("Kamu memilih 1 untuk menghitung luas persegi")
         sisi = int(input("masukan sisi persegi: "))
         luasPsg = sisi*sisi
         print("luas persegi yang sisinya ",sisi, "adalah", luasPsg)

     case 2 :
         print("Kamu memilih 2 untuk menghitung lingkaran")
         jari2 = int(input("masukan jari-jari: "))
         luasLkr = 3.14 * jari2 * jari2
         print("luas lingkaran yang jari-jarinya", jari2, "adalah", luasLkr)

     case 3 :
         print("kamu memilih 3 untuk menghitung segitiga")
         alas = int(input("masukan alas segitiga: "))
         tinggi = int(input("masukan tinggi segitiga: "))
         luassegitiga = 0.5 * alas * tinggi
         print("luas segitiga dengan alas",alas, "dan tinggi",tinggi, "adalah",luassegitiga)
     case _:
         print("Anda salah pilih")


# Meminta input dari pengguna untuk setiap atribut
nama_kendaraan = input("Masukkan nama kendaraan: ")
jenis_kendaraan = input("Masukkan jenis kendaraan: ")
cc_kendaraan = input("Masukkan cc kendaraan: ")
warna_kendaraan = input("Masukkan warna kendaraan: ")
roda_kendaraan = input("Masukkan jumlah roda kendaraan: ")
harga_kendaraan = input("Masukkan harga kendaraan: ")
tipe_kendaraan = input("Masukkan tipe kendaraan: ")
merk_kendaraan = input("Masukkan merk kendaraan: ")

# Membuat list awal
kendaraan = [nama_kendaraan, jenis_kendaraan, cc_kendaraan, warna_kendaraan, roda_kendaraan]

# Menambahkan value di akhir list
kendaraan.extend([harga_kendaraan, tipe_kendaraan])

# Menambahkan value setelah 'jenis_kendaraan'
index_jenis = kendaraan.index(jenis_kendaraan)
kendaraan.insert(index_jenis + 1, merk_kendaraan)

# Output akhir dari list kendaraan
print("List kendaraan yang dimasukkan:",kendaraan)