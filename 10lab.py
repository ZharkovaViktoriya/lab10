import json
def z1():
    with open("text.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        products=data['products']
        for product in products:
            if product['available']==True:
                available="В наличии"
            else:
                available="Нет в наличии!"
            print("Название:", product['name'], '\n',"Цена:", product['price'], '\n', "Вес:", product['weight'], '\n', available)
def z2():
    k=int(input("Сколько необходимо внести новых товаров?: "))
    new_products=[]
    while k!=0:
        name=input("Название продукта: ")
        price=int(input("Цена: "))
        weight=int(input("Вес: "))
        available=input("Наличие(да/нет): ")
        if available=="да":
            available=True
        else:
            available=False
        new_product={'name': name, 'price': price, 'available': available, 'weight': weight}
        new_products.append(new_product)
        k-=1
    print(new_products)
    with open('text.json') as f:
        data= json.load(f)
        data['products'] += new_products
    with open('text.json', 'w') as f:
        json.dump(data, f,ensure_ascii=False, indent=2)
    with open("text.json", "r") as f:
        data = json.load(f)
        products=data['products']
        for product in products:
            if product['available']==True:
                available="В наличии"
            else:
                available="Нет в наличии!"
            print("Название:", product['name'], '\n',"Цена:", product['price'], '\n', "Вес:", product['weight'], '\n', available)
def z3():
    ru_en={}
    with open('en-ru.txt', "r", encoding="utf-8") as f:
        for s in f:
            para = s.strip().split("-")
            en=para[0]
            ru = para[1].split(",")
            for ru_1 in ru:
                if ru_1 in ru_en:
                    ru_en[ru_1]+=en
                else:
                    ru_en[ru_1]=en
    sorted_ru_en = dict(sorted(ru_en.items()))
    with open('ru_en.txt', "w", encoding="utf-8") as f:
        for key,value in sorted_ru_en.items():
            f.write(f"{key} - {value}\n")

z1()
z2()
z3()
