from product_manager import ProductManager
from product import Product
from cart import Cart

proman = ProductManager()

proman.add_product(Product("majica", 1500, 5))
proman.add_product(Product("patike", 8500, 2))
proman.add_product(Product("dukserica", 2500, 3))
proman.add_product(Product("trenerka", 3000, 2))
proman.add_product(Product("lopta", 1500, 1))



cart = Cart()

cart.add_to_cart(Product("cipele", 8500, 5))
cart.add_to_cart(Product("farmerke", 3000, 7))
cart.add_to_cart(Product("potkosulja", 1500, 3))

