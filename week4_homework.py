# Soru1
# Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan elemanlari bulan bir Python programı yazın. 
# Bu soruyu cozerken Python kumelerini kullanmaya calisin.

listem = [1,2,3,4,12,45,1,2,54,65,77,8,1,2]
listem1 = list()
setlist = set()
for i in listem:
    if i not in listem1:
        listem1.append(i)
    else:
        setlist.add(i)
print(setlist)


print("------------------------------------------------------------------------------")


# soru2
# Bir restoranın menüsünü Python sözlükleri kullanarak oluşturun ve kullanıcının yemekler sipariş etmesine izin verin.
# Aşağıdaki adımları izleyebilirsiniz:
# Restoranın menüsünü bir Python sözlüğü olarak oluşturun. Her yemek bir anahtar kelime, fiyatı ise değer olarak tanımlanabilir.
# Kullanıcının menüyü görmesi için menüyü ekrana yazdırın.
# Kullanıcıdan yemekler sipariş etmesini isteyin. Kullanıcı, bir yemek adı veya numarası girebilir.
# Kullanıcının seçtiği yemekleri bir sözlükte saklayın.
# Kullanıcının siparişlerini ekrana yazdırın ve toplam fiyatı hesaplayın.

menu = {
    "tavuk dürüm" : 5,
    "et dürüm" : 6,
    "kapsalon" : 10,
    "iskender" : 11,
    "pizza" : 8,
    "lahmacun" : 4,    
    }
print(f"""Menü          Fiyat
----          -----
""")
for i,j in menu.items():
     print(f"""{i}    \t{j} Euro """)

orders = {}
total = 0
while True:

    order = input("Lütfen siparişinizi giriniz sonlandırmak için ise q ya basınız...   : ")

    if order == "q":
            if orders == {}:
                 print("Sipariş alım sayfasından çıkılıyor...")
                 break
            else:
                 break       

    for i,j in menu.items():

        if order == i:
            orders[i] = j
            total += j
    print(orders)

for i in orders.keys():
                
    print(i)
print(f"Toplam sipariş tutarınız ise {total} avro'dur")  

print("------------------------------------------------------------------------------")

# BONUS
# Kullanıcının bir metin girmesini ve ardından bu metni Mors alfabesi koduna dönüştürüp yazdırmasını
# veya aynı şekilde Mors alfabesi kodunu alıp metne dönüştürmesini saglayan bir program yazin. 
# Asagidaki mors alfabesi sozlugunu kullanabilirsiniz.

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

word = input("Veri giriniz :")
name = list()

print(word)
for i in word:

    if i == " ":
        continue
    
    print(MORSE_CODE_DICT.get(i), end=" ")    

    
print("")
mors = input("Mors alfabesi giriniz :").split(" ")

for k in mors:
    for i,j in MORSE_CODE_DICT.items():
        if k == j:
            print(i,end = (""))
