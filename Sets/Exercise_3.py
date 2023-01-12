# Create your order for the food truck and see if your order is available

order = {'Pizza'}
menu = {'Pizza', 'Hot Dog', 'PB&J', 'Salad', 'Water', 'Soda'}

print('Order Available: ', order.issubset(menu))

other_order = {'ice cream'}
# Make an order that isn't available

print('Order not Available: ', other_order.issubset(menu))
