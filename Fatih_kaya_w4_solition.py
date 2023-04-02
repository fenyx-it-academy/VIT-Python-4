# Soru-1

my_list = [1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]
my_set = {i for i in my_list if my_list.count(i) > 1}
print(f"Tekrarlayan öğeler: {my_set}")

#Soru-2
my_menu= {
    "Main_corse":{
        "Soup": 5,
        "Meatball":15,
        "Pizza":20,
        "Pasta":10,
        "Doner":10,
        "No": 0},
    "Dessert":{
        "Baklava":10,
        "Sutlac":10,
        "No": 0},
    "Appetizer":{
        "Ezme":3,
        "Şakşuka":3,
        "No": 0},
    "Drinks":{
        "Cola":5,
        "Ayran":5,
        "No": 0}    
        }
currency = "€"
for key, value in my_menu.items():
    print(f"***  {key}  ****")
    for subkey, subvalue in value.items():
        print(f"\t{subkey} -> {currency}{subvalue}")

orders  = {}
total= 0
order_list = ["Main_corse", "Dessert", "Appetizer", "Drinks"]

for order in order_list:
    select = input(f"Please select your {order}: ")
    
    while True:        
        if select not in my_menu[order]:
            print(f" <<< {select} >>> is not available. Choose again!")
            select = input(f"Please select your {order}: ")
        else:
            orders.update({select:my_menu[order][select]})
            
            print(f"{select} -> {currency} {my_menu[order][select]}")
            total += my_menu[order][select]
            break
if "No" in orders:
    orders.pop("No")
print("Your orders: ")
for key, value in orders.items():
    print(f"{key} ____ €{value}")
print(f"_____Total Price______: {currency}{total}")

# BONUS
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

choise = input("""Choose one option. 
       Text to Mors _ Press '1' 
       Mors to Text _ Press '2' 
       """)
if choise == '1':
    text = input("Enter your text: ").upper()
    for i in text:
        if i == " ":
            continue
        else:
            print(f"{MORSE_CODE_DICT[i]} ", end= " ")
else:
    mors = input("Enter your morse code: ").split(" ")
    for i in mors:
        print(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(i)], end="")      

