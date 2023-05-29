from asyncio.windows_events import NULL
from http import client
import requests
from bs4 import BeautifulSoup
import sqlite3

con=sqlite3.connect("COMPUTERS.db")
cursor=con.cursor()
print("Baglanti gerçekleştirildi")

a=NULL
b=NULL
c=NULL
d=NULL
e=NULL
f=NULL
g=NULL

def tabloolustur():
            cursor.execute("CREATE TABLE IF NOT EXISTS Urunler (isim TEXT,fiyat INT,puan INT,site TEXT,Marka TEXT,islemcimodeli TEXT,EkranBoyutu TEXT,İşletimSistemi TEXT,İşlemciHızı TEXT,RAM TEXT,DiskTürü TEXT,DiskKapasitesi INT,ÜrünLinki TEXT)")
            

def degerekle():

            cursor.execute("INSERT  INTO Urunler (isim,fiyat,puan,site,Marka,islemcimodeli,EkranBoyutu,İşletimSistemi,İşlemciHızı,RAM,DiskTürü,DiskKapasitesi,ÜrünLinki) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(urunun_adi,urunun_fiyati,urunun_puani,urunun_sitesi,markasinin_adi,a,b,d,c,e,f,g,urunun_linki))
            con.commit()
            
vatanToplamUrun = 0
for page in range(1,10):
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    vatan_url = "https://www.vatanbilgisayar.com/lenovo-huawei-hp-dell-casper-asus-apple-acer-msi/notebook/?page=" + str(page)
    vatan_r = requests.get(vatan_url)
    #print(r.content)
    vatan_soup = BeautifulSoup(vatan_r.content,"lxml")
    #print(soup)
    urunler = vatan_soup.find_all("div",attrs={"class":"product-list product-list--list-page"})
    #print(vatan_urunler)
    for urun in urunler:
        urun_link_basi = "https://www.vatanbilgisayar.com/"
        urun_link_devam = urun.a.get("href")
        urunun_linki = urun_link_basi + urun_link_devam
        print("Ürünün Linki: {}".format(urunun_linki))

        urunun_adi = urun.find("div",attrs={"class":"product-list__product-name"}).text.strip()
        print("Ürünün Adı: {}".format(urunun_adi))

        urunun_fiyati = urun.find("span",attrs={"class":"product-list__price"}).text
        print("Ürünün Fiyatı: {}TL".format(urunun_fiyati))

        #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        try:
            urun_r = requests.get(urunun_linki)
            vatanToplamUrun += 1
        except Exception:
            print("ürün detayı alınamadı.")

        urun_soup = BeautifulSoup(urun_r.content,"lxml")

        markasinin_adi = urun_soup.find("div", attrs={"class": "wrapper-product-brand"}).find("img").get("title")
        markasinin_linki = urun_soup.find("div", attrs={"class": "wrapper-product-brand"}).find("a").get("href")
        marka_linki = urun_link_basi + markasinin_linki

        print("Ürünün Markasının Adı: {}".format(markasinin_adi))
        print("Ürün Markasının Linki: {}".format(marka_linki))

        urunun_puani = urun_soup.find("strong", attrs={"id": "averageRankNum"}).text
        print("Ürünün Puanı: {}".format(urunun_puani))

        urunun_sitesi = urun_soup.find("h4", attrs={"class": "footer-title"}).text
        print("Ürünün Sitesi: {}".format(urunun_sitesi))

        #urunun_fotosu = vatan_urun_soup.find("a",attrs={"data-fancybox":"images"})
        urunun_fotosu = urun_soup.find("img", attrs={"class": "swiper-lazy img-responsive wrapper-main-slider__image"}).get("data-srcset")
        print("Ürünün Fotosu: {}".format(urunun_fotosu))

        ozellikler = urun_soup.find_all("li", attrs={"data-count": "0"})
        for ozellik in ozellikler:
            urun_ozelligi = ozellik.find("span",attrs={"class":"property-head"}).text
            urun_ozelligi_devam = ozellik.find_all("span")[1].text
            print("{}{} ".format(urun_ozelligi,urun_ozelligi_devam))


            if(urun_ozelligi.find("İşlemci Numarası"))!=-1:
                a=urun_ozelligi_devam
            if(urun_ozelligi.find("Ekran Boyutu"))!=-1:
                b=urun_ozelligi_devam
            if(urun_ozelligi.find("İşlemci Nesli"))!=-1:
                d=urun_ozelligi_devam
            if(urun_ozelligi.find("İşlemci Hızı"))!=-1:
                c=urun_ozelligi_devam
            if(urun_ozelligi.find("Bellek Kapasitesi"))!=-1:
                e=urun_ozelligi_devam
            if(urun_ozelligi.find("Disk Türü"))!=-1:
                f=urun_ozelligi_devam
            if(urun_ozelligi.find("Disk Kapasitesi"))!=-1:
                g=urun_ozelligi_devam
                

        degerekle()
        print("-"*200)
print("Vatan toplam ürün sayısı: {}".format(vatanToplamUrun))