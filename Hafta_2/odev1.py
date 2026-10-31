
def ayır(veriler):
    VerilerListe = veriler.split(",")
    for i,x in enumerate(VerilerListe):
        VerilerListe[i]= (x.strip()).lower()
    return VerilerListe


giris=input("Ad soyad ve yaşadığınız şehri sırayla arada virgül bırakarak giriniz: ")
veriler=ayır(giris)
print(f"Ad: {veriler[0].capitalize()} \nSoyad: {veriler[1].capitalize()}\nŞehir: {veriler[2].capitalize()}")
