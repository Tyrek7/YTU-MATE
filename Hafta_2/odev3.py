from datetime import datetime

x=datetime.now()
yil=x.year

def kontrol():
    try:
        dogumyil=int(input("Doğum Yılınızı Girin: "))
    except ValueError:
        dogumyil=kontrol()
    return dogumyil

dogumyil=kontrol()

if (yil-dogumyil) >= 18:
    print("Ehliyet Alabilirsin")
else:
    print("Ehliyet Alamazsın")

