from asyncio.windows_events import NULL
from http import client
import requests
from bs4 import BeautifulSoup
import sqlite3
import lxml

con=sqlite3.connect("COMPUTERS.db")
cursor=con.cursor()
print("Baglanti gerçekleştirildi")
'''url="https://www.hepsiburada.com/ara?q=notebook&sayfa=1"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

list=soup.find_all("li",{"class":"productListContent"},limit=1)'''

def tabloolustur():
            cursor.execute("CREATE TABLE IF NOT EXISTS Urunler (isim TEXT,fiyat INT,puan INT,site TEXT,Marka TEXT,islemcimodeli TEXT,EkranBoyutu TEXT,İşletimSistemi TEXT,İşlemciHızı TEXT,RAM TEXT,DiskTürü TEXT,DiskKapasitesi INT,ÜrünLinki TEXT)")
            

def degerekle():
            cursor.execute("INSERT  INTO Urunler (isim,fiyat,puan,site,Marka,islemcimodeli,EkranBoyutu,İşletimSistemi,İşlemciHızı,RAM,DiskTürü,DiskKapasitesi,ÜrünLinki) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(urunAdi,urunFiyati,urun_puani,site,h,a,b,d,c,e,f,g,urunLinki))
            con.commit()

def degerekle2():
           # cursor.execute("UPDATE Urunler SET model=? WHERE model=NULL",((urun_prop,)))
           cursor.execute("UPDATE Urunler SET model=? WHERE model=NULL",(urun_prop))
           con.commit()


a=NULL
b=NULL
c=NULL
d=NULL
e=NULL
f=NULL
g=NULL
h=NULL
n11_toplamUrun = 0
for page in range(1,10):
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    n11_url = "https://www.n11.com/arama?q=laptop&m=Asus-Lenovo-HP-Dell-Msi-Monster-Acer-Huawei-Casper&ipg=" + str(page)
    html = requests.get(n11_url).content
    n11_soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    urunler = n11_soup.find_all("li", attrs={"class": "column"})
    #urunler = urunler1.find_all("div",{"class":"columnContent"})

    # print(urunler)

    for urun in urunler:
        urunAdi = urun.a.get("title")
        print("Ürün Adı:{}".format(urunAdi))
        urunLinki = urun.a.get("href")
        print(urunLinki)
        # urunFiyati = urun.span.get("newPrice cPoint priceEventClick")
        # print(urunFiyati)

        try:
            fiyat = urun.find("span", {"class": "newPrice cPoint priceEventClick"}).find("ins").text
        except Exception:
            print("fiyat yok veya alınamadı.")
        #print("Sepette Ürün Fiyatı: {}".format(fiyat))
        
        try:
            urunFiyati = urun.find("span",{"class": "newPrice cPoint priceEventClick"}).text.strip()
        except Exception:
            print(".")
        
        print("Sepette Ürün Fiyatı: {}".format(urunFiyati))
    
        # urunFiyati = urun.find("span", attrs={"class": "newPrice cPoint priceEventClick"}).text.strip()
        # print("Sepette Ürün Fiyatı: {}".format(urunFiyati))
        

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        
        try:
            urun_r = requests.get(urunLinki)
            n11_toplamUrun += 1
        except Exception:
            print(".")


        urun_soup = BeautifulSoup(urun_r.content, "html.parser")

        # urun_fiyati = urun_soup.find("div",attrs={"class":"unf-p-summary-price"}).text
        # urun_fiyati = urun_soup.ins.get("content")
        # print("Ürün Fiyatı : {}".format(urun_fiyati))

        try:
            urun_puani = urun_soup.find("strong", attrs={"class": "ratingScore"}).text
        except Exception:
            print("puan alınamadı")
        print("Ürünün Puanı: {}".format(urun_puani))

        site1 = urun_soup.find("div", attrs={"class": "columnContent"})
        site = site1.h4.text
        print("Ürün Sitesi: {}".format(site))

        tabloolustur()
        
        try:
            urun_fotosu1 = urun_soup.find("div", attrs={"class": "imgObj"})
            urun_fotosu = urun_fotosu1.a.get("href")
        except Exception:
            print("Yok")
        print(urun_fotosu)

        ozellikler = urun_soup.find_all("li", attrs={"class": "unf-prop-list-item"})
        for ozellik in ozellikler:
            urun_title = ozellik.find("p", attrs={"class": "unf-prop-list-title"}).text
            # print(urun_title)
            urun_prop = ozellik.find("p", attrs={"class": "unf-prop-list-prop"}).text
            # print(urun_prop)
            
            print("{} : {}".format(urun_title, urun_prop))

        # fiyatlar = urun_soup.find_all("div", attrs={"class": "priceContainer"})
        # for fiyat in fiyatlar:
        # urun_fiyat = fiyat.find("div",attrs={"class":"newPrice"})
        # print("Fiyatı:{}".format(urun_fiyat))

            if(urun_title.find("Model"))!=-1:
                a=urun_prop
            if(urun_title.find("Ekran Boyutu"))!=-1:
                b=urun_prop
            if(urun_title.find("İşletim Sistemi"))!=-1:
                d=urun_prop
            if(urun_title.find("İşlemci Hızı"))!=-1:
                c=urun_prop
            if(urun_title.find("Bellek Kapasitesi"))!=-1:
                e=urun_prop
            if(urun_title.find("Disk Türü"))!=-1:
                f=urun_prop
            if(urun_title.find("Disk Kapasitesi"))!=-1:
                g=urun_prop  
            if(urun_title.find("Marka"))!=-1:
                h=urun_prop    
            
            
        degerekle()       
        print("-" * 150)
print("n11 toplam ürün sayısı: {}".format(n11_toplamUrun))
con.close()

