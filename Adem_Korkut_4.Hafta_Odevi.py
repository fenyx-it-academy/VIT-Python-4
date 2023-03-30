#        4. Hafta Odevi - Sozlukler -

#  1. Soru - Tekrar Eden Eleman -

a= [2,4,5,1,7,8,2,9,5,1,0,6,5]
b= set()
for i in a:
    if a.count(i)> 1 : # i'nin a listesi icerisinde kac kez kullanidigini tespit etmek icin, eger birden fazla anlamina gelen (i)>1 ifadesini kullandim.
       b.add(i) # Yukaridaki sart saglandiginda tekrar eden elemani b'ye gondermesi istedim.
print(b)

#  2. Soru - Menu, Hesap -

menu= ("CORBALAR: \n  Mercimek:  5.00 Euro \n  Yayla: 5.00 Euro \n  Ezo Gelin: 5.00 Euro \n\nANA YEMEKLER: \n  Beyti: 7.50 Euro \n  Kuru Fasulye: 6.50 Euro \n  Patlican Musakka: 6.50 Euro \n  Portakalli Pekin Ordegi: 20.00 Euro \n\nSALATALAR: \n  Coban Salata: 5.00 Euro \n  Mevsim Salata: 6.00 Euro \n  Tonbalikli Salata: 8.00 Euro \n  Sogan Sogus: 4.00 Euro \n\nTATLILAR: \n  Baklava:8.50 \n  Kadayif: 7.50 \n  Tulumba: 6.00 Euro \n  Sutlac: 7.00 Euro")
print(menu) #Musterinin menuyu duzgun bir sekilde gormesi sagladim.
siparis_listesi= [] # Musteriden input olarak alacagimiz siparisi bu listede topladim.
menu1= {"Mercimek": 5, "Yayla": 5,"Ezo Gelin": 5, "Beyti": 12,"Kuru Fasulye": 6,"Patlican Musakka": 8,"Portakalli Pekin Ordegi": 20,
    "Coban Salata": 4,"Mevsim Salata": 6,"Tonbalikli Salata": 8,"Sogan Sogus": 4.00,
    "Baklava": 6.50,"Kadayif": 6.00,"Tulumba": 3.00,"Sutlac": 4.00} 
while True:
    musteri= input("Siparis etmek istediginiz urunun tam adini yaziniz:") # Musteri siparis vermeyi kendisi durdurana kadar dongunun devam etmesi icin While True dongusunu kullandim.
    siparis_listesi.append(musteri) #Musteriden gelen siparisi dogrudan siparis listesine bu sekilde gonderdim.
    if musteri == '0': # Musterinin siparisini 0'a basarak tamamlamasini sagladim.
        break
    print("Siparisleriniz:", siparis_listesi) # Bu kisma kadar musteriden siparisi alinip, siparis_listesi adli listeye ekledim.
hesap=0     #Bu kisimdan itibaren siparisin ucreti hesaplandim.
for i in siparis_listesi:  #Once siparis listesindeki tum elemanlar tek tek gezildi.
    if i in menu1:  #musterinin siparisinin sozlukteki eslesmesine bakildi,
        hesap += menu1[i]  #Siparislerin sozlukteki value degeri fiyati belirttigi icin her turda hesaba eklenmesi sagladim.
    
print("Siparisinizin tutari", hesap, "Euro'dur. \nAfiyet olsun")

# 3. Bonus Soru - Mors Alfabesi -

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
kullanici= input("Bir kelime ya da soz dizini yaziniz:")
buyuk_harf= kullanici.upper() # Kullanicinin kucuk harf kullanmasi durumuna karsin bunu yaptim.
harf=tuple(buyuk_harf) # Kullanicidan gelen degeri tek tek ele almak istedigim icin gelen veriyi tuple'a cevirdim.
mors=() # Sozluk icindeki harflerin mors karsiliklarini burada toplamak icin bos bir kume actim.
for i in harf: # i'nin tuple'a donusen kumede dolasmasini sagladim.
    if i in MORSE_CODE_DICT: # Uzerine geldigin eleman eger Morse dictionary'de varsa sartini olusturdum.
        mors += (MORSE_CODE_DICT[i],) # Sartin saglanmasi durumunda harf degerlerini mors kumesine gondermesini sagladim.
print(mors)
