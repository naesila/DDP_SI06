class Gempa:
    # Konstraktor Inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method penentu skala gempa
    def dampak(self):
        # Logika/Statment
        if self.skala < 2:
            print("Gempa Tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Gempa berdampak bangunan retak")
        elif 4 <= self.skala <= 6:
            print("Gempa berdampak bangunan roboh")
        elif self.skala > 6:
            print("Gempa Besar Berpotensi Tsunami")


        # Menampilka Lokasi dan Skala Gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Lokasi Gempa: {self.skala}')




