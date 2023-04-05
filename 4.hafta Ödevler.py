#S1

#Rastgele sayilardan olusan bir liste olusturuldu
l = [1, 5, 4, 12, 45, 1, 2, 54, 65, 77, 8, 55, 2, 72, 12]

# "uniek" ve "repeat" isimli iki set olusturuldu
uniek = set()
repeat = set()

# for dongusu ile listenin her bir elemani isleme alindi ve 
# tekrar edenler(repeat) ve etmeyenler(uniek) olarak iki farkli kumeye ayrildi.
for i in l:
    if i in uniek:
        repeat.add(i)
    else:
        uniek.add(i)

#Bu iki kumenin ciktisi ekrana yazildi.
print(uniek,repeat, sep="\n")


#S2

#menu isimli bir dictionary olusturuldu.
#key degerleri yemeklerden, values degerleri fiyatlardan olusturuldu.
menu = {"adana kebap" : [15,"Euro"],
        "urfa kebap" : [15,"Euro"],
        "pilav ustu et doner":  [20,"Euro"],
        "mercimek corba" : [5, "Euro"],
        "patates kizartma" : [10, "Euro"],
        "baklava" : [8, "Euro"],
        "sutlac" : [6, "Euro"],
        "kadayif" : [7, "Euro"],
        "kola" : [3, "Euro"],
        "fanta" : [3, "Euro"],
        "ayran" : [2, "Euro"],
        "su" : [1, "Euro"],
        "cay" : [1,"Euro"]}

#Yemekler ve fiyatlar kullanicinin secim yapmasi icin ekrana basildi.
for k,v in menu.items():
    print(k, "=", v)

#Girdilerin tamamini tutmak icin yeni bir sozluk olusturuldu.
hesap =  {}

#Kullanicidan siparisleri istendi ve sozluge(hesap) eklendi.
#Siparisi tamamlamak icin cikis olusturuldu.
while  True:
    siparis = input("Lutfen bir yemek adi yazin.(Cikmak icin 'q' basin.):".lower())
    if siparis == "q":
        break


    for s,p in  menu.items():         
        if siparis == s:
            hesap[s] = {p[0]}
        elif siparis != s:
            print("Lutfen menuden bir yemek secin!")
            break
            


#Siparis tutarinin hesaplanmasi icin 
# keys ve values degerlerini tutacak iki farkli liste olusturuldu.
fyt = []
sprs = []
for y,f in hesap.items():
    fyt.append(f)
    sprs.append(y)

#Fiyat hesaplanmasi yapildi
fiyat = [list(x) for x in fyt]
tutar = 0
for t in fiyat:
    tutar += t[0]

#Verilen yemek siparisi ve toplam tutari ekrana basildi.
print("Sirasisleriniz:",sprs)
print("Tutar:",tutar," ", "Euro")


#BONUS

# Latin harflerine ve sembollere karsilik gelen mors alfabesi olusturuldu.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                   '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

#Alternatif olmasi icin mors alfabesine karsilik gelen 
# latin harfleri ve sembollerden sozluk olusturuldu.
# LATIN_HARF = {} 
# for latin,mors in MORSE_CODE_DICT.items():
    # LATIN_HARF[mors] = latin

#Kullanicidan bir girdi istendi
girdi = input("Lutfen adinizi latin harfleri ile yazin:")

#Eslesmelerin hatasiz olmasi icin aldigimiz girdinin her bir ogesi 
# string tipinde buyuk harf olarak (eger harf ise) bir listeye eklendi.
a = list(girdi.upper())



# Eslesen harfleri kaydetmek icin "cikti" isimli bir dictionary olusturuldu.
cikti = {}


# Listede bulunan her bir veri sozlukte arandi. 
# Eslesen verilerin mors alfabesindeki karsiliklari (values) "cikti" sozlugune eklendi.
for x in a:
    for l,m in MORSE_CODE_DICT.items():
        if l == x:
            cikti[l] = m

#yeni sozlukte bulunan degerler liste haline getirildi.
kod = list(cikti.values())

#Sozlukte bulunan veriler 
# tek bir string degeri olusturacak sekilde bir veri yapisina donusturuldu.
b = ""
for z in kod:
    b += " " + z


#Verinin son hali cikti olarak ekrana verildi.
print("Mors kodu:",b)
