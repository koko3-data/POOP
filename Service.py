class Service:
    def __init__ (self,name, duration_min,base_price:float):
        self.name = name
        self.duration_min = duration_min
        self.base_price = base_price

    def price_quote(self):
        return self.base_price

    def info(self):
        return self.name , f"{self.duration_min}  minutes" ,f"price for service rendered is {self.price_quote()} PLN"
    
class HaircutService(Service):
    def price_quote(self):
        return super().price_quote()+ 10.0

class ManicureService(Service):
    def price_quote(self):
        return super().price_quote() + 5.0

# lola = HaircutService("Haircut", 30, 50.0)
# price =lola.price_quote()
# details = lola.info()
# print(price)
# print(details)