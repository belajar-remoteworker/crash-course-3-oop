from geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
    # fungsi yang dipanggil pertama kali saat object diciptakan
        self.p=p
        self.l=l


    def info(self):
        return f'Modul menghitung rumus-rumus tentang persegipanjang, panjang = {self.p} dan lebar = {self.l}'


    def hitung_luas(self):
        return self.p * self.l

