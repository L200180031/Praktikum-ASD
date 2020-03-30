def BubbleSort(value):
    for passnum in range(len(value)-1,0,-1):
        for i in range(passnum):
            if value[i]>value[i+1]:
                temp = value[i]
                value[i] = value[i+1]
                value[i+1] = temp
 
DaftarAngka = [6,66,666,33,3,333,36,366]
BubbleSort(DaftarAngka)

a = DaftarAngka
DaftarAngka1 = [6,66,666,33,3,333,36,366]
BubbleSort(DaftarAngka1)

b = DaftarAngka1
DaftarAngka2 = (a+b)
BubbleSort(DaftarAngka2)

c = DaftarAngka2
print(c)
