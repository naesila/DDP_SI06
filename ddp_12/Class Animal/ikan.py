from animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah {self.warna_ikan} dan jenis ikan ini {self.jenis_ikan}')

ikan = ikan('Ikan Badut', 'Plankton', 'air', 'bertelur', 'kuning dan jingga', 'air laut')
ikan.cetak_ikan()