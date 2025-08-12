class Payment_Method:

    def __init__(self,holders_name):
        self.holders_name = holders_name

    def make_payment(self,amount):
        self.amount = amount
        """This method should be overridden by subclasses to implement unique payment logic in subclasses."""
        raise NotImplementedError("Subclasses must implement this method")
        

class Card(Payment_Method):
    
    def __init__(self,holders_name,card_number):
        super().__init__(holders_name)
        self.card_number = card_number

    def make_payment(self, amount):
        print(f"{self.holders_name} is paying {amount} using  Card.")

class Cash(Payment_Method):

    def make_payment(self, amount):
        print(f"{self.holders_name} is paying {amount} using Cash.")

class BLIK (Payment_Method):

    def __init__(self,hoders_name,blik_code):
        super(). __init__(hoders_name)
        self.blik_code = blik_code

    def make_payment(self, amount):
        print(f"{self.holders_name} is paying {amount} using BLIK.")

#Create instances of each payment method
card_payment = Card (" Omolola")
cash_payment = Cash ("Dmytro")
blik_payment = BLIK ("Aisha")

#Make payments using each method
card_payment.make_payment(100)
cash_payment.make_payment(50)
blik_payment.make_payment(75)