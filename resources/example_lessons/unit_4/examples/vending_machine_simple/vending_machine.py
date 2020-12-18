from utilities import inventory, display_menu, get_total, item_in_inventory

def main():
    while True:
        
        # display the inventory in a nice way
        display_menu()

        item = input('Enter the name of the item you want: ')
        
        # ask again if the item isn't in the inventory
        while not item_in_inventory(item):
            print(f'{item} is not in the inventory')
            item = input('Enter the name of the item you want: ')

        item_price = inventory[item]

        # ask how many
        quantity = input(f'Enter how many {item} you want: ')

        # convert quantity to integer
        quantity = int(quantity)

        # get the total cost
        total = get_total(quantity, item_price)

        print(f'{quantity} {item} @ ${item_price:.2f} each: ${total:.2f}')

# print(__name__)

# only run main() if this file is run directly
if __name__ == '__main__':
    main()