"""
Soru 1
Bir dizi içeren bir liste verildiğinde, listedeki tekrarlayan unsurları bulan bir Python programı yazın.
Bu soruyu cozerken Python kumelerini calisin kullanarak cozer.

Örnek Girişi:
1 2 3 4 12 45 1 2 54 65 77 8 1 2

Örnek Çıktısı:
Tekrarlayan öğeler: {1, 2}


"""

lst = [1,2,3,4,12,45,1,2,54,65,77,8,1,2,9,0,3,4,5]

tekrar_list={ i for i in set(lst) if lst.count(i)>1 }
print(f"Tekrar eden sayilar : {tekrar_list} ")  #{1, 2, 3, 4}



""""
Soru-2
Bir restoran yolunun Python sözlüklerini kullanarak oluşturun ve kullanıcıların yemeklerini ziyaret etmesine izin verin.

Aşağıdaki adımları izleyin:

Restoranın gezdiği bir Python sözlüğü olarak oluşturun. Her yemek bir anahtar kelime, fiyatı ise değer olarak yönlendirir.
Kullanıcının menüyü görmek için menüyü ekranı yazdırın.
Kullanıcıdan yemek siparişi isteyin. Kullanıcı, bir yemek adı veya numarasına sahiptir.
Kullanıcının yemeklerini bir sözlükte saklamak.
Kullanıcının ürünlerini ekrana yazdırın ve toplam fiyatını hesaplayın.

"""
#Restoranın gezdiği bir Python sözlüğü olarak oluşturun. Her yemek bir anahtar kelime, fiyatı ise değer olarak yönlendirir.
menu = {
    "01": "Ezogelin Fiyat  € - 6.99 ",
    "02": "Mercimek Fiyat  € - 5.99 ",
    "03": "Iskembe Fiyat   € - 10.99 ",
    "04": "Kellepaca Fiyat € - 12.99 ",

    "11": "Adana_Kebap Fiyat  € - 11.99 ",
    "12": "Et_Sis Fiyat       € - 12.99 ",
    "13": "Tavuk_Sis Fiyati   € -  9.99 ",
    "14":  "Beyti_Kebap Fiyat € - 12.09 ",
        
    "21": "Kusbasi_Kasarli_Pide Fiyat € - 11.99 ",
    "22": "Kasarli_Pide Fiyat         € - 12.00 ",
    "23": "Kasar_Sucuk_Pide Fiyat     € -  9.99 ", 
    "31": "Cola Fiyat           € - 3.99",
    "32": "Portakal_Suyu Fiyat  € - 4.99",
    "33": "Su Fiyat             € - 1.99",
    
}
#Kullanıcının yemeklerini bir sözlükte saklamak.
siparisler={}



#Kullanıcının menüyü görmek için menüyü ekranı yazdırın.

print("Welcome to our restaurant! Here's our menu:")
for siparis in menu :
    print(f"{siparis} :  {menu[siparis]}")

#Kullanıcıdan yemek siparişi isteyin. Kullanıcı, bir yemek adı veya numarasına sahiptir.
while True:
    siparis= input("Lutfen siparislerinizin numarasini seciniz  :")
    if siparis == "q":
        break
    if siparis not in menu:
        print("siparis bulunamadi tekrar deneyiniz")
    else:
        if siparis in siparisler:
            siparisler[siparis] += 1
        else:
            siparisler[siparis] = 1
            print("Secilen  :" + menu[siparis] + " siparisiniz.")
#Kullanıcının ürünlerini ekrana yazdırın ve toplam fiyatını hesaplayın.
print("Siparisleriniz  :")
total_fiyat= 0
for siparis in siparisler:
    yemek_name = menu[siparis].split(" - ")[0]
    yemek_fiyat = float(menu[siparis].split(" - ")[1])
    total_yemek_fiyat = yemek_fiyat * siparisler[siparis]
    print(f"{yemek_name}   x   {str(siparisler[siparis])} adet fiyati  {str(total_yemek_fiyat)}€ ")
    total_fiyat += total_yemek_fiyat
print(f"Toplam fiyat:  {str(total_fiyat)} €")
