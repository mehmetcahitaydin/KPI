def kar():
    print("Karlılık Hesaplama")
    finansmanGelir=int(input("Lütfen Finansman Gelirini Giriniz:"))
    pazarGelir=int(input("Lütfen Pazar Gelirini Giriniz:"))
    kiraGelir=int(input("Lütfen Kira Gelirini Giriniz:"))
    toplamGelir=finansmanGelir+pazarGelir+kiraGelir
    print("Geliriniz:",toplamGelir)
    maasGider=int(input("Lüfen Maaş giderini giriniz:"))
    finansmanGider=int(input("Lütfen Finansman giderlerini giriniz:"))
    pazarGider=int(input("Lütfen Pazar giderini giriniz:"))
    kiraGider=int(input("Lütfen Kira giderini giriniz:"))
    muhasebeGider=int(input("Lütfen muhasebe giderlerini giriniz:"))
    toplamGider=maasGider+finansmanGider+pazarGider+kiraGider+muhasebeGider
    print("Gideriniz:",toplamGider)
    kar=toplamGelir-toplamGider
    if kar>=1000:
        print("İşletme Kardadır")
    else:
        print("İşletme Zarardadır")
        return kar
