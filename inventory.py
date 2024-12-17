#inventory management

inventory = {    #dictionary to store player inventory
    "items": []
}


def add_item(item):  #function to add item to inventory
    inventory["items"].append(item)

def show_inventory():
    if inventory["items"]:
        inventory_list = ""
        for item in inventory["items"]:
            inventory_list += item +", "
        return inventory_list.strip(", ")
    else:
        return "No items in inventory"

