def ilkGelirHesapla(yazilimGeliri,finansmanGeliri,urunGelir):
    global ilkToplamGelir
    ilkToplamGelir=yazilimGeliri+finansmanGeliri+urunGelir
    return ilkToplamGelir
def ilkGiderHesapla(calisanGider,kiraGider,donanimMaliyet):
    global ilkToplamGider
    ilkToplamGider=calisanGider+kiraGider+donanimMaliyet
    return ilkToplamGider
def ilkKarHesapla(ilkToplamGelir,ilkToplamGider):
    global ilkKar
    ilkKar=ilkToplamGelir-ilkToplamGider
    return ilkKar
def sonGelirHesapla(yazilimGeliri,urunGelir,sponsorlukGelir,eTicaretGelir):
    global sonToplamGelir
    sonToplamGelir=yazilimGeliri+urunGelir+sponsorlukGelir+eTicaretGelir
    return sonToplamGelir
def sonGiderHesapla(calisanGider,kiraGider,bakimMaliyet):
    global sonToplamGider
    sonToplamGider=calisanGider+kiraGider+bakimMaliyet
    return sonToplamGider
def sonKarHesapla(sonToplamGelir,sonToplamGider):
    global sonKar
    sonKar=sonToplamGelir-sonToplamGider
    return sonKar
def yillikKarHesapla(ilkKar,sonKar):
    yillikKar=sonKar-ilkKar
    if (yillikKar>=5000):
        print("İşletme Çok Karlı")
    elif (yillikKar>=1000) and (yillikKar<=4999):
        print("İşletme Karı Normal")
    else:
        print("İşletme Karı düşük")
print("Lütfen İlk ve son 6 aylık değerleri giriniz")
yazilimGeliri=int(input("Yazılım gelirini giriniz:"))
finansmanGeliri=int(input("Finansman gelirini giriniz:"))
urunGelir=int(input("Ürün satış gelirini giriniz:"))
calisanGider=int(input("Çalışan giderlerini giriniz:"))
kiraGider=int(input("Kira gideriniz:"))
donanimMaliyet=int(input("Donanım maliyetini Giriniz:"))
sponsorlukGelir=int(input("Sponsorluk gelirini Giriniz:"))
eTicaretGelir=int(input("E-Ticaret gelirinizi giriniz:"))
bakimMaliyet=int(input("Bakım maliyetlerini giriniz:"))
ilkGelir=ilkGelirHesapla(yazilimGeliri,finansmanGeliri,urunGelir)
ilkGider=ilkGiderHesapla(calisanGider,kiraGider,donanimMaliyet)
ilkKarHesapla(ilkGelir,ilkGider)
sonGelir=sonGelirHesapla(yazilimGeliri,urunGelir,sponsorlukGelir,eTicaretGelir)
sonGider=sonGiderHesapla(calisanGider,kiraGider,bakimMaliyet)
sonKarHesapla(sonGelir,sonGider)
ilkKar=ilkKarHesapla(ilkToplamGelir,ilkToplamGider)
sonKar=sonKarHesapla(sonToplamGelir,sonToplamGider)
yillikKarHesapla(ilkKar,sonKar)

        
                                        
    
