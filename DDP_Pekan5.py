{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOMSMvF/fr5JBx5F2phk2cR"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"zIHSh2MsyV2r","executionInfo":{"status":"ok","timestamp":1730365046521,"user_tz":-420,"elapsed":78379,"user":{"displayName":"Naesila","userId":"09881180266258646625"}},"outputId":"de8e0a72-cd28-43dc-aecf-4ef2a31fb744"},"outputs":[{"output_type":"stream","name":"stdout","text":["Selamat datang di aplikasi menghitung\n","1. Untuk menghitung luas persegi\n","2. Untuk menghitung luas lingkaran\n","3. Untuk menghitung luas segitiga\n","masukan pilihan anda : \n","1\n","Kamu memilih 1 untuk menghitung luas persegi\n","masukan sisi persegi: 5\n","luas persegi yang sisinya  5 adalah 25\n","Masukkan nama kendaraan: 6\n","Masukkan jenis kendaraan: Scoopy\n","Masukkan cc kendaraan: 190\n","Masukkan warna kendaraan: Merah\n","Masukkan jumlah roda kendaraan: 2\n","Masukkan harga kendaraan: 22000000\n","Masukkan tipe kendaraan: Roda sua\n","Masukkan merk kendaraan: Honda\n","List kendaraan yang dimasukkan: ['6', 'Scoopy', 'Honda', '190', 'Merah', '2', '22000000', 'Roda sua']\n"]}],"source":["pilih = int(input(\"\"\"Selamat datang di aplikasi menghitung\n","1. Untuk menghitung luas persegi\n","2. Untuk menghitung luas lingkaran\n","3. Untuk menghitung luas segitiga\n","masukan pilihan anda : \\n\"\"\"))\n","\n","match pilih:\n","     case 1 :\n","         print(\"Kamu memilih 1 untuk menghitung luas persegi\")\n","         sisi = int(input(\"masukan sisi persegi: \"))\n","         luasPsg = sisi*sisi\n","         print(\"luas persegi yang sisinya \",sisi, \"adalah\", luasPsg)\n","\n","     case 2 :\n","         print(\"Kamu memilih 2 untuk menghitung lingkaran\")\n","         jari2 = int(input(\"masukan jari-jari: \"))\n","         luasLkr = 3.14 * jari2 * jari2\n","         print(\"luas lingkaran yang jari-jarinya\", jari2, \"adalah\", luasLkr)\n","\n","     case 3 :\n","         print(\"kamu memilih 3 untuk menghitung segitiga\")\n","         alas = int(input(\"masukan alas segitiga: \"))\n","         tinggi = int(input(\"masukan tinggi segitiga: \"))\n","         luassegitiga = 0.5 * alas * tinggi\n","         print(\"luas segitiga dengan alas\",alas, \"dan tinggi\",tinggi, \"adalah\",luassegitiga)\n","     case _:\n","         print(\"Anda salah pilih\")\n","\n","\n","# Meminta input dari pengguna untuk setiap atribut\n","nama_kendaraan = input(\"Masukkan nama kendaraan: \")\n","jenis_kendaraan = input(\"Masukkan jenis kendaraan: \")\n","cc_kendaraan = input(\"Masukkan cc kendaraan: \")\n","warna_kendaraan = input(\"Masukkan warna kendaraan: \")\n","roda_kendaraan = input(\"Masukkan jumlah roda kendaraan: \")\n","harga_kendaraan = input(\"Masukkan harga kendaraan: \")\n","tipe_kendaraan = input(\"Masukkan tipe kendaraan: \")\n","merk_kendaraan = input(\"Masukkan merk kendaraan: \")\n","\n","# Membuat list awal\n","kendaraan = [nama_kendaraan, jenis_kendaraan, cc_kendaraan, warna_kendaraan, roda_kendaraan]\n","\n","# Menambahkan value di akhir list\n","kendaraan.extend([harga_kendaraan, tipe_kendaraan])\n","\n","# Menambahkan value setelah 'jenis_kendaraan'\n","index_jenis = kendaraan.index(jenis_kendaraan)\n","kendaraan.insert(index_jenis + 1, merk_kendaraan)\n","\n","# Output akhir dari list kendaraan\n","print(\"List kendaraan yang dimasukkan:\", kendaraan)"]}]}