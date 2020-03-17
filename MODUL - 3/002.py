#NOMER2A
def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

#NOMER2B
def buatIdentitas(m):
    n = m
    print("membuat matriks identitas dengan ordo"+str(n)+"x"+str(n))
    matriks = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matriks)
