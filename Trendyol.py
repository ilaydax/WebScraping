from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import lxml
import sqlite3


con=sqlite3.connect("COMPUTERS.db")
cursor=con.cursor()
print("Baglanti gerçekleştirildi")


def tabloolustur():
            cursor.execute("CREATE TABLE IF NOT EXISTS Urunler (isim TEXT,fiyat INT,puan INT,site TEXT,Marka TEXT,islemcimodeli TEXT,EkranBoyutu TEXT,İşletimSistemi TEXT,İşlemciHızı TEXT,RAM TEXT,DiskTürü TEXT,DiskKapasitesi INT,ÜrünLinki TEXT)")
            

def degerekle():
            cursor.execute("INSERT  INTO Urunler (isim,fiyat,puan,site,Marka,islemcimodeli,EkranBoyutu,İşletimSistemi,İşlemciHızı,RAM,DiskTürü,DiskKapasitesi,ÜrünLinki) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(urunAd,urunFiyat,urun_puani,site,urun_marka_linki,a,b,d,c,e,f,g,link_tamami))
            con.commit()

a=NULL
b=NULL
c=NULL
d=NULL
e=NULL
f=NULL
g=NULL
h=NULL
trendyolToplamUrun=0
for pi in range(1,10):
    trendyol_url = "https://www.trendyol.com/sr?wb=102323%2C101606%2C101849%2C104964%2C103505%2C105536%2C101470%2C102324%2C103502%2C107655&wc=103108&qt=laptop+&st=laptop+&os=1&pi=" + str(pi)
    r = requests.get(trendyol_url)
    #print(r.content )
    soup = BeautifulSoup(r.content,"lxml")
    #print(soup)
    urunler = soup.find_all("div",attrs = {"class":"p-card-wrppr with-campaign-view"})
    #print(urunler)

    for urun in urunler:
        #print(urun.span.text)
        link_basi = "https://www.trendyol.com"
        link_devam = urun.a.get("href")
        link_tamami = link_basi + link_devam

        urunAd = urun.find("div",attrs = {"class":"prdct-desc-cntnr"}).text
        urunFiyat = urun.find("div", attrs = {"class": "prc-box-dscntd"}).text


        print("Ürünün Adı: {}".format(urunAd))
        print("Ürünün Linki: {}".format(link_tamami))
        print("Ürünün Fiyatı: {}".format(urunFiyat))


        try:
           urun_r = requests.get(link_tamami)
           trendyolToplamUrun += 1
        except Exception:
            print("Urun detayi alinamadi.")

        urun_soup = BeautifulSoup(urun_r.content,"lxml")

        site1 = urun_soup.find("div",attrs={"class": "header"})
        site = site1.a.get("title")
        print("Ürün Sitesi: {}".format(site))

        urun_markasi = urun_soup.find("h1", attrs={"class": "pr-new-br"})
        urun_marka_linki = urun_markasi.a.get("href")
        print("Ürünün Markası: {}".format(link_basi + urun_marka_linki))

        urun_puani = urun_soup.find("div", attrs={"class": "pr-rnr-sm-p"})
        print("Ürünün Puanı: {}".format(urun_puani))

        urun_fotosu = urun_soup.find("div", attrs={"class": "base-product-image"})
        #urun_fotosu = urun_soup.img.get("src")
        #urun_fotosu = urun_fotosu1.img.get("src")
        print(urun_fotosu)

        ozellikler = urun_soup.find_all("li",attrs = {"class":"detail-attr-item"})

        for ozellik in ozellikler:
            urun_ozellik = ozellik.span.text
            urun_ozellik_devam = ozellik.b.text
            print("{} : {}".format(urun_ozellik, urun_ozellik_devam))

            if(urun_ozellik.find("Model"))!=-1:
                a=urun_ozellik_devam
            if(urun_ozellik.find("Ekran Boyutu"))!=-1:
                b=urun_ozellik_devam
            if(urun_ozellik.find("İşletim Sistemi"))!=-1:
                d=urun_ozellik_devam
            if(urun_ozellik.find("Maksimum İşlemci Hızı"))!=-1:
                c=urun_ozellik_devam
            if(urun_ozellik.find("Ram"))!=-1:
                e=urun_ozellik_devam
            if(urun_ozellik.find("Disk Türü"))!=-1:
                f=urun_ozellik_devam
            if(urun_ozellik.find("SSD Kapasitesi"))!=-1:
                g=urun_ozellik_devam
            '''if(urun_ozellik.find("Ürünün Markası"))!=-1:
                h=urun_ozellik_devam'''
                
        degerekle() 
        print("#"*200)

print("Trendyol toplam ürün sayısı: {}".format(trendyolToplamUrun))