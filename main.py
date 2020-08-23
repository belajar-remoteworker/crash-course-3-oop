from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')
print('\nMenghitung Persegi Panjang')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

print('\nMenghitung Segitiga')
s1 = Segitiga(4,2)
print(s1.info())
print(s1.hitung_luas())

print('\nMenggunakan BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Polymorphism: kemampuan objeck untuk merespon berbeda, terhadap pemanggilan yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorfism')
for bangunruang in daftar_bangun_ruang:
    print(bangunruang.info())