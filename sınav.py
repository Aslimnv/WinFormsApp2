#Mantıksal İşlemler
#1.	Aşağıdaki ifadelerin karşısına True False yazın 
print(10>8 and 10<11 )
print(2<1 and 4>3)
print(8>=9 or 4<5)
print(not 15>10) 
print(not 6<5) 
print(17<9 or 2>21)
print(20>21 and 33<11)
print(6>4 and 0<1) 
print(9>=10 or 5<4)
print(28>25 or 1<11)

print("-"*50)

#Tip Sorgulama
#2.	Aşağıdaki ifadelerin değer tiplerini yazınız

Deger= 12 
print(type(Deger))

Deger2='123'
print(type(Deger2))

Deger3=11.33 
print(type(Deger3))

Deger4= [1,3,56,78] 
print(type(Deger4))

Deger5=(13,56,78,98,65)
print(type(Deger5))

Deger6= {13,43,56,75,12,32} 
print(type(Deger6))

Deger7={"isim": "Sadat"}
print(type(Deger7))

Deger8= '45t'
print(type(Deger8))

Deger9= 37
print(type(Deger9))

Deger10= 123.4 
print(type(Deger10))


print("-"*50)

#Tip Dönüştürme
#3.	Aşağıdaki tip dönüşümleri yapınız

a= '14.4' 
print(type(float(str(a))))

b= 18
print(type(int(float(b)))) 

c= 12 
print(type(str(int(c)))) 

d= '14'
print(type(int(str(d)))) 

e= '14.4' 
print(type(bool(str(e))))

print("-"*50)

# anahtar ve değerleri getiren fonksiyon
# anahtar ve değerlerin isimleri
#4.Verilen değerin anahtar ve değerini getiren fonksiyonu yazınız
My_dict={"Kullanicilar" : [
{"isim":"Furkan","soyisim":"ATLAN","bolum":"YBS"}
]}

for deger in My_dict["Kullanicilar"]:
    print(deger.items())


print("-"*50)

# Listeye eleman ekleme ve listeden eleman silme

#5.listeye “erik” elemanını ekleyiniz 

Meyveler=["elma", "armut" ,"kiraz"]
Meyveler.append(("erik"))
print(Meyveler)

print("-"*50)

#6.Rakamlar listesine 3 ve 5 rakamlarını sırayı bozmayacak şekilde ekleyiniz
Rakamlar=[1,2,4,6]
Rakamlar.insert(2,3)
Rakamlar.insert(4,5)
print(Rakamlar)

print("-"*50)

#7.Rakamlar listesinde son elemanı siliniz
Rakamlar.pop()
print(Rakamlar)

print("-"*50)

#8.Meyveler listesinde kirazı siliniz
Meyveler.remove(Meyveler[2])
print(Meyveler)

print("-"*50)

#9.Rakamlar ve meyveler listeleriniz tamamen siliniz
# del Meyveler
# del Rakamlar
# print(Meyveler)
# print(Rakamlar)

print("-"*50)

# for ile kalansız bölünme
# 10. 1 ile 20 arasındaki 20’de dahil  2 ve 4 e kalansız bölünen sayıları yazdıran fonksiyonu yazınız

def artis():
    boslist=[]
    for i in range(1,21):
        if i%2==0 and i%4==0:
                 boslist.append(i)
    return boslist 

print(f"Sonuçlar= {artis()}")

print("-"*50)

#11. 1’den 40’a kadar çift sayıları yazdıran fonksiyonu yazınız

def ciftsayi():
	Boslist=[]
	for i in range (1,40):
		if i%2==0:
			Boslist.append(i)
	return Boslist
print(f"1'den 40'a kadar olan çift sayılar: {ciftsayi()}")

print("-"*50)

# 1 tane fonksiyon => dışarıdan parametre alan ve dışarıya bir değer döndüren yani parametreli ve return kullanılan bir fonksiyon
#12.Dışarıdan parametre olarak alınan bir listenin içerisindeki
   # sınav notları eğer 45'den küçükse "KALDI", büyükse "GEÇTİ"
   # yazacak ve bu ifadeleri de yeni bir listeye ekleyecek ve bu listeyi de
   # return edecek fonksiyonu yazınız

def notlar(my_list):
	Boslist=[]
	for deger in my_list:
		if deger<45:
			Boslist.append("Kaldı")
		else:
			Boslist.append("Geçti")
	return Boslist
 
Notlar=[68,35,98,65,34,24,43,54]
print(f"Alınan Notlar: {Notlar}")
print(f"Sonuçlar: {notlar(Notlar)}")

print("-"*50)

#13.Dışarıdan parametre olarak alınan bir listedeki verilerin
    # karesini hesaplayıp yeni bir listeye ekleyen ve bu listeyi geri döndüren
    # fonksiyonu yazınız

def kare_al(x):
	kare_liste=[]
	for i in x:
            i = i**2
            kare_liste.append(i)
	return kare_liste

deneme_kare_list=[2,3,4,5]
print(f"Karesiz sayılar: {deneme_kare_list}")
print(f"Sonuçlar:{kare_al(deneme_kare_list)}")

print("-"*50)


#14.   dışarıdan alınan bir not listesinin her bir değerinin yüzde 70'ını
      # hesaplayınız. Eğer bu hesaplamanın sonucu 30'dan küçükse "Kaldı", büyükse
      # "Geçti" yazacak ve bunu da bir listeye ekleyecek. Listeyi geri döndürün

 
def not_list(y): 
	Not_list=[]
	for i in y:
		i=i*0.70
		if i<30:
			Not_list.append("Kaldı")
		else:
			Not_list.append("Geçti")
	return Not_list

deneme_notlar=[67,89,65,43,57,98]
print(f"Notlar: {deneme_notlar}")
print(f"Sonuçlar: {not_list(deneme_notlar)}")










