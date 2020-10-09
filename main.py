
def todoEkle():
    yapılacakEkle = input("Yapılacak Ekle:")
    todoLisitTxt = open("todoLisit.txt", "a")
    todoLisitTxt.write("\n")
    todoLisitTxt.write(yapılacakEkle)
    todoLisitTxt.close()
    readList()


def removeItem():
    removeditem = input("Silmek istedğinizi işi yazınız")
    todoLisitTxt = open("todoLisit.txt", "r")
    data = todoLisitTxt.readlines()

    with open("todoLisit.txt", "w") as todoLisitTxt:
        for line in data:
            if line.strip("\n") != removeditem:
                todoLisitTxt.write(line)

def readList():
    todoLisitTxt = open("todoLisit.txt", "r")
    print(todoLisitTxt.read())
    todoLisitTxt.close()


def ereasetodoListTxt():
    todoLisitTxt = open("todoLisit.txt", "w")
    todoLisitTxt.truncate(0)
    todoLisitTxt.close()





def mainComand():
    operation = input('''
Lütfen aşağıdaki komutlardan birini seçiniz:

1: Yapılacak Ekle
2: Yapılacak Çıkart
3: Yapılacakları Görüntüle
4: Tüm Yapıalcakaları Sil
5: Programdan Çık

''')


    if operation == '1':
        todoEkle()

        mainComand()

    elif operation == '2':

        removeItem()
        mainComand()


    elif operation == '3':
        readList()
        mainComand()



    elif operation == '4':
        ereasetodoListTxt()
        mainComand()


    elif operation == '5':
        print("Programdan Çıkılıyor")



    else:
        print('Geçersiz bir komut lütfen tekrar deneyiniz.')
        mainComand()

mainComand()
