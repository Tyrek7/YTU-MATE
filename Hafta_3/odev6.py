from datetime import datetime 

def kontrol():
    girdi=input("Vize Tarihini Girin (GG.AA.YYYY): ")
    try:
        vize_tarih= datetime.strptime(girdi, format)
    except Exception:
        vize_tarih=kontrol()
    return vize_tarih

def metin(kalan):
    text="Vizeye"
    yil=kalan//365
    ay=(kalan%365)//30
    gün=(kalan%365)%30
    if yil!=0:
        text=text+f" {yil} Yıl" 
    if ay!=0:
        text=text+f" {ay} Ay" 
    if gün!=0:
        text=text+f" {gün} Gün Kaldı" 
    return text.strip()

format="%d.%m.%Y"
simdi=datetime.now().date()
vize_tarih=kontrol().date()

if vize_tarih < simdi:
    print("Vize Geçti.")
elif vize_tarih == simdi:
    print("Vize Bugün.")
else:
    kalan=vize_tarih-simdi
    print(metin(kalan.days))