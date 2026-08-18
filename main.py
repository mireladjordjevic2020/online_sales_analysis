
# main.py 

import random
from cart import Cart
from product import Product 
from product_manager import ProductManager

p1a = Product("laptop", 1200, 2)
p2a = Product("cable", 20, 5)

p3a = Product("headphones", 130, 3)
p4a = Product("mic", 35, 2)
m1 = ProductManager([p1a,p2a])


m1.add_product(p3a)


m1.remove_product("Laptop") 

print(f"Product Manager after removing laptop: {m1}")
print(f"Ukupna cena: {m1.total_price()}")

m1.add_product(p4a)
selected_products = random.sample(m1.products, 3)
cart = Cart(selected_products)
print(f"Cart : {cart}")
