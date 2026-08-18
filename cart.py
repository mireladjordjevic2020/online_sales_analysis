from product import Product 

class Cart:
 
	def __init__(self, cart_items: list[Product]): 
		self.cart_items = cart_items

	def __str__(self):
		result = ""
		for p in self.cart_items : 
			result += str(p) + "," 
		return result

	def add_product(self, product): 
		self.cart_items.append(product)

	def total_price(self): 
		
		return sum([price for price in map(lambda x : x.get_price() * x.get_quantity(), self.cart_items)]) 

