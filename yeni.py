
# def ile fonksiyon tanımlanır

def ilkFonsiyon():
    print("bu bizim ilk fonksiyonumuz")

ilkFonsiyon()
print(ilkFonsiyon())

# return ifadesi kullanan fonksiyon yani geriye değer döndüren

def ilkFonksiyon():
    print(8+5)

def ikinciFonksiyon():
    return 8+5

print(f"1. fonksiyonun çıktısı = {ilkFonksiyon()}")
print(f"2. fonksiyonun çıktısı = {ikinciFonksiyon()}")

# fonksiyon çağırma 2. yol   değişkene atayarak çağırma

deger2 = ikinciFonksiyon()

print(f"fonlsiyonun geri dönüş değeri = {deger2}")
print(f"fonksiyonun geri dönüş tipi = {type(ikinciFonksiyon())}")

# çıkan sonucu 10la çarptı
print(deger2*10)

# liste tipine göre geri dönüş değeri veren bir fonksiyon yazalım

print("-"*50)
def ucuncuFoksiyon():
    return ["Furkan","Makü",15,96,105,True,False,85,456]

print(ucuncuFoksiyon())

deneme3 = ucuncuFoksiyon()
print(deneme3[3])

# fonksiyonun döndürdüğü değer, fonksiyonun çağırılmasıyla ya da
# fonksiyonun çalıştırılmasıyla elde edilir 
# fonksiyon_adı() => fonksiyonu çağırır ya da çalıştırır
# sadece fonksiyonun adını yazarsak onun bellekteki adresini çağırmış oluruz

print("-"*50)
print(f"fonksiyonun çalıştırılması = {ucuncuFoksiyon()}")
print(f"fonksiyonun bellekteki adresine erişim = {ucuncuFoksiyon()}")

#0 dan 12 ye kadar 12 dahil olmayacak tek sayıları yazdıran fonksiyon

def teksayi():
    for i in range(0,12):
        if i%2!=0:
            print(i)

teksayi()    

# 0 la 50 arasında hem 3e hem 5e bölünenler

def bolunen():
    for a in range(0,50):
        if a%3==0 and a%5==0:
            print(a)

bolunen()

# aynısı hocanın yaptığı
            
def katonbes():
    for i in range(0,50,15):
        if i !=0:
            print(i)
# 7ye tam bölünenler 1.yol
def kat7():
    for i in range(1,501):
        if i%7==0:
            print(i)

kat7()
#2.yol

for i in range(0,501,7):
    print(i)

 #1 ile 450 arasında hem 5e hem de 8'e bölünen sayıları yazdıran fonksiyon

def beşsekiz():
    for a in range(1,450):
        if a%5==0 and  a%8==0:
            print(a) 

beşsekiz() 

#1 ile 300 arasında 5'e tam bölünen ama 2'ye tam bölünmeyen sayıları yazan fonksiyon  i%2!=0 şeklinde de olanilir

def beşiki():
    for e in range (1,300):
     if e%5==0 and e%2==1:
        print(e)

beşiki()        

#parametre olarak verilen not listesinin her bir değerinin yüzde kırkını alan
#ve bu değerin 30dan küçük olması durumunda kendi oluşturduğu listeye                 ÖNEMLİ!!!!!!!!!!!!!!
#kaldı yazan aksi durumda geçti yazan fonksiyon

def vizenotal(rastgele):
    bos_liste = []

    for deger in rastgele:
        yeni_deger = deger * 0.4
        if yeni_deger<30:
            bos_liste.append("KALDI")
        else:
            bos_liste.append("GEÇTİ")
    return bos_liste

my_not_list = [54,96,31,21,80,98,45,23]

print(f"orijinal not listesi = {my_not_list}")
print(vizenotal(my_not_list))


# final için yani %60 

# üstteki fonksiyonun aynısını yazdık çözxüm olarak sadece 0.4
#yerine 0.6 yazdık ve tabikide verdiğimiz not listesini değiştirdik.

def donemNotuHesapla(vize,final):
    donem_liste = []

    for deger in range (len(vize)):
        my_not_vize = vize [deger]
        my_not_final = final [deger]

        yeni_vize = my_not_vize * 0.4
        yeni_final = my_not_final * 0.6

        my_last_note= yeni_vize + yeni_final

        if my_last_note < 50:
            donem_liste.append("kaldı")
        else:
            donem_liste.append("geçti")
    return donem_liste

# yukarıdaki işlemi yerine getiren 3 ayrı fonksiyon

#def vizeHesapla (vize_liste):
   # vize_bos = []
   # for i in vize_liste:
        #deger = i*0.4
        #vize_bos.append(deger)
   # return vize_bos

#def finalHesapla (final_liste)


soz="Burdur Mehmet Akif Ersoy Üniversitesi"
# yukarıdaki ifade de yer alan e harflerini a olarak değiştiren fonksiyon

def harf(metin):
    yeni_metin = []

    for i in metin:
        if i == "e":
            i ="a"
            yeni_metin += i
        else:
            yeni_metin += i
    return yeni_metin
print(f"orijinal metin = {soz}")
print(harf(soz))

# 2.yol

def harfDegis2(metin):
    return metin.replace("e","a")

print(harfDegis2(soz))

#bazı kelimelerin 





def siralama(kelime_liste):
    bos_liste = []

    for i in kelime_liste:
        if i [: :] == i [ :: -1]:
            bos_liste.append(i)

    return bos_liste

my_list = ["kabak","ekmek", "ses", "radar", "dosya","makü"]

print(siralama(my_list))

# 1 den 10 a kadar olan sayıların küpünü alıp bir listeye ekleyen
#ve bu listeyi döndüren fonksiyonu yazınız


def sayılarınküpü():
    bos_liste = []

    sayılarınküpü = [i**3 for i in range(1,11)]
    return sayılarınküpü

liste = sayılarınküpü()
print(liste)



# 1 den 500 e kadar 3 7 ve 8 ile tam bölünen 

def sayi():
    for a in range(1,501):
        if a%3==0 and a%7==0 and a%8==0:
            print(a) 

sayi() 
         

# c = "merhaba"  hata türleri

#try: 
 #   print(c)

#except Exception as e:
 #   print(e)

#print("her halükarda çalışan kod")


#  2) assert (AssertionError)
# python da daha çok versiyon uyumsuzluğunu kontrol etmek için


#deger = input("lüftfn sayı giriniz:")

#assert type(deger)==int, "girdiğiniz değeri int e dönüştürün"
# if type(deger)==int aynı şey üsttekiyle
#51
# print(f"girdiğiniz sayı: = {deger}")

# girilen sayı pozitif ise kod çalışsın ve girmiş olduğunuz sayıyı yazarak sayı pozitiftir desin 
# negatifse uyarsın assert ile yapın 

#deger2 = input("sayı giriniz:")
#deger2 = int(deger2)
#assert deger2>0, "pozitif bir sayı girin"
#print(f"girdiğiniz sayı {deger2} pozitiftir")

# kullanıcıdan alınan sayı tek ise "girmiş olduğunuz sayı tektir."
# çift ise assert hatası verecek ve "lütfen tek sayı giriniz" mesajı yazacak.

#deger3 = input("sayı gir")
#deger3 = int(deger3)
#assert deger3%2==1, f"tek bir sayı girin"
#print(f"girdiğiniz değer {deger3} sayısı tek sayıdır")

# Dışarıdan girilen not değeri, 50 den küçükse assert ile " KALDINIZ" yazacak
# büyükse, "TEBRİKLER!" yazacak.

#deger4 = input("not gir")
#deger4 =int(deger4)
#assert deger4>50, "KALDIN ZA"
#print(f"Notunuz = {deger4} tebrikler geçtiniz")



#dışarıdan girilen kullanıcı adı bilgisi kendi isminiz ise
#"TEBRİKLER GİRİŞ YAPILDI" yazıcak. kullanıcı adı farklı ise 
# assert hatası verilecek ve "lütfen doğru kullanıcı adını giriniz" yazacak

#deger5 = input("isim girin")

#assert deger5== "ali","bu sen değilsin"
#print("tebrikler giriş yapıldı")

# girilen kullanıcı adı sizin adınız ve şifresi de öğrenci numaranızın
# son 4 hanesi ise " başarılı bir şekilde giriş yaptınız" yazacak
# değilse, assertionerror verecek "kullanıcı adı ya da parola hatalı" yazacak

#kullanici_adi = input("kullanıcı adınızı giriniz")
#sifre = input("şifrenizi giriniz.")

#assert kullanici_adi == "aslı" and int(sifre) == 1759, "kullanıcı adı ve parola yanlış"

#print("giriş yapıldı")


# Dışarıdan girilen vize ve final notlarının ortalamasını alan
# ortalama 50 den büyükse "tebrikler geçtiniz" yazan
# ortalama 50 den küçükse assertionerror ile " maalesef kaldınız" yazan kod.


vize_notu = input("vize notunuzu girin")
final_notu = input("final notunuzu girin")

assert (int(vize_notu) + int(final_notu))/2 > 50, "maalesef kaldınız"
print("tebrikler geçtiniz")







    
        
    

