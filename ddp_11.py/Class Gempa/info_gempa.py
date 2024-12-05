from Gempa import *

#  Membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("JayaPura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Info gempa
print('## Gempa Bumi Info ##')
print()
gempa1.dampak() #memanggil method dampak(

print()
print(' ## Gempa Bumi Info ##')
print()
gempa2.dampak() # Memanggil method dampak

print('## Gempa Bumi Info ##')
print()
gempa3.dampak() #memanggil method dampak(

print('## Gempa Bumi Info ##')
print()
gempa4.dampak() #memanggil method dampak(

print('## Gempa Bumi Info ##')
print()
gempa5.dampak() #memanggil method dampak(

