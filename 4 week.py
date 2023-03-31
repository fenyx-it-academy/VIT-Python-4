#1.Sorunun Cevabı
#------------------
liste=[1,2,3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]
liste2=set(liste)       #tekrarlanan elemanları set metodu ile başka kaldırıyoruz


for i in liste2:      #liste 2 de olan elemanların liste 1 de olanlar ile karşılaştırıyorum eğer aynıları varsa siliyoruz 
    if i in liste:    
        liste.remove(i)
    
print("Liste içinde tekrarlanan elemanlar:  ",set(liste))    #yine set metodu ile tekrarlanan elemanları silerek ekrana yazırıyoruz.
        
#2.Sorunun Cevabı
#------------------
menu={"CORBA":10,               #Yemeklerin ve fiyatların olduğu sözlük tanımladım
      "KEBAP":20,
      "TAVUK":15,
      "TATLI":10}
print("""-----MENU------""")     #Yemek isimlerinin alt alta görünmesini sağlamak için for döngüsü ile alt alta yazdırdım
for x,y in menu.items():
    print(x,"=",y,"€")
siparis={}          #siparişlerin eklenemsini için yeni boş bir sözlük oluşturdum
tutar=0                #toplam tutarı hesaplamak için değişken tanımladım
while True:       #kullanıcıdan sürekli bilgi istemesi için while true ile sonsuz döngü kurdum
    sno=input("Siparişinizi giriniz, Sipairişi Tamamlamak için 'q' tuşuna basınız:    ").upper()  
    if  sno=="Q":   #siparişi tamamlamak için q tuşuna basıp döngüyü bitirdim
        break
    elif sno not in menu:   #eger girilen deger menüde yoksa menüden seçmesini sağlıyoruz
        print("Lütfen Geçerli Bir Seçim Yapınız")
        continue
    siparis[sno]=menu[sno] #kullanıcıdan gelen  yemek ismini ve fiyatını sipariş isimli sözlüğe ekledim       
print("""----SİPARİŞİNİZ------""")    
for x,y in siparis.items():       #Yine müşterinin siparişlerini alt alta yazdırmak ve toplam tutarı hesaplamak için for döngüsü kullandım
    print(x,"=",y,"€")
    tutar+=y
print("Toplam Tutar: ",tutar," €")

# Bonus sorunun cevabı

mors= {' ':' ','A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

giris=input("Metin girmek için'1' Mors alfabesi girmek için 2 ")
if giris=='1':
    metin=input("Lütfen bir metin giriniz").upper()
    yenimetin=""
    for i in metin:
        yenimetin=yenimetin+mors[i]

    print(yenimetin)
elif giris=='2':
    metin=input("Mors Alfabesi Giriniz").upper()
    yenimetin=""
    morsters={value: key for key, value in mors.items()}
  
    for i in metin:
        yenimetin=yenimetin+morsters[i]
    print(yenimetin)
    
