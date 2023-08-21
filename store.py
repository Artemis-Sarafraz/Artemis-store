import os
current_path = os.getcwd()

print("Artemis store")
print()

def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- exit")
    print()

myfile = open("store.txt" , "r")
data = myfile.read()
print()


PRODUCT = []
product_list = data.split("\n")
print(product_list)
for i in range (len(product_list)):
    product_info  =product_list[i].split(" , ")
    mydict = {}
    mydict["code"] = product_list[0]
    mydict["name"] = product_list[1]
    mydict["price"] = product_list[2]
    mydict["count"] = product_list[3]
    PRODUCT.append(mydict)
    print(product_info)
print()

show_menu()
choice = int(input("please chosse a number:"))

if choice == 1:
    print("what do you want to add ? \n  pleas just wright what you want. \n" )
    b = int(input("code: "))
    c = str(input("name: "))
    d = int(input("price: "))
    e = int(input("count: "))
    a = b,c,d,e
    product_list.append(a)
    print(product_list)
elif choice == 2:
    pass
elif choice == 3:
    print("delete product: \n" , "if you wanna to remove a things , please write a number.(frome 0 till that you want)")
    a = int(input())
    del product_list [a]
    print(product_list)
elif choice == 4:
    def searchText(path,text):
        os.chdir(path)
        files = os.listdir()
        for file_name in files :
            abs_path = file_name
            if os.path.isfile(abs_path):
                with open(file_name , 'r' , encoding='utf-8') as f:
                    line = f.read()
                    if text in line:
                        final_path = file_name
                        print(text + "word found in this path" + final_path + "and index: " + str(line.file(text)))
                    else:
                        print("no match found in" + abs_path)
elif choice == 5:
    print(data)
elif choice == 6:
    q = input("what do you want to buy?  write:  ")
    if q in data :
        print(open (data(q)))
    else:
        print("sorry! we dont have this!")
elif choice ==7:
    print("Thank you!")
    exit