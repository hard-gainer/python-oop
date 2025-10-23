class NotEnoughProductsInStockError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Error: not enough products in stock for {self.name}"

class NegativeProductQuantityError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"Error: desired quantity cannot be negative"

class NegativeProductStockValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"Error: product stock can not be negative"

class NegativeProductPriceValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"Error: product price can not be negative"