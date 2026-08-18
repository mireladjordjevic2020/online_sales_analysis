from product import Product

class ProductManager : 
	def __init__(self, products: list[Product]): 
		self.products = products

	def __str__(self):
		result = ""
		for p in self.products : 
			result += str(p) + "," 
		return result

	def add_product(self, product): 
		self.products.append(product)

	def total_price(self): 
		
		return sum([price for price in map(lambda x : x.get_price() * x.get_quantity(), self.products)]) 

