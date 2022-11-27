# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_in_or_out):
    pet_shop["admin"]["total_cash"] += cash_in_or_out


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pet_sales):
    pet_shop["admin"]["pets_sold"] += pet_sales


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, pet_breed):
    pet_breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_breed_count.append(pet)
    return pet_breed_count


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    pet_index = pet_shop["pets"].index(pet)
    del pet_shop["pets"][pet_index]            


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append({"name": new_pet})


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_removed):
    customer["cash"] = get_customer_cash(customer) - cash_removed
    return customer["cash"]


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if get_customer_cash(customer) - new_pet["price"] >= 0:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet_name, customer):
    pet = find_pet_by_name(pet_shop, pet_name)
    if customer_can_afford_pet(customer, pet_name) == True:
        add_pet_to_customer(customer, pet_name)
        remove_pet_by_name(pet_shop, pet_name)
        remove_customer_cash(customer, cash_removed)
        add_or_remove_cash(pet_shop, cash_in_or_out)


