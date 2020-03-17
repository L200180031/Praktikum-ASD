a = [[1,2], [3,4], [5,6]]
b = [[7,8], [9,10]]
c = [[2,6], [5,2]]
#Nomor A
class matriks(object):
    def cetakmatriks(self, matriks):
        for i in matriks:
            print(i)
    def cekkonsisten(self, matriks):
        if len(matriks[0]) == len(matriks) :
            print ("matriks konsisten")
        else:
            print ("matriks tidak konsisten")
x = matriks()
x.cetakmatriks(a)
print(x.cekkonsisten(a))
y = matriks()
y.cetakmatriks(b)
print(y.cekkonsisten(b))
            
#Nomor B
def Ordo(matriks):
    return("Ordo Matriks = "+str(len(matriks))+" x "+str(len(matriks[0])))

#Nomor C
def Jumlah(matriks1,matriks2):
    if Ordo(matriks1) == Ordo(matriks2):
        for x in range(0, len(matriks1)):
            for y in range(0, len(matriks1[0])):
                print(matriks1[x][y] + matriks2[x][y],' '),
            print()
    else:
        print("Matriks Tidak Sesuai")

#Nomor D
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("tidak memenuhi syarat")

kali(a,b)
kali(b,c)

def determinan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total
