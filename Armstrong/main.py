# Bu iki satir arasini kendiniz doldurmaniz gerekiyor.
# indirdiginiz numbers.txt dosyasina VSCode uzerinden sag tiklayip Copy Path yapin, 
# elde ettiginiz degeri tirnak isaretlerinin arasina yapistirin.
NUMBERS = r""


def read_file():
    numbersList = list()
    try:
        with open(NUMBERS) as file:  # DOSYA ACMA
            fileRead = file.readlines()
            for number in fileRead: # 42/n
                numberStripped = number.strip("\n") # 42
                numbersList.append(numberStripped)
    except OSError as problem:
        print("There is a problem with the files.")
        exit(1)
    return numbersList


# [42, 7, 1634, 1743, 2, 45656, 565, 371, 407, 8208, 153, 6, 4646, 370, 9474, 9475]
def armstrong(numbersList):
    armstrongList = list()
    for number in numbersList:# 8208 = STRING
        lengthNumber = len(number) # uzunluk = 4 = integer
        sum = 0
        for letter in number: # 8208
            sum = sum + int(letter) ** lengthNumber
        if sum == int(number):
            armstrongList.append(int(number))
    return armstrongList


# listenin icerisindeki tum elemanlar nasil print edilir?
def print_all(armstrongList):
    print(f"Number of Armstrong Numbers: {len(armstrongList)}")
    for number in armstrongList:
        print(number)


def main(): # HUB -> ÇEKİRDEK , TOPLANMA ALANI
    numbersList = read_file()
    armstrongList = armstrong(numbersList)
    print_all(armstrongList)





# SQUILLERO icin  1. version
if __name__ == "__main__":
    main()

# PROFu SQUILLERO OLMAYANLAR icin  2. version
main()
