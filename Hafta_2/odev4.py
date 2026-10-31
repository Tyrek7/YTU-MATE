def kontrol():
    try:
        vize=int(input("\nVize: "))
        final=int(input("\nFinal: "))
    except ValueError:
        vize,final=kontrol()
    return vize,final

vize,final=kontrol()

o=(vize*0.4)+(final*0.6)

if o >= 90:
    harfnot="AA"
elif o >= 85:
    harfnot="BA"
elif o >= 80:
    harfnot="BB"
elif o >= 75:
    harfnot="CB"
elif o >= 70:
    harfnot="CC"
elif o >= 65:
    harfnot="DC"
elif o >= 60:
    harfnot="DD"
elif o >= 50:
    harfnot="FD"
elif o >= 0:
    harfnot="FF"

print(f"\nNot Ortalama: {o} \n\nHarf Not: {harfnot}\n")