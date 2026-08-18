
# main.py 


from product import Product 
from product_manager import ProductManager

p11 = Product("laptop", 1200, 2)
p22 = Product("cable", 20, 5)

p33 = Product("headphones", 130, 3)
p44 = Product("mic", 35, 2)
m1 = ProductManager([p11,p22])

print(f"Product Manger is : {m1}")

m1.add_product(p33)

print(f"Ukupna cena: {m1.total_price()}")

m1.remove_product("Laptop") 
print(f"Product Manager {m1}")
print(f"Ukupna cen: {m1.total_price()}")


