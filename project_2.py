

class User:
    def __init__(self,name,gender,age):
        print(f'welcome {name} ')
        self.name = name
        self.gender = gender
        self.age = age
        self.balance = 0
    

    def show_details(self):
        print('personal information ...')
        print(f"name  : {self.name}")
        print(f"gender  : {self.gender}")
        print(f"age  : {self.age}")
        print(f"balance  : {self.balance}")



class Bank(User) :

    def __init__(self,name,gender,age):
        super().__init__(name,gender,age)
        self.balance = 0


    def deposite(self,amount):
        self.balance += amount
        print(f" you current balance = {self.balance}")

        
    def withdraw(self,amount):
        if amount <= self.balance :
           self.balance -= amount
           print(f"withdraw done successfully , you current balance = {self.balance}")
        
          
        else :
            print(f" you do not have insuffcient funds , balance {self.balance}")



    def show_balance(self):
         self.show_details()





u1 = Bank('Muhannad' , 'Male ', 26 )       
u1.show_details()



u1.deposite(100)
u1.deposite(500)

u1.withdraw(400)
#u1.withdraw(190)

u1.show_balance()
