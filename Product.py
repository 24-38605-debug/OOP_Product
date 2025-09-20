class Product:
    Inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.Inventory.append(new_product)
        return f"Product '{name}' added successfully."
    
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.Inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return f"Product {product_id} information updated successfully."
        return "Product not found."

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.Inventory:
            if product.product_id == product_id:
                cls.Inventory.remove(product)
                return f"Product{product_id} deleted successfully."
        return "Product not found."
    

class Order:
    def __init__(self, order_id, product_id, quantity, customer_info=None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info

    def place_order(self):
        return f"Order placed successfully. Order ID: {self.order_id}"


print(Product.add_product("Pistachio Donut", "Dessert", 50, 25, "Dunkin Donut"))
print(Product.add_product("Matcha Donut", "Dessert", 100, 25, "Mr Donut"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))

order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())

