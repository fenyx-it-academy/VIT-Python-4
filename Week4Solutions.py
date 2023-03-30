# VIT-Python-4

## Soru-1

#Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan elemanlari bulan bir Python programi yazin. Bu soruyu cozerken Python kumelerini kullanmaya calisin.

### Ornek Input:
#`1 2 3 4 12 45 1 2 54 65 77 8 1 2`

### Ornek Output:
#`Tekrarlayan öğeler: {1, 2}`


liste=[1,2,3,4,12,45,1,2,54,65,77,8,1,2]

# Tekrarlayan elemanlari bulmak için küme oluşturulur
kume = set()

# Elemanlar kontrol edilir ve tekrar edenler kümeye eklenir
for eleman in liste:
    if liste.count(eleman) > 1:
        kume.add(eleman)

# Sonuç ekrana yazdirilir
print("Tekrarlayan öğeler:", kume)




# # Soru-2
# Bir restoranin menüsünü Python sözlükleri kullanarak oluşturun ve kullanicinin yemekler sipariş etmesine izin verin.

# Aşağidaki adimlari izleyebilirsiniz:
# *  Restoranin menüsünü bir Python sözlüğü olarak oluşturun. Her yemek bir anahtar kelime, fiyati ise değer olarak tanimlanabilir.
# *  Kullanicinin menüyü görmesi için menüyü ekrana yazdirin.
# *  Kullanicidan yemekler sipariş etmesini isteyin. Kullanici, bir yemek adi veya numarasi girebilir.
# *  Kullanicinin seçtiği yemekleri bir sözlükte saklayin.
# *  Kullanicinin siparişlerini ekrana yazdirin ve toplam fiyati hesaplayin.


# restoran menüsü sözlüğü
menu = {
    "hamburger": 25,
    "patates kizartmasi": 12,
    "sandviç": 15,
    "pizza": 30,
    "tavuk şiş": 20,
    "lahmacun": 18
}

# menüyü yazdirma
print("Menü:")
for yemek, fiyat in menu.items():
    print(yemek, "-", fiyat, "TL")

# kullanici siparişi almak
siparisler = {}
while True:
    secim = input("Sipariş vermek için bir yemek adi girin (Çikmak için q): ")
    if secim.lower() == "q":
        break
    elif secim in menu:
        if secim in siparisler:
            siparisler[secim] += 1
        else:
            siparisler[secim] = 1
    else:
        print("Geçersiz seçim.")

# siparişleri ekrana yazdirma
print("Siparişler:")
toplam_fiyat = 0
for yemek, adet in siparisler.items():
    fiyat = menu[yemek]
    toplam_fiyat += fiyat * adet
    print(yemek, "-", adet, "adet -", fiyat * adet, "TL")
print("Toplam fiyat:", toplam_fiyat, "TL")


# # ## BONUS

# Kullanicinin bir metin girmesini ve ardindan bu metni Mors alfabesi koduna dönüştürüp yazdirmasini veya ayni şekilde Mors alfabesi kodunu alip metne dönüştürmesini saglayan bir program yazin. Asagidaki mors alfabesi sozlugunu kullanabilirsiniz.

# `MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
#                    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
#                    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
#                    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
#                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
#                    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
#                    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#                    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
#                    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
#                    '(': '-.--.', ')': '-.--.-'}`
                   
# ### Ornek Input:
# Metin girin: `Fenyx IT Academy`

# ### Ornek Output:
# `Mors kodu:  ..-. . -. -.-- -..-  .. -  .- -.-. .- -.. . -- -.-- ` 
                 
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                   '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

text = input("Metin girin: ")
morse_code = ""
for char in text.upper():
    if char != " ":
        morse_code += MORSE_CODE_DICT[char] + " "
    else:
        morse_code += " "
print("Mors kodu: ", morse_code)