import time
import random

class KahveOtomati():
    def __init__(self,otomat_durumu="Kapalı",kahve_menusu={"Filtre Kahve":18.50,"Flat White":23.25,"Cortado":21.00,"Espresso":18.00,"Cafe Latte": 26.00,"Latte Macchiato":27.00},hesaba_eklenen_kahve=[],hesap_tutari=0):

        self.otomat_durumu = otomat_durumu
        self.kahve_menusu = kahve_menusu
        self.hesaba_eklenen_kahve = hesaba_eklenen_kahve
        self.hesap_tutari = hesap_tutari

    def otomat_ac(self):
        if (self.otomat_durumu == "Açık"):
            print("Otomat zaten açık...")
        else:
            print("Otomat açılıyor...")
            time.sleep(1)
            self.otomat_durumu = "Açık"
            print("Otomat açıldı...")

    def otomat_kapat(self):
        if (self.otomat_durumu == "Kapalı"):
            print("Otomat zaten kapalı...")
        else:
            print("Otomat kapanıyor...")
            time.sleep(1)
            self.otomat_durumu = "Kapalı"
            print("Otomat kapandı...")

    def menuyu_goruntule(self):
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
          print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()
        print("(Orta boy fiyatları 1.25 ile, büyük boy fiyatları 1.5 ile çarpılarak elde edilir...)")

    def kahve_ve_boyut_sec(self):
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
            print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()
        kahve_secimi = input("Lütfen istediğiniz kahvenin ismini giriniz: ")
        self.hesaba_eklenen_kahve.append(kahve_secimi)
        boyut_secimi = input("Lütfen boyut seçiniz (küçük/orta/büyük): ")
        if boyut_secimi == "küçük":
            self.hesap_tutari += self.kahve_menusu[kahve_secimi]
        elif boyut_secimi == "orta":
            self.hesap_tutari += 1.25 * self.kahve_menusu[kahve_secimi]
        elif boyut_secimi == "büyük":
            self.hesap_tutari += 1.5 * self.kahve_menusu[kahve_secimi]

        print("Seçiminiz: {}, {} boyutu {} TL'dir.".format(kahve_secimi,boyut_secimi,self.hesap_tutari))

    def seker_sec(self):
        tercih = input("Şeker istiyorsanız y'ye istemiyorsanız n'ye basınız. (Şeker ücreti 2 TL'dir)  ")
        if tercih == "y":
            print("Kahvenize şeker ilave ediliyor...(+2 TL)")
            time.sleep(1)
            self.hesap_tutari += 2
        elif tercih == "n":
            print("Kahvenize şeker ilave edilmiyor...")

    def fis_al(self):
        with open("hesap.txt", "a", encoding="utf-8") as file:
            file.write(str(time.ctime(time.time())))
            file.write("\n")
            file.write("Satın alınan kahve: ")
            file.write(self.hesaba_eklenen_kahve[0])
            file.write("\n")
            file.write("Kahve seçiminin ücreti: ")
            file.write(str(self.hesap_tutari))
            file.write("\n")
            file.write("*" * 20)
            file.write("\n")
        print("Hesap fişiniz başarıyla hazırlandı...")

    def sans_kahvesi(self):
        print("Şans Kahvesi Seçeneğini Seçtiniz...")
        print("Küçük Boy şans kahveniz hazırlanıyor...")
        time.sleep(1)
        rastgele = random.choice(list(self.kahve_menusu))
        self.hesaba_eklenen_kahve.append(rastgele)
        self.hesap_tutari += self.kahve_menusu[rastgele]
        print("Şans kahveniz {} oldu... Afiyet Olsun <3...".format(rastgele))

    def menuye_kahve_ekle(self):
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
            print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()
        eklenecek_kahve_ismi = input("Lütfen eklemek istediğiniz kahvenin ismini giriniz: ")
        eklenecek_kahve_fiyat = float(input("Lütfen eklediğiniz kahvenin küçük boy fiyatını giriniz: "))
        self.kahve_menusu[eklenecek_kahve_ismi] = eklenecek_kahve_fiyat
        print("Kahve Menüsünün yeni hali: ")
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
            print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()

    def fiyat_guncellemesi(self):
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
            print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()
        secim = str(input("Menüdeki kahvelerden fiyatını güncellemek istediğinizin ismini giriniz: "))
        yeni_fiyat = float(input("{} için yeni fiyatı giriniz: ".format(secim)))
        self.kahve_menusu[secim] = yeni_fiyat
        print()
        print("Kahve Menüsünün yeni hali: ")
        print("- - - - - KAHVE MENÜSÜ - - - - -")
        for (i, j) in self.kahve_menusu.items():
          print("Kahve İsmi:", i, "----- Küçük Boy Fiyatı:", j, "TL")
        print()

    def otomatDurumu(self):
        print("Otomat Durumu: {}".format(self.otomat_durumu))

def main():
    otomat = KahveOtomati()

    while (True):

        print("""
****************************************
|  ...Kahve Otomatına Hoş Geldiniz...  |
|                                      |
|  Otomatı Aç - - - - - - - - - - - 1  |
|  Otomatı Kapat- - - - - - - - - - 2  |
|  Menüyü Görüntüle - - - - - - - - 3  |
|  Kahve ve Boyut Seç - - - - - - - 4  |
|  Şeker Seçimini Yap - - - - - - - 5  |
|  Fişini Al- - - - - - - - - - - - 6  |
|  Şans Kahvesi Seç - - - - - - - - 7  |
|  Menüye Kahve Eklemesi Yap- - - - 8  |
|  Fiyat Güncellemesi Yap - - - - - 9  |
|  Otomattan Çık- - - - - - - - - - 10 |
|  Otomat Durumu- - - - - - - - - - 11 |
|                                      |
****************************************""")

        secim = input("Yapmak istediğiniz seçimi tuşlayınız: ")
        print()

        if secim == "1":
            otomat.otomat_ac()
        elif secim == "2":
            otomat.otomat_kapat()
        elif secim == "3":
            otomat.menuyu_goruntule()
        elif secim == "4":
            otomat.kahve_ve_boyut_sec()
        elif secim == "5":
            otomat.seker_sec()
        elif secim == "6":
            otomat.fis_al()
        elif secim == "7":
            otomat.sans_kahvesi()
        elif secim == "8":
            otomat.menuye_kahve_ekle()
        elif secim == "9":
            otomat.fiyat_guncellemesi()
        elif secim == "10":
            print("Otomattan çıkılıyor ve ekran karartılıyor... Yine Bekleriz....")
            break
        elif secim == "11":
            otomat.otomatDurumu()

main()