#cevap1
my_list = [1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]

my_set = set(my_list)

repeated_items = []
for item in my_set:
    if my_list.count(item) > 1:
        repeated_items.append(item)
print(*repeated_items)


#cevap2
menu={
    "kebap"       : 15.0,
    "doner"       : 8.0,
    "iskender"    : 12.0,
    "pizza"       : 7.0,
    "hamburger"   : 6.0,
    "spaghetti"   : 4.0,
}
print("***** RESTAURANT MENÜSÜ *****")
for yemek, fiyat in menu.items():
 print(yemek, ":", fiyat)

orders={}

while True:
    order=input("Lutfen siparisinizi yazin: ")
    if order not in menu:
        print("Maalesef " + order + " adında bir yemek bulunmamaktadir.")
        continue
    
    if order in orders:
        orders[order] += 1
    else:
        orders[order] = 1
    
    more_orders = input("Başka siparişiniz var mı? (evet/hayır): ")
    if more_orders == "evet":
        continue
    else:
        break

print("\nYour orders:")
total = 0
for item, count in orders.items():
    fiyat = menu[item] * count
    print(item + " x " + str(count) + " = " + str(fiyat))
    total += fiyat
print("Toplam tutar: " + str(total))
print("Bizi sectiginiz icin tesekkurler!")
    
