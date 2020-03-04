
def jumlahHurufVokal(x):
    vokal = "AIUEOaiueo"
    a = len(x)
    b = ""
    for k in x:
        if k in vokal:
            b+=k
    c = len(b)
    return (a,c)
