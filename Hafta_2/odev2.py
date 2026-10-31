def indirim_hesapla(İndirimsizFiyat,İndirimYüzdesi):
    İndirimTutarı=İndirimsizFiyat*(İndirimYüzdesi/100)
    SonFiyat=İndirimsizFiyat-İndirimTutarı
    return İndirimTutarı, SonFiyat

def kontrol():
    try:
        indfiy=int(input("İndirimsiz Fiyat: "))
        indyüz=int(input("İndirim Yüzdesi: "))
    except ValueError:
        indfiy, indyüz = kontrol()
    return indfiy,indyüz

indfiy, indyüz = kontrol()
indtut,sonfiy=indirim_hesapla(indfiy,indyüz)
print(f"İndirim Tutarı: {indtut}\n Son Fiyat: {sonfiy}")