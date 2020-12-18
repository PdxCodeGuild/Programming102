inventory = {
    'crackers': .5,
    'cookies': .75,
    'mints': .10,
}

def display_menu():
    '''display the inventory in a nice way'''
    for item in inventory:
        # get the item's price
        price = inventory[item]

        print(f'{item} - ${price:.2f}')


def get_total(quantity, price_per):
    '''
    Return the total of quantity * price_per
    '''
    return quantity * price_per

def item_in_inventory(item):
    '''
    Return True if the item is in the inventory,
    '''
    return item in inventory


# only run code if a file is run directly
# if __name__ == '__main__':
    # print(__name__)
    # print('You just ran utilities.py!!!')