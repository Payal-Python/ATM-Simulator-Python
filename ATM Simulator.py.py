#ATM Machine-Made by Payal
#datetime Tool Box,def(),for(mini statement),While(tries),while True break,multiple if's else.

print("************Mini ATM Machine******************")
import datetime

Balance=5000
History=[]
PIN="1234"

def show_balance():
    print("Current Balance-Rs.",Balance)
    
def Deposit():
    global Balance
    Amount=float(input("Enter your Amount-Rs. "))
    Balance=Balance+Amount
    time=datetime.datetime.now().strftime("%d-%m %H:%M")
    print("Deposite Successful.New Balance=Rs.",Balance)
    History.append(f"{time}/ Deposited=Rs.{Amount}")
    
def Withdraw():
    global Balance
    Amount=float(input("Enter your Withdral Amount-Rs. "))
    if Amount<=5000:
        Balance=Balance-Amount
        time=datetime.datetime.now().strftime("%d-%m %H:%M")#--------------phla datetime=toolbox--->dibba---->.now()button
        print("Withdraw Successful.Availble Balance=Rs.",Balance)
        History.append(f"{time}/Withdraw=Rs.{Amount}")
    else:
        print("Do not your Sufficient Balance")
        
def Mini_statement():
    print("\n----------Mini Statement------------")
    if len(History)==0:
        print("Abhi tk koi transaction Nhi hua")
    else:
        for item in History[-3: ]:
            print(item)
        print(f"Current Balance:Rs.{Balance}")
        print("----------------------------------")

tries=3
while tries>0:
    PIN=input("Enter your PIN- ")
    if PIN=="1234":
        print("Login Successful---WELCOME PAYAL")
        break
    else:
        tries=tries-1
        print(f"Galat PIN.{tries}try bache hai")
        if tries==0:
            print("ATM Block ho gya.kl aana")
            exit()
             
while True:
    print("Kya krna hai-\n1.Balance Check \n2.Deposit\n3.Withdraw\n4.Mini Statement\n5.exit")
    Choice=input("Choose the option 1/2/3/4/5")

    if Choice=="1":
        show_balance()
    elif Choice=="2":
        Deposit()
    elif Choice=="3":
        Withdraw()
    elif Choice=="4":
        Mini_statement()
    elif Choice=="5":
        print("Thank You Payal!Paise Sambhal ke Rakhana")
        break
    else:
        print("Invalid Choice")
            

