from animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.jenis_ular = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah {self.warna_ular} dan jenis ular ini {self.jenis_ular}')

print('-----ular sawah-----')
sawah = ular('ular sawah', 'tikus', 'darat dan air', 'bertelur atau ovivar', 'hijau dan cokelat', 'tidak berbisa')
sawah.cetak_ular()
print('---ular sanca----')
sanca = ular('ular sanca', 'reptil', 'darat', 'ovipar', 'hijau', 'tidak berbisa') 
sanca.cetak_ular()