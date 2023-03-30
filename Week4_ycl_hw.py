# Soru-1
# Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan elemanlari bulan 
# bir Python programı yazın. Bu soruyu cozerken Python kumelerini kullanmaya calisin.

# Ornek Input:
# 1 2 3 4 12 45 1 2 54 65 77 8 1 2

# Ornek Output:
# Tekrarlayan öğeler: {1, 2}

liste=[1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]

kume=set(liste)   # Listeyi set ederek her elementin bir kere bulunacagi
                  # bir kume olusturdum.


for i in kume:             # For dongusuyle kumenin her bir elementinin listeden  
    if i in liste:         # cikartilmasini amacladim ki bu sayede tekrarlayanlar
        liste.remove(i)    # listede halen en az 1 kere kalacaklar.
        
print(set(liste))          # Tekrar listeyi set ederek tekrarlayan elementleri
                           # kumeye cevirerek ekrana yazdirdim.
                           
################################################################################

# Soru-2
# Bir restoranın menüsünü Python sözlükleri kullanarak oluşturun ve 
# kullanıcının yemekler sipariş etmesine izin verin.
# Aşağıdaki adımları izleyebilirsiniz:
# Restoranın menüsünü bir Python sözlüğü olarak oluşturun. 
# Her yemek bir anahtar kelime, fiyatı ise değer olarak tanımlanabilir.
# Kullanıcının menüyü görmesi için menüyü ekrana yazdırın.
# Kullanıcıdan yemekler sipariş etmesini isteyin. Kullanıcı, 
# bir yemek adı veya numarası girebilir.
# Kullanıcının seçtiği yemekleri bir sözlükte saklayın.
# Kullanıcının siparişlerini ekrana yazdırın ve toplam fiyatı hesaplayın.


menu = {"ezo": 5, "tavuksuyu": 5, "coban": 3, "american": 5,
      "iskender": 15, "alinazik": 13,"kunefe": 7, "katmer": 7}

for i,j in menu.items():
    print(i,"=",j)
    
order = {}
toplam=0    
while True: 
        user = input("Lutfen seciminizi girin, cikmak icin q ya basin: ").lower()
   
        if user == "q":
            print("Iyi gunler...") 
            break
        elif user in menu.keys():
            order[user] = menu[user]
            toplam += menu[user]
        else:
            print("Tekrar deneyin")
            continue    
print("Siparisiniz asagidaki gibidir: ", *order.items(), sep="\n")
print("Toplam: ", toplam, "euro")        
        

# Kullanıcının bir metin girmesini ve ardından bu metni Mors alfabesi 
# koduna dönüştürüp yazdırmasını veya aynı şekilde Mors alfabesi kodunu alıp 
# metne dönüştürmesini saglayan bir program yazin. 
# Asagidaki mors alfabesi sozlugunu kullanabilirsiniz.

# Ornek Input:
# Metin girin: Fenyx IT Academy

# Ornek Output:
# Mors kodu: ..-. . -. -.-- -..-  .. -  .- -.-. .- -.. . -- -.--

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

text = input("Cevirmek istediginiz teksti giriniz: ").upper()

text_morse = ""

for i in text:
        
        if i in MORSE_CODE_DICT.keys():
            text_morse += MORSE_CODE_DICT[i] 
        else:
            text_morse += " "   
print(text_morse)   
                                   