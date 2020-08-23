class Segitiga():

    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return f'Modul menghitung rumus-rumus tentang segitiga, alas = {self.a} dan tinggi = {self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2