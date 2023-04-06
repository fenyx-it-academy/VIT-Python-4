cevap1
#Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan elemanlari bulan bir Python programı yazın.
#Bu soruyu cozerken Python kumelerini kullanmaya calisin.
a=[1 ,2,3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]
tekrarlayan_sayi=set()
for i in a:
  if a.count(i)>1:
    tekrarlayan_sayi.add(i)
print("Listemiz:",a,"\nTekrarlayan sayilar:",tekrarlayan_sayi)
  
cevap2
#Bir restoranın menüsünü Python sözlükleri kullanarak oluşturun 
#Her yemek bir anahtar kelime, fiyatı ise değer olarak tanımlanabilir.
menu={
    "CORBA"   :5 ,
    "KEBAP"       : 15,
    "DONER"       : 8,
    "ISKENDER"    :12,
    "TAVUK"        :7,
    "SALATA"      :5,
    "BAKLAVA"      :30,
    "KUNEFE"       :20,}
print("""***** MENÜ *****
      1--CORBA
      2--KEBAP
      3--DONER
      4--ISKENDER
      5--TAVUK
      6--SALATA
      7--BAKLAVA
      8--KUNEFE""")

numara1={'1':'CORBA','2':'KEBAP','3':'DONER','4':'ISKENDER','5':'TAVUK','6':'SALATA','7':'BAKLAVA','8':'KUNEFE'}
numara2={'CORBA':'1','KEBAP':'2','DONER':'3','ISKENDER':'4','TAVUK':'5','SALATA':'6','BAKLAVA':'7','KUNEFE':'8'}
secilenler={}
#Kullanıcıdan yemek siparişi istiyoruz. Kullanıcı, bir yemek adı veya numarası giriyor
while True:
    siparis=input("Lutfen siparisinizin numarasini yada adini yazin: ").upper()
    
    if siparis in numara1.keys():
        secilenler[numara1[siparis]]=menu[numara1[siparis]]
    elif siparis in numara2.keys():
        secilenler[siparis]=menu[siparis]
    elif siparis not in numara1 or siparis not in numara2:
        print("Maalesef siparisiniz menude bulunmamaktadir.")
        pass
        
    devam = input("Başka siparişiniz var mı? (E/H): ").upper()
    if devam == "E":
        continue
    else:
        print("siparisleriniz:",secilenler)
        print("toplam fiyat:",sum(secilenler.values()))
        break
    
    cevap3
    #Kullanıcının bir metin girmesini ve ardından bu metni Mors alfabesi koduna dönüştürüp yazdırmasını 
# veya aynı şekilde Mors alfabesi kodunu alıp metne dönüştürmesini saglayan bir program yazin. 
# Asagidaki mors alfabesi sozlugunu kullanabilirsiniz.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
menu=""" Mors Kodu Olusturucu/Okuyucu:
     1.Morsa cevir
     2.Morstan cevir
     3.Cikis """
while True:
    print(menu)
    secim=int(input("Bir Secim(numara) Giriniz:"))
    if secim==3:
        break
    elif secim==1:
        kullanici=input("Metni giriniz:").upper()
        morsmetni=[]
        for i in kullanici:
            for j,k in MORSE_CODE_DICT.items():
                if i==j :
                    a=k
            morsmetni.append(a)


        print(*morsmetni)
    else :   
        
        kullanici=input("Cevrilmesini istediginiz kodu giriniz:")
        baslangic,indis=0,0
        i=0
        s=[]
        morstanc=[]
        while indis<int(len(kullanici))-1:
            indis+=1
            if kullanici[indis]==" ":
                morstanc.append(kullanici[baslangic:indis])
                baslangic=indis+1
                indis+=1
                     
                for x,z in MORSE_CODE_DICT.items():
                   
                   if morstanc[i]==z:
                        b=x
                        s.append(b)
                i+=1
            
        print(*s,sep="")
    
