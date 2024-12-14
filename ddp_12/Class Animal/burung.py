from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
      super().__init__(nama, makanan, hidup, berkembang_biak)
      self.jenis_bulu = jenis_bulu
      self.bunyi = bunyi

    def cetak_burung(self):
     super().cetak()
     print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('-----Cetak Burung-----')
beo = Burung('Burung Beo', 'Biji bijian', 'udara', 'bertelur', 'biru dan orange', 'cukurukuku')
beo.cetak_burung()

kenari = Burung('Burung Kenari', 'buah buahan', 'udara', 'bertelur', 'kuning dan putih', 'pipipit')
kenari.cetak_burung()

nuri = Burung('Burung Nuri', 'Serbuk Sari', 'udara', 'bertelur', 'hijau', 'pcitpcit')
nuri.cetak_burung()

