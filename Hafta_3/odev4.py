def kontrol():
    try:
        n=int(input("Bir Sayı Giriniz: "))
    except ValueError:
        n=kontrol()
    return n

n=kontrol()
print(n)