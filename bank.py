import data

def password_strength(password):
  count = 0
  if len(password) >= 8:
    count += 0.5
  if any(I.isupper() for I in password):
    count += 0.7
  if any(I.islower() for I in password):
    count += 0.7
  if any(I.isdigit() for I in password):
    count += 1
  if any(I in "!@#$%^&*" for I in password):
    count += 1
  if any(I.isspace() for I in password[1:-1]):
    count += 0.5
  return count

def create_account():
    ask_username = input("Please create user name for creating the account : ")
    print("\n")
    while ask_username in data.users_account.keys():
      print("username already exist. Please try another username.\n")
      ask_username = input("Please create user name for creating the account : ")      
     
    ask_password = input("Please create password for creating the account : ")
    print("\n")
    check = password_strength(ask_password)
    while check <= 2:
      print("password is very weak, please make a strong password\n")
      ask_password = input("Please create password for creating the account : ") 
      print("\n")
      check = password_strength(ask_password)
    ask_pin = input("Please create a 4 digit pin for your account : ")
    print("\n")
    while len(ask_pin) != 4 or not ask_pin.isdigit():
      print("pin must be 4 digits and contain only numbers.\n")
      ask_pin = input("Please create a 4 digit pin for your account : ")

    data.users_account.update({ask_username:{"password":ask_password,"pin":ask_pin,"balance":0}})
    data.users_transactions.update({ask_username:[]}) 
    print(f"Account for {ask_username} created successfully!")

def login():
    ask_username = input("Please type your user name for login : ")
    print("\n")
    while ask_username not in data.users_account.keys():
      print("username not found\n")
      ask_f = input("If you forgot your username, type (1) to create a new account, or press anything else to retry your username: ")
      if ask_f == "1":
          create_account()
          return None 
      ask_username = input("Please type correct user name for login : ")
    
    ask_password = input("Please enter password for log in : ")
    print("\n")
    while ask_password != data.users_account[ask_username]["password"]:
      print("password is incorrect\n")
      ask_password = input("Please enter correct password for log in : ")
    print(f"Login successful! Welcome {ask_username}.\n")
    return ask_username 

def deposit(current_user):
    try:
      deposit_amount = float(input("enter the amount you want to deposit : "))
      while deposit_amount < 1:
        print("minimum deposit amount is ₹1\n")
        deposit_amount = float(input("enter the amount you want to deposit : "))
        print("\n")
      
      asking_pin = input("please enter your pin : ")
      print("\n")
      while asking_pin != data.users_account[current_user]["pin"]:
        print("pin incorrect\n")
        asking_pin = input("please enter your pin : ")
        print("\n") 
      
      data.users_account[current_user]["balance"] += deposit_amount
      data.users_transactions[current_user].append(f"deposited ₹ {deposit_amount}")
      print("\n")
      print(f"Successfully deposited {deposit_amount}.\n")
    except ValueError:
      print("Invalid input. Please enter a valid number.\n")

def withdraw(current_user):
    try:
      withdraw_amount = float(input("enter the amount you want to withdraw : "))
      print("\n")
      if withdraw_amount > data.users_account[current_user]["balance"]:
        print("Insufficient balance.\n")
      else:
        asking_pin = input("please enter your pin : ")
        print("\n")
        while asking_pin != data.users_account[current_user]["pin"]:
          print("pin incorrect\n")
          asking_pin = input("please enter your pin : ")
          print("\n")
        data.users_account[current_user]["balance"] -= withdraw_amount
        data.users_transactions[current_user].append(f"withdrawn ₹ {withdraw_amount}")
        print(f"Successfully withdrawn {withdraw_amount}.\n")
    except ValueError:
      print("Invalid input. Please enter a valid number.\n")

def transfer(current_user):
    try:
      transfer_account = input("Enter the username of the account you want to transfer the money to : ")
      print("\n") 
      while transfer_account not in data.users_account.keys():
        print("user not found.\n")
        transfer_account = input("Enter the username of the account you want to transfer the money to : ")
      
      if transfer_account == current_user:
          print("Cannot transfer to your own account.\n")
          return

      transfer_amount = float(input("Enter the amount you want to transfer : "))
      print("\n")
      if transfer_amount > data.users_account[current_user]["balance"]:
        print("Insufficient balance.\n")
      else:
        asking_pin = input("Please enter your pin : ")
        print("\n")
        while asking_pin != data.users_account[current_user]["pin"]:
          print("pin incorrect\n")
          asking_pin = input("Please enter your pin : ")
          print("\n")
        
        print(f"Transferring ₹{transfer_amount} to {transfer_account}...")
        data.users_account[current_user]["balance"] -= transfer_amount
        data.users_account[transfer_account]["balance"] += transfer_amount

        data.users_transactions[current_user].append(f"transfered ₹ {transfer_amount} to {transfer_account}")
        data.users_transactions[transfer_account].append(f"received ₹ {transfer_amount} from {current_user}")
        print("\n")
        print("Transfer successful!\n")
        
    except ValueError:
      print("Invalid input. Please enter a valid number.\n")
   
def check_balance(current_user):
    asking_pin = input("Please enter your pin : ")
    print("\n")
    while asking_pin != data.users_account[current_user]["pin"]:
      print("pin incorrect\n")
      asking_pin = input("Please enter your pin : ")
    print(f"Your current balance is ₹{data.users_account[current_user]["balance"]}\n")  

def view_transactions(current_user):
    print("\nTransaction History\n")
    if not data.users_transactions[current_user]:
        print("No transactions yet for this account.\n")
        return
    for transaction in data.users_transactions[current_user]:
        print(transaction)
    print("\n")
