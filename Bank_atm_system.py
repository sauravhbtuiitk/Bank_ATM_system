class Atm:

  #constructor(special function don't need to call just make object)
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    user_input = input("""
    Hi how can i help you ?
    1. press 1 to create pin
    2. press 2 to change pin
    3. press 3 to check balance
    4. press 4 to withdraw 
    5. Anything else to exist
    """)
    if user_input == '1':
      self.create_pin()
      #create pin
    elif user_input == '2':
      self.change_pin()
      #change pin
      
    elif user_input == '3':
      self.check_balnce()
      
      #check balance
    elif user_input == '4':
      self.withdraw()
      #withdraw
      
    else:
      print('thank you for use')
      exit()
  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.balance = user_balance

    print('pin created sucessfully')
    self.menu()

  def change_pin(self):
    
    old_pin = input('enter old pin')

    if old_pin == self.pin :
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
      self.menu()
    else:
      print('nai karne de sakta re baba')
      self.menu()

  def check_balnce(self):
      user_pin = input('enter you pin')
      if self.pin == user_pin:
        print('your balance is',self.balance)
      else:
        print('chal nikal bc')
      self.menu()

  def withdraw(self):

      user_pin = input('enter your pin')

      if user_pin == self.pin:

        amount = int(input('enter the amount'))
        if amount <= self.balance:
          self.balance = self.balance - amount
          print('withdrawl successful balance is',self.balance)
        else:
          print('abe garib')
      else:
        print('sale chor')
      self.menu()
    
obj = Atm()
