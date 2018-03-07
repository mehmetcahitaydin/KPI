def adamBasiCiro():
    print("Ciro Hesaplama")
    satisMiktari=int(input("Satış Miktarını giriniz:"))
    birimSatisFiyati=int(input("Birim Satış Fiyatını giriniz:"))
    toplamCiro=satisMiktari*birimSatisFiyati
    calisanSayisi=int(input("Çalışan Sayısını Giriniz:"))
    adamBasiCiro=toplamCiro/calisanSayisi
    print(adamBasiCiro)
    return adamBasiCiro

    
    
