class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
   
    def make_withdrawal(self, amount):
        self.account_balance-=amount


    def display_user_balance(self):

       print(f"the name of the user is {self.name} and the account balance is {self.account_balance}")

    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        self.account_balance-=amount

mohammed=User("Mohammed","mohammed@gmail.com")
asma= User("Asma", "Asma@gmail.com")
lateen= User("lateen","lateem@gmail.com")

asma.make_deposite(100)
asma.make_deposite(1000)
asma.make_deposite(3000)
asma.make_withdrawal(900)
asma.display_user_balance()

mohammed.make_deposite(2000)
mohammed.make_deposite(2500)
mohammed.make_withdrawal(600)
mohammed.make_withdrawal(150)
mohammed.display_user_balance()

lateen.make_deposite(5000)
lateen.make_withdrawal(200)
lateen.make_withdrawal(300)
lateen.make_withdrawal(1000)
lateen.display_user_balance()

asma.transfer_money(lateen,3000)
lateen.display_user_balance()
asma.display_user_balance()

