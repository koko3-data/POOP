class Person:
    
    def __init__ (self,name :str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        # return f"Person created with name: {self.name} and phone number: {self.phone_number}"
    
class Client(Person):

        def __str__(self):
           return f"Client created with name :{self.name} and phone number: {self.phone_number}"
        

#creating ths instance of the Client class
client = Client("Omolola", "+48-881278182")
print(client) 
print(type(client) )
print(type(client.phone_number))
print(type(client.name))
# This will show that client is an instance of Client class

        