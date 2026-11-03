import random

def kontrol():
    try:
        tahmin=int(input("Sayı Tahmin Et: "))
    except ValueError:
        tahmin=kontrol()
    return tahmin

sayi= random.randint(1,100)
tahmin=kontrol()

while sayi != tahmin:
    if sayi > tahmin:
        print("Yukarı Çık")
        tahmin=kontrol()
    elif sayi < tahmin:
        print("Aşağı İn")
        tahmin=kontrol()

print("Doğru Bildin")
        