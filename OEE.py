def ekipmanEtkililikOrani():
    print("Ekipman Etkililik Oranı")
    a=float(input("Planlanmış Üretim Süresini Giriniz:"))
    b=float(input("Plansız Duruş süresini giriniz:"))
    c=float(input("Planlanmış Üretim Süresini giriniz:"))
    kullanilabilirlik=(a-b)/c
    d=float(input("Standart çevrim zamanını giriniz:"))
    e=float(input("Üretim miktarını giriniz:"))
    performans=(d*e)/(a-b)
    f=int(input("Sağlam Ürün Miktarını Giriniz:"))
    g=int(input("Toplam Üretim miktarını Giriniz:"))
    kalite=f/g
    ekipmanEtkililikOrani=kullanilabilirlik*performans*kalite*100
    print(ekipmanEtkililikOrani)
    return ekipmanEtkililikOrani
