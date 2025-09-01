n = input("Enter elements for the list: ")
spell = "lumos"
my_list = n.split()
print("Your list:", my_list)
store_runes = set()

for x in my_list :
        if x in spell :
            store_runes.add(x)
        

if store_runes <= set(spell) :
      
    print(store_runes)

else:
     
    print(-1)