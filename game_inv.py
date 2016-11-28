import operator


def display_inventory(inv):
    print ("Inventory:")
    sum_items = 0
    for key, value in inv.items():
        sum_items += value
        print (value, key)

    print ("Total number of items: {0}".format(sum_items))
    print ()


def add_to_inventory(inventory, added_items):
    for element in added_items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory[element] = 1

    return inventory


def print_table(inventory, order=None):
    longest_string = 0
    for key in inventory.keys():
        if len(key) > longest_string:
            longest_string = len(key)

    if order is None:
        print ("Inventory:")
        print ("count".rjust(longest_string + 2), "item name".rjust(longest_string + 2))
        print ("-" * (longest_string * 2 + 5))
        for key, value in inventory.items():
            print (str(value).rjust(longest_string + 2), key.rjust(longest_string + 2))

    if order == "count,desc":
        print ("Inventory:")
        print ("count".rjust(longest_string + 2), "item name".rjust(longest_string + 2))
        print ("-" * (longest_string * 2 + 5))
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1))
        for key, value in sorted_inv:
            print (str(value).rjust(longest_string + 2), key.rjust(longest_string + 2))

    if order == "count,asc":
        print ("Inventory:")
        print ("count".rjust(longest_string + 2), "item name".rjust(longest_string + 2))
        print ("-" * (longest_string * 2 + 5))
        sorted_inv = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
        for key, value in sorted_inv:
            print (str(value).rjust(longest_string + 2), key.rjust(longest_string + 2))


def import_inventory(inv, filename):
    with open(filename, "r") as f:
        import_inv = {}
        # take the elements to the new dict
        for line in f.readlines():
            element = line.strip().split(",")
            if element[1].isnumeric() is False:
                continue
            else:
                import_inv[element[0]] = int(element[1])

        # compare the original and the new dict, and add the new dict content to the orig dict
        for key, value in import_inv.items():
            if key in inv:
                inv[key] += value
            else:
                inv[key] = value

    return inv


def export_inventory(inv, filename):
    with open(filename, "w") as f:
        f.write("item" + "," + "count name" + "\n")
        for key, value in inv.items():
            f.write(str(key) + "," + str(value) + "\n")


def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    display_inventory(inv)

    # added items to the inv and print out it
    added_inv = add_to_inventory(inv, dragon_loot)
    display_inventory(added_inv)

    print_table(added_inv, "count,asc")

    # import inventory
    added_and_imported_inv = import_inventory(added_inv, "inventory.csv")
    print_table(added_and_imported_inv, "count,asc")

    # export the inventory
    export_inventory(added_and_imported_inv, "exported_inv.csv")


main()
