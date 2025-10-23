import store_errors as e

class Product:
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        try:
            if stock < 0:
                raise e.NegativeProductStockValueError
            if price < 0:
                raise e.NegativeProductPriceValueError

            self.price = price
            self.stock = stock
        except e.NegativeProductStockValueError as exc:
            print(exc)
            self.price = 0 if price < 0 else price
            self.stock = 0 if stock < 0 else stock
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, stock: {self.stock}"
    
    def update_stock(self, quantity: int) -> None:
        try:
            if quantity < 0:
                raise e.NegativeProductQuantityError
            if self.stock + quantity < 0:
                raise e.NotEnoughProductsInStockError(self.name)

            self.stock += quantity
        except (e.NotEnoughProductsInStockError, e.NegativeProductQuantityError) as exc:
            print(exc)


class Store:
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)
    
    def list_products(self) -> None:
        print("\n=== Available Products ===")
        for product in self.products:
            print(product)
        print()
    
    def create_order(self) -> 'Order':
        return Order()

class Order:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product: Product, quantity: int) -> None:
        try:
            if product.stock < quantity:
                raise e.NotEnoughProductsInStockError(product.name)

            self.products[product] = quantity
            product.stock -= quantity 
        except e.NotEnoughProductsInStockError as exc:
            print(exc)

    
    def calculate_total(self) -> int:
        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total

if __name__ == "__main__":
    store = Store()

    apple = Product("apple", 10, 50)
    orange = Product("orange", 25, 45)
    pineapple = Product("pineapple", 100, 1)

    store.add_product(apple)
    store.add_product(orange)
    store.add_product(pineapple)

    store.list_products()

    ordr = store.create_order()

    ordr.add_product(apple, 3)
    ordr.add_product(orange, 5)

    print(ordr.calculate_total())

    ordr.add_product(pineapple, 2)

    print(apple)
    print(orange)
    print(pineapple)