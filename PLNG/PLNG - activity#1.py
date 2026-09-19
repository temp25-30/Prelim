#in USD
products = {
    #price based on KG
    "Watermelon":{
        "price": 15
    } ,
    "Corn":{
        "price": 50
    } ,
    "Potato":{
        "price": 10
    } ,
    "Wheat":{
        "price": 20
    } ,
    "Carrot":{
        "price": 25
    } ,
    "Apple":{
        "price": 30
    }
}

#in EURO
euPrices = []

for key in products:
    convPrice = products[key]["price"] * 0.867
    euPrices.append(convPrice)

print("Price in USD:")
for key in products:
    print(f"Name: {key} || Price: {products[key]["price"]}")

print("\nPrice in EUROS:")
index = 0
for key in products:
    print(f"Name: {key} || Price: {round(euPrices[index], 2)}")
    index += 1
