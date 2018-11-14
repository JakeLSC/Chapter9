class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
    	self.item_name = item_name
    	self.item_price = item_price
    	self.item_quantity = item_quantity
    	self.item_description = item_description
    
    def __add__(self, other):
    	price1 = self.item_price * self.item_quantity
    	price2 = other.item_price * other.item_quantity
    	return (price1 + price2)

    def print_item_cost(self):
    	totalPrice = self.item_price * self.item_quantity
    	print('%s %d @ $%d = $%d' %
                (self.item_name, self.item_quantity, self.item_price, totalPrice))

    def print_item_description(self):
    	print('%s: %s' % (self.item_name, self.item_description))

if __name__ == '__main__':
	print('Item 1')
	item_name = str(input('Enter the item name:\n'))
	item_price = float(input('Enter the item price:\n'))
	item_quantity = int(input('Enter the item quantity:\n'))
	item_description = str(input('Enter item description:\n'))
	item1 = ItemToPurchase(item_name, item_price, item_quantity, item_description)

	print('\nItem 2')
	item_name = str(input('Enter the item name:\n'))
	item_price = float(input('Enter the item price:\n'))
	item_quantity = int(input('Enter the item quantity:\n'))
	item_description = str(input('Enter item description:\n'))
	item2 = ItemToPurchase(item_name, item_price, item_quantity, item_description)

	print('\nTOTAL COST')
	item1.print_item_cost()
	item2.print_item_cost()

	print('\nTotal: $%d' % (item1 + item2))

	print('Item Descriptions.')
	print(item1.print_item_description())
	print(item2.print_item_description())
