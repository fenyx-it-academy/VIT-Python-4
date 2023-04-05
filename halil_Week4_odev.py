#Soru1

liste = [1, 2, 3, 41, 2, 2, 4, 4, 5, 6, 76, 34, 1, 2]

tekrarlanan = set()
listem = {}
for i in liste:
    if liste.count(i) > 1:
        tekrarlanan.add(i)
        listem[i] = liste.count(i)

for i, j in listem.items():
    print(i, "sayisi", j, "kere")

print(
    f"tekrar etmistir.\nTekrar eden sayilarin listesi:\t{list(listem.keys())}")

#################################
#Soru2

menu = {'kebap': 20, 'salata': 13, 'ayran': 4, 'kola': 6, 'tatli': 14,
        }


print(
    """ABC Lokantasina Hos Geldiniz

1--Kebap  :  20 $
2--Salata :  13 $
3--Ayran  :  4  $
4--Kola   :  6  $
5--Tatli  :  14 $

Cikmak icin "q" giriniz""")
siparis_ve_sayisi = {}
while True:
    musteri = input("Lutfen Siparisinizi giriniz : ")
    if musteri == "1":
        musteri = "kebap"

    elif musteri == "2":
        musteri = "salata"

    elif musteri == "3":
        musteri = "ayran"

    elif musteri == "4":
        musteri = "kola"

    elif musteri == "5":
        musteri = "tatli"

    if musteri in siparis_ve_sayisi:
        siparis_ve_sayisi[musteri] += 1
    elif musteri not in siparis_ve_sayisi and musteri in menu:
        siparis_ve_sayisi[musteri] = 1

    if musteri == "q":
        break
    elif musteri not in menu:
        pass


total = 0

for i, j in menu.items():
    for k in siparis_ve_sayisi.keys():
        if k == i:
            total += j


print("""
        
*************____________SIPARISLER____________*************""")
for i, j in siparis_ve_sayisi.items():
    print(f"{j} adet\t {i}")
print("Toplam ucret : ", total, "dolar")


#################
#Bonus

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

print("""
Morstan Latin alfabesine cevirmek icin    1   
Yazidan Mors alfabesine cevirmek icin     2""")

secim = int(input("Secim yapiniz  1^2 "))
while True:
    if secim == 1:
        morse_to_name = input("Mors giriniz")
        morse_to_name = morse_to_name.split()
        result_mors = []

        for i in morse_to_name:
            for j, k in MORSE_CODE_DICT.items():
                if i == k:
                    result_mors.append(j)

        print("".join(result_mors))
        break
    elif secim == 2:

        name_to_morse = input("Isim giriniz: ").upper()
        result_name = []
        for k in name_to_morse:
            for i, j in MORSE_CODE_DICT.items():
                if k == i:
                    result_name.append(j)
        print(*result_name)
        break
    else:
        print("Hatali giris yaptiniz tekrar deneyiniz!")
