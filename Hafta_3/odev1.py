import time

def kontrol():
    try:
        gerisayim=int(input("Geri Sayım Süre: "))
    except ValueError:
        gerisayim=kontrol()
    return gerisayim

gerisayim=kontrol()

while gerisayim > 0:
    print(gerisayim)
    gerisayim -= 1
    time.sleep(1)

print("Ateşle")