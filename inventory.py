
class Product:

    def __init__(self,price,idItem,quantity):
        self.price = price
        self.idItem = idItem
        self.quantity = quantity


    def return_product(self):
        print("Price:",self.price, "ID:", self.idItem, "Quantity:", self.quantity)


#We create a new product
coca_cola = Product("$5","2","200")
pepsi = Product("$3","1", "100")


#Return product Func to return the object
coca_cola.return_product()
pepsi.return_product()



