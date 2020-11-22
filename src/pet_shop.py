# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"] 

def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove 

def add_or_remove_cash(shop, cash_to_add_or_remove):
    shop["admin"]["total_cash"] += cash_to_add_or_remove 

def get_pets_sold(amount):
    return amount["admin"]["pets_sold"]


def increase_pets_sold(amount_1, amount_2):
    amount_1["admin"]["pets_sold"] += amount_2
    
def get_stock_count(shop):
    return len(shop["pets"])
    

def get_pets_by_breed (pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed



def get_pets_by_breed (shop, breed):
    pets_by_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed


def find_pet_by_name (shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet




#  def remove_pet_by_name(shop,pet_name):
#     for pet in shop["pets"]:
#         if pet["name"] == pet_name:
#             del pet



def add_pet_to_stock(shop, new_pet_1):
    shop["pets"].append(new_pet_1)


def get_customer_cash(costumer):
    return costumer["cash"]

def remove_customer_cash(customer, cash_remove):
    customer["cash"] -= cash_remove















    


        


    
