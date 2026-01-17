# Object - bundle of attributes (variables) and methond(functions) on what that object can do
        # You neeed class to create an object
# class - blueprint or prototype to design the struture and layout of an object



class ecomm:

    def __init__(self, name, type, price):
        self.name= name
        self.type = type
        self.price= price

    def brand(self):
        print(f'{self.name} is a brand for {self.type}')

    def prices(self):
        print(f'{self.name} has price of Rs. {self.price}')

    


user1= ecomm('Shopify','Ecomm', 4500)
user2= ecomm('Automate','Electric Car', 6500)
user3= ecomm('Agro','Agriculture', 3500)

print(f"{user1.name}, {user1.type}, Rs. {user1.price}")
user1.brand()
user1.prices()
user2.brand()
user2.prices()
user3.brand()
user3.prices()


