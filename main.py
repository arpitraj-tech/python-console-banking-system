from bank import  *

print("Welcome to our local Bank".center(140))
print("\n\n")
while True :          
  asking_user_preference=(input("If  you want to create a new account type (0) or want to login your existing account type(1) : ").strip())
  print("\n")
  while asking_user_preference !="1" and asking_user_preference !="0":
     print("please enter only 1 or 0 \n")
     asking_user_preference=(input("Please enter 0 for creating a new account or 1 for login to your existing account : ").strip())
     print("\n")
  if asking_user_preference=="0" :
    create_account()
    asking_user_preference=(input("If  you want to create a new account type (0) or want to login your existing account type(1) : ").strip())
    
    while asking_user_preference=="0" :
        print("\n")
        create_account()
        asking_user_preference=(input("If  you want to create a new account type (0) or want to login your existing account type(1) : ").strip())
          
  current_user = None
  if asking_user_preference=="1" :
    print("\n")
    if  not data.users_account:       #empty dictionary evaluates to false       
       print("No account is been created till now please create a account first")
       print("\n")
       create_account()
       print("\nnow u can login using this account\n")
       current_user = login()
    else:
      current_user = login()
  
  if current_user:
    print(f"Welcome {current_user} to your account".center(120))
    print("\n")
    while True:
      ask_user=input("1.Deposit money to your account\n\n2.Withdraw money from your account\n\n3.Transfer money to another account\n\n4.Check Balance\n\n5.view transaction details\n\n6.log out\n\n")
      if ask_user=="1":
        print(deposit(current_user) )
        print("\n")
      if ask_user=="2":
        print(withdraw(current_user) )
        print("\n")
      if ask_user=="3":
        print(transfer(current_user) )
        print("\n")
      if ask_user=="4":
        print(check_balance(current_user) )
        print("\n")
      if ask_user=="5":
          print(view_transactions(current_user))
      if ask_user=="6":
          print("successfully logged out")
          break
      while ask_user not in ["1","2","3","4","5","6"] :
        print("please enter only 1,2,3,4,5,6")
        ask_user=input("1.Deposit money to your account\n\n2.Withdraw money from your account\n\n3.Transfer money to another account\n\n4.Check Balance\n\n5.view transaction details\n\n6.log out and exit\n\n")
        print("\n")
   
