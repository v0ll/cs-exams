from pprint import pprint
PRODUCTS = r"products.txt"
PURCHASES =  r"purchases.txt"


def products_reader():
    products = dict()
    try:
        with open(PRODUCTS) as file: # dosyayi ac
            for line in file: # file.readline() ile dosyayi oku.
                #print(line) # P234HF22222 r1011
                lineSplitted = line.split(" ")
                productID = lineSplitted[0]
                sellerID = lineSplitted[1].rstrip("\n")
                products[productID] = sellerID
    except OSError:
        print("There is a problem with products.txt")
        exit(1)
    return products


def purchases_reader(): # 2D Dictionary olusturacagiz.
    purchases = dict()
    try:
        with open(PURCHASES) as file: # dosyayi ac
            for line in file: # file.readline() ile dosyayi oku.
                lineSplitted = line.split(" ")
                productID = lineSplitted[0]
                sellerID = lineSplitted[1].rstrip("\n")

                if productID not in purchases:
                    purchases[productID] = set() # productID: []
                    purchases[productID].add(sellerID)

                elif productID in purchases:
                    purchases[productID].add(sellerID)
    except OSError:
        print("There is a problem with products.txt")
        exit(1)
    return purchases


def compare_sellers(products, purchases):
    print("Suspicious transactions list")
    for productID, sellerIDSet in purchases.items():
        officialSeller = products[productID]
        if (officialSeller not in sellerIDSet) or (len(sellerIDSet) > 1):
            print(f"Product code: {productID}")
            print(f"Official dealer: {products[productID]}")
            print(f"Dealer list: ", end = "") # Print'ten sonra yeni satira gecmemeyi saglar
            for i in sellerIDSet:
                print(f"{i} ", end = "")
            print()
            print()


def main():
    products = products_reader()
    purchases = purchases_reader()
    compare_sellers(products, purchases)

# Squillero 
if __name__ == "__main__":
    main()


# Squillero olmayanlar icin
#main()
