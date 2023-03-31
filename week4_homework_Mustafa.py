# VIT-Python-4
# Soru-1
# Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan elemanlari bulan bir Python programı yazın. Bu soruyu cozerken Python kumelerini kullanmaya calisin.

# Ornek Input:
# 1 2 3 4 12 45 1 2 54 65 77 8 1 2

# Ornek Output:
# Tekrarlayan öğeler: {1, 2}

liste=  [1 ,2 ,3 ,4 ,12, 45, 1 ,2 ,54, 65 ,77, 8, 1 ,2,54, 65 ,77]
   
kumem=set(liste)
for i in kumem:
    liste.remove(i)
    
print(set(liste))


#=====================================================


#  Soru-2
# Bir restoranın menüsünü Python sözlükleri kullanarak oluşturun ve kullanıcının yemekler sipariş etmesine izin verin.

# Aşağıdaki adımları izleyebilirsiniz:

# Restoranın menüsünü bir Python sözlüğü olarak oluşturun. Her yemek bir anahtar kelime, fiyatı ise değer olarak tanımlanabilir.
# Kullanıcının menüyü görmesi için menüyü ekrana yazdırın.
# Kullanıcıdan yemekler sipariş etmesini isteyin. Kullanıcı, bir yemek adı veya numarası girebilir.
# Kullanıcının seçtiği yemekleri bir sözlükte saklayın.
# Kullanıcının siparişlerini ekrana yazdırın ve toplam fiyatı hesaplayın.


menu={'CORBA': 1, 'PILAV': 3, 'SALATA': 5, 'TOST':7, 'PATATES': 9,  'AYRAN': 11}
print("Menumuz:")

for i,j in menu.items():
    print(i,"____",j)

order = {'CORBA': 0, 'PILAV': 0, 'SALATA': 0, 'TOST': 0, 'PATATES': 0, 'AYRAN': 0}

while True:
    urun = input("Sipariş etmek istediğiniz ürünün adını yazın (bitirmek için Q yazın): ").upper()
    if urun == 'Q':
        break
    adet = input("Sipariş etmek istediğiniz {} adetini yazın: ".format(urun)).upper()
    order[urun] = int(adet)
    print("Siparişiniz kaydedildi: {} adet {}".format(adet, urun))
total=0

print("Siparişleriniz:")
for urun, adet in order.items():
    if adet > 0:
        print("{}: {} adet  {} lira ".format(urun, adet,adet*menu[urun]))
        total+=adet*menu[urun]

print("Toplam Hesap: {} Lira, Afiyet olsun ".format(total))


#=====================================================


# BONUS
# Kullanıcının bir metin girmesini ve ardından bu metni Mors alfabesi koduna dönüştürüp yazdırmasını veya aynı şekilde Mors alfabesi kodunu alıp metne dönüştürmesini saglayan bir program yazin. Asagidaki mors alfabesi sozlugunu kullanabilirsiniz.

# MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# Ornek Input:
# Metin girin: Fenyx IT Academy

# Ornek Output:
# Mors kodu:  ..-. . -. -.-- -..-  .. -  .- -.-. .- -.. . -- -.-- 
# Mors kodu:  ..-. . -. -.-- -..-  .. -  .- -.-. .- -.. . -- -.--

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


secim=input("""Metni mors koduna çevirmek için: (1) 
            Mors kodunu metne çevirmek için (2) 
            çıkış için (Q)'ya basınız): 
            """).upper()

if secim==1:
    text = int(input("Dönüştür istediğiniz metni yazın (bitirmek için Q yazın): ").upper())
    donusum=""
    for i in text:
        if i not in MORSE_CODE_DICT.keys():
            donusum+=" "
        else:
            donusum+=MORSE_CODE_DICT[i]+" "
    print("'{}' metninin Mors alfabesi koduna dönüşümü: '{}' ".format(text,donusum))
    
    
elif secim==2:
    text = int(input("Dönüştür istediğiniz kodu yazın (bitirmek için Q yazın): ").upper())
    donusum=""
    
    
    pass

elif secim=="Q":
    print("Hoşça kalın")
    
else:
    print("Hatalı giriş yaptınız")
