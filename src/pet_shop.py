# WRITE YOUR FUNCTIONS HERE
# 1
def get_pet_shop_name(shop):
    return shop["name"]
# 2
def get_total_cash(shop):
    return shop["admin"]["total_cash"] 
# 3
def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove 
# 4
def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove 
# 5
def get_pets_sold(amount):
    return amount["admin"]["pets_sold"]

# 6
def increase_pets_sold(amount_1, amount_2):
    amount_1["admin"]["pets_sold"] += amount_2
 
# 7
def get_stock_count(shop):
    return len(shop["pets"])
    
# 8
def get_pets_by_breed (pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed


# 9
def get_pets_by_breed (shop, breed):
    pets_by_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

# 10
def find_pet_by_name (shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# 11
def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet


# 12
def remove_pet_by_name(shop,pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)


# 13
def add_pet_to_stock(shop, new_pet_1):
    shop["pets"].append(new_pet_1)

# 14
def get_customer_cash(costumer):
    return costumer["cash"]

# 15
def remove_customer_cash(customer, cash_remove):
    customer["cash"] -= cash_remove

# 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

# 17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False 
    

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False 