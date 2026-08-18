
# main.py 


from product import Product 
from product_manager import ProductManager

p1 = Product("laptop", 1200, 2)
p2 = Product("cable", 20, 5)

p3 = Product("headphones", 130, 3)
p4 = Product("mic", 35, 2)
m1 = ProductManager([p11,p22])

#print(f"Product Manger is : {m1}")

m1.add_product(p3)

print(f"Ukupna cena: {m1.total_price()}")

m1.remove_product("Laptop") 
#print(f"Product Manager {m1}")
print(f"Ukupna cena: {m1.total_price()}")


