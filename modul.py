def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    with open(f"./data/{shop_file}") as f:
    
        for line in f:
            words = line.strip().split()
            if len(words) == 2:
                menu, price_str = words
                price_str = price_str.replace("원", "")

                if menu != "#쇼핑몰":
                    try:
                        price = int(price_str)
                    except ValueError:
                        print(f'Invalid price:{price_str}')

                    shop_dict[menu] = price

    return shop_dict

def item_price(shop_file, item):
    shopping_list = shopping(shop_file)
    shopping_price = shopping_list.get(item)

    return shopping_price