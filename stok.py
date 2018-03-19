def donemBasiStok(dolapSayisi,yatakSayisi,KoltukSayisi):
    global donemBasiStokSayisi
    donemBasiStokSayisi=yatakSayisi+dolapSayisi+koltukSayisi
    return donemBasiStokSayisi
def donemSonuStok(satKoltSayisi,satDolapSayisi,satYatSayisi,alKoltSayisi,alDolapSayisi,alYatSayisi):
    global donemSonuStokSayisi
    donemSonuStokSayisi=(yatakSayisi-satYatSayisi)+(dolapSayisi-satDolapSayisi)+(koltukSayisi-satKoltSayisi)+(alKoltSayisi+alYatSayisi+alDolapSayisi)
    return donemSonuStokSayisi
def ortStok(donBasStokSayi,donSonStokSayi):
    ortalamaStokMiktari=(donemBasiStokSayisi+donemSonuStokSayisi)/2
    print("1 Yıllık Ortalama stok miktarı:",ortalamaStokMiktari)
yatakSayisi=int(30)
dolapSayisi=int(20)
koltukSayisi=int(25)
print("Dolap sayısı:",dolapSayisi)
print("Yatak sayısı:",yatakSayisi)
print("Koltuk sayısı:",koltukSayisi)
donBasStokSayi=donemBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
print("Dönem başı stok:",donemBasiStokSayisi)
satKoltSayisi=int(25)
satYatSayisi=int(20)
satDolapSayisi=int(10)
print("Satılan koltuk sayısı:",satKoltSayisi)
print("Satılan yatak sayısı:",satYatSayisi)
print("Satılan dolap sayısı:",satDolapSayisi)
alDolapSayisi=int(5)
alKoltSayisi=int(10)
alYatSayisi=int(15)
print("Alınan koltuk sayısı:",alKoltSayisi)
print("Alınan yatak sayısı:",alYatSayisi)
print("Alınan dolap sayısı:",alDolapSayisi)
donSonStokSayi=donemSonuStok(satKoltSayisi,satDolapSayisi,satYatSayisi,alKoltSayisi,alYatSayisi,alDolapSayisi)
print("Dönem sonu stok sayısı:",donemSonuStokSayisi)
stok1=donemBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
stok2=donemSonuStok(satKoltSayisi,satDolapSayisi,satYatSayisi,alKoltSayisi,alYatSayisi,alDolapSayisi)
ortStok(stok1,stok2)
