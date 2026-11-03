def kontrol():
    try:
        n=int(input("Bir Sayı Giriniz: "))
    except ValueError:
        n=kontrol()
    return n

def ekle(n):
    if n == 1:
        toplam=n
    else:
        toplam=n+ekle(n-1)
    return toplam

def islem(n):
    a=1
    metin="1"
    while a < n:
        a+=1
        metin=metin+" + "+str(a)
    return metin

n=kontrol()
print(f"{islem(n)} = {ekle(n)}")


