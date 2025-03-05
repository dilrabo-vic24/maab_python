def invest(sarmoya, yillik_foiz, yillar):
    for yil in range(1, yillar + 1):
        sarmoya = sarmoya + sarmoya * yillik_foiz//100
        print(f"Yil {yil}: ${sarmoya:.2f}")


sarmoya = float(input("Sarmoya miqdorini kiriting: "))
yillik_foiz = float(input("Yillik foizni kiriting: "))
yillar = int(input("Yillar miqdorini kiriting: "))

invest(sarmoya, yillik_foiz, yillar)