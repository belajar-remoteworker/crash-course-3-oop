class PersegiPanjang():
    def __init__(self, p, l):
        #fungsi yang dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return 'Modul menghitung rumus-rumus tentang persegipanjang'

     def hitung_luas(self):
         return self.p * self.l
