#inventory management

inventory = {    #dictionary to store player inventory
    "items": []
}

#load inventory from a file
def load_inventory():
    try:
        with open('inventory.txt', 'r') as file:
            inventory["items"] = file.read().splitlines()
    except FileNotFoundError:
        print("No saved inventory found, starting with an empty inventory.")

#save inventory to a file
def save_inventory():
    with open('inventory.txt', 'w') as file:
        for item in inventory["items"]:
            file.write(item + '\n')


#function to add item to inventory
def add_item(item): 
    inventory["items"].append(item)

def show_inventory():
    if inventory["items"]:
        inventory_list = ", ".join(inventory["items"])
        return inventory_list
    else:
        return "No items in inventory"

