class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        
def BubbleSort(value):
    for passnum in range(len(value)-1,0,-1):
        for i in range(passnum):
            if value[i]>value[i+1]:
                temp = value[i]
                value[i] = value[i+1]
                value[i+1] = temp

        
c0 = Mahasiswa('Iko',9,'Sukoharjo')
c1 = Mahasiswa('Budo',2,'Sragen')
c2 = Mahasiswa('Ahmado',10,'Surakarta')
c3 = Mahasiswa('Chandro',1,'Surakarta')
c4 = Mahasiswa('Eko',7,'Boyolali')
c5 = Mahasiswa('Fando',3,'Salatiga')
c6 = Mahasiswa('Deno',6,'Klaten')
c7 = Mahasiswa('Galoh',4,'Wonogiri')
c8 = Mahasiswa('Janto',5,'Klaten')
c9 = Mahasiswa('Haso',8,'Karanganyar')
c10 = Mahasiswa('Khalido',11,'Purwodadi')

DaftarAngka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(DaftarAngka)
print(DaftarAngka)
