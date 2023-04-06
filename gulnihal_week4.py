#soru 1
a=[1,5,87,9,7,4,6,6,3,6,9,0,24,65,34,8]
tekrarlayan=set()
for i in a:
    if a.count(i)>1:
        tekrarlayan.add(i)
print(tekrarlayan,"sayilari listenizde tekrar ediyor.")


#soru2
Menu            ={"mercimek":7,
                 "tavuk":10,
                 "ezogelin":7,
                  
                  "humus":5,
                  "sarma":8,
                  "salad":5,
                  "mucver":6,
                  
                  "adana kebab":23,
                  "beyti kebab":25,
                  "iskender kebab":23,
                  "chicken shish":18,
                  "doner plate":18,
                  "falafel plate":18,
                  
                  "kunefe":10,
                  "pistachio baklava":9,
                  "walnut baklava":8,
                  "sutlac":6,
                  "kazandibi":6}    
print("Menu")

for yemek, fiyat in Menu.items():
    print("{} = {}".format(yemek, fiyat))

siparis={}
total=0
while True:
    secim=input("Lutfen siparis etmek istediginiz yemeklerin isimlerini giriniz.siparisi tamamlamak icin 'q'")
    if secim =="q":
        break
    elif secim in Menu.keys():
        siparis[secim]="siparis"
        for yemek, fiyat in Menu.items():
            for a in siparis:
                if a == yemek:
                    total += fiyat
    else:
        continue    

 

print("siparisleriniz", siparis,"\n","toplam tutar:",total)   
