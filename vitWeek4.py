# # Soru-1

# liste = [1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]

# # set ile liste icinde olan tekrarli ifadeler ortadan kalkmis olur.
# tekrarsizListe = []  # buraya tekrar edilmeyen yeni bir liste olusturaagiz
# tekrarEdenlerListe = []  # burada ise tekrar edilenleri toplayacagiz

# for i in liste:
#     if i not in tekrarsizListe:
#         tekrarsizListe.append(i)
#     else:
#         tekrarEdenlerListe.append(i)
# print(tekrarsizListe)

# # set ile tam tekrarsiz liste olusturmus olacagiz
# sonucListe = set(tekrarEdenlerListe)
# print(sonucListe)


# Soru-2
# restoran menusunu dict olarak hazirliyoruz
# menu = {
#     'MERCIMEK': 11,
#     'TARHANA': 12,
#     'SALATA': 7,
#     'MEZE': 6,
#     'KEBAP': 53,
#     'DURUM': 36,
#     'KADAYIF': 21,
#     'SUTLAC': 19
# }

# print('FENXY 😋 LOKANTASINA HOS GELDINIZ\n')

# # bos dict olusturup inputtan gelen siparisleri onceden olusturdugumuz dict icindeki menu ile...
# # eslestirip buraya musterinin menusunu olusturmus oluyoruz.

# siparisler = {}

# # while ile surekli dongu olusturuyoruz.
# while True:
#     # count ile menu numaralari veriyoruz.
#     count = 1
#     for key, value in menu.items():
#         # dict icindeki menuye mudahale ederek listeyi daha okunakli yaptik
#         print(count, '. Menu:', key, ', Fiyati:', value, '€')
#         count += 1
#     # input ile kullanicidan veri aliyoruz
#     menuSecim = input(
#         'Lutfen listeden yemek seciniz: (Siparsiniz bittiginde "x" ile cikabilirsiniz)').upper()

#     # print(siparisler)
#     menuListe = siparisler.keys()
#     # if ile gelen verinin dogrulanmasi ve liste icine yazilmasi islemini yapiyoruz.
#     if menuSecim == 'x':
#         break  # kullanici cikmak isterse x e basabilir
#     # kullanici secimi olusturdugumuz dict de varmi kontrol ediyoruz
#     elif menuSecim in menu:
#         ###
#         siparisler[menuSecim] = menu.get(menuSecim)
#     else:
#         print('Hatali secim yaptiniz. Lutfen tekrar deneyiniz')

#     # secilen menunun fiyatlarini values lara ulasarak hesaplayabiliriz
#     # total ve menuliste ile for icindeki verileri toplanmasini sagliyoruz.
#     total = 0
#     menuListe = []
#     for i, j in siparisler.items():
#         total += j
#         menuListe.append(i)
#         # print icinde kullaniciya guzel bir bildirim gostermis oluyoruz. * isareti ile listeyi parantesiz yazdirabiliyoruz
#     print('Sectiginiz menu olan:', *menuListe, 'icin toplam Fiyat:',
#           total, '€ olarak hesaplanmistir')

# # BIR MENUDEN 2 KEZ SECTIRMIYOR


#  Soru - 3
# Kullanıcının bir metin girmesini ve ardından bu metni Mors alfabesi koduna
# dönüştürüp yazdırmasını veya aynı şekilde Mors alfabesi kodunu alıp metne
# dönüştürmesini saglayan bir program yazin.

# MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
#                    'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# kelime = input('Bir metin giriniz:').upper()
# print(kelime)

# veriListe = []
# for i in kelime:
#     veriListe.append(i)
# print(veriListe)
# liste = dict([veriListe], MORSE_CODE_DICT.values())
# print(liste)
# print(MORSE_CODE_DICT.values())
