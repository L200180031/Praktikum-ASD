class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class buatArray(object):
    #membuat list
    internalData = 11*[None]

    #mengambil data di list
    def __getitem__(self, item):
        return self.internalData[item]

    #mengatur posisi data dan index-nya pada list
    def __setitem__(self, key, value):
        self.internalData[key] = value

    #03
    def cariuangkecil250k(self):
        terkecil = 250000
        d = []
        for i in self:
            if i.uangSaku < terkecil:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        for i in d:
            print (i)

c = buatArray()
c[0] = MhsTIF('Ika',10,'Sukoharjo', 240000)
c[1] = MhsTIF('Budi',51,'Sragen', 230000)
c[2] = MhsTIF('Ahmad',2,'Surakarta', 250000)
c[3] = MhsTIF('Eka',4,'Boyolali', 240000)
c[4] = MhsTIF('Fandi',31,'Salatiga', 250000)
c[5] = MhsTIF('Deni',13,'Klaten', 245000)
c[6] = MhsTIF('Galuh',5,'Wonogiri', 245000)
c[7] = MhsTIF('Janto',23,'Klaten', 245000)
c[8] = MhsTIF('Chandra',18,'Surakarta', 235000)
c[9] = MhsTIF('Hasan',64,'Karanganyar', 270000)
c[10] = MhsTIF('Khalid',29,'Purwodadi', 265000)


print ("Mahasiswa dengan uang saku kurang dari 250.000 adalah :")
c.cariuangkecil250k()
