def katmaDegerCiro(satisMiktar,hammaddeMaliyet,bakimGider,sevkiyatGider,hizmetGider):
    global katmaDegerCiro
    katmaDegerCiro=satisMiktar-(hammaddeMaliyet+bakimGider+sevkiyatGider+hizmetGider)
    if (katmaDegerCiro>=1000):
        print("İşletme Katma Değer cirosu yüksek")
    elif (katmaDegerCiro>=500) and (katmaDegerCiro<=999):
        print("İşletme Katma Değer cirosu normaldir")
    else:
        print("İşletme Katma Değer cirosu düşüktür.")
    return katmaDegerCiro
print ("Katma Değer Ciro Hesaplama")
satisMiktar=int(input("Toplam Satış miktarını giriniz:"))
hammaddeMaliyet=int(input("Hammadde Maliyetini giriniz:"))
bakimGider=int(input("Bakım  onarım giderini giriniz:"))
sevkiyatGider=int(input("Sevkiyat giderini giriniz:"))
hizmetGider=int(input("Satın Alınan  Hizmet giderini giriniz:"))
ciro=katmaDegerCiro(satisMiktar,hammaddeMaliyet,bakimGider,sevkiyatGider,hizmetGider)


        

