def calismaSuresi2016():
    calisilanSure2016=int(170)
    toplamMusteri2016=int(50)
    global musteriCalismaSuresi2016
    musteriCalismaSuresi2016=calisilanSure2016/toplamMusteri2016
    print("2016 yılı Çalışılan süre:",calisilanSure2016)
    print("2016 yılı Toplam Müşteri:",toplamMusteri2016)
    print("2016 yılı Müşterilerle çalışma süresi:",musteriCalismaSuresi2016)
    return musteriCalismaSuresi2016
def calismaSuresi2017():
    calisilanSure2017=int(220)
    toplamMusteri2017=int(70)
    global musteriCalismaSuresi2017
    musteriCalismaSuresi2017=calisilanSure2017/toplamMusteri2017
    print("2017 yılı Çalışılan Süre:",calisilanSure2017)
    print("2017 yılı toplam müşteri:",toplamMusteri2017)
    print("2017 yılı Müşterilerle çalışma süresi:",musteriCalismaSuresi2017)
    return musteriCalismaSuresi2017
def yillikFark(musteriCalismaSuresi2016,musteriCalismaSuresi2017):
    calismaSureFark=musteriCalismaSuresi2017-musteriCalismaSuresi2016
    print("Yıllık Müşterilerle Çalışma süreleri farkı:",calismaSureFark)
calismaSureleri2016=calismaSuresi2016()
calismaSureleri2017=calismaSuresi2017()
yillikFark(calismaSureleri2016,calismaSureleri2017)

