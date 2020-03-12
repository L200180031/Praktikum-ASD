class Manusia(object):
    """kelas 'manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print ("salam, namaku",self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga (self,k):
        print("saya baru saja latihan",k)
        self.keadaan = 'lapar'
    def mengalikandengandua(self,n):
        return n*2


class Mahasiswa(Manusia):
    """class mahasiswa yang dibangun dari kelas manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        """metode inisiasi ini menutupi metode inisiasi di kelas manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotatinggal =kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama +",NIM"+ str(self.NIM)\
            +",tinggaldi" + self.kotatinggal \
            +", uangsaku Rp" + str(self.uangsaku) \
            +"tiap bulannya"
        return s
    def ambilnama (self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        """metode ini menutupi metode 'makan' nya classs manusia.
        mahasiswa kalau makan sambil belajar."""
        print("saya baru saja makan", s,"sambil belajar")
        self.keadaan = "kenyang"
    def ambilKotaTinggal(self):
        return self.kotatinggal
    def perbaruikotatinggal(self,kotabaru):
        self.kotatinggal = kotabaru
    def tambahUangSaku(self,uangtambah):
        self.uangsaku += uangtambah
    def ambilkuliah(self,mk):
        self.matkul.append(mk)
    def listkuliah(self):
        print(self.matkul)
    def hapuskuliah(self,mkhapus):
        return self.matkul.remove(mkhapus)
