stuff = {
    'rope': 30,
    'torch': 10,
    'mobile': 20,
    'sim card': 50
}


def display_inventory():
    print("Total number of items:" + str(len(stuff)))
    item_total = 0

    for k, v in stuff.items():
        item_total += v

    print("Total quantity: " + str(item_total))


display_inventory()
