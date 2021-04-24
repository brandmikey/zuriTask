#You can *Deposit, *Withdraw(If you have sufficient funds),
#and check your *Account Balance at any point in time....
#you can also *Re-login after you exit,and your Balance in Intact
 
import random

database={}

def init():
    
    print('--Welcome to Bank PHP--')
    start()
def start():
    exsistingUser=int(input('\n Do you have an Account with us?\n (1).Yes (2) No\n'))
    if(exsistingUser ==1):
        login () 
    elif(exsistingUser ==2):
        register()      
    else:
        print('Invalid input')       
        start()
            
            


def login ():
    print('\n== Login ==')
    loginId= int(input('Account Number:'))
    passwordId= input('Password:')
    for useraccountNum,userdetails in database.items():
        if(loginId == useraccountNum):
            if(userdetails[3] == passwordId):
                operations(userdetails)
            else:
                print('Invalid Login Details')
                start()
    else:
        print('\nINVALID Login Details\n')
        start()


    
def register():
    print('*** Registration Details ***')
    first_name= input('Your First Name:\n')
    last_name=input('Your Last Name:\n')
    email=input('Your Email address:\n')
    password= input('your password:\n')  
    accountNum= generateAccountNum()
    database[accountNum]=[first_name, last_name, email, password]
    print( '--Your Account Number--\n  %d' %accountNum)
    print('Make sure you keep it safe')
    login()


    
def operations(user):
    print('\n        ***WELCOME %s %s***\n' %(user[0],user[1]))
    options()

def options():
    optionlist= int(input('\n-Which Operations Would you Like to Perform-\n (1).Deposit         (2).Withdrawals\n (3).Account Balance (4).Complaint (5).Exit\n'))
    if( optionlist == 1): depositOperation()
    elif( optionlist == 2): withdrawalOperation()
    elif( optionlist == 3): balance()
    elif( optionlist == 4): ComplaintOperation()
    elif( optionlist == 5): close()
    options()


#Calculation of Acoount Balance    
initialBalance= 0
deposit=[]
withdrawal=[]
def totalDeposit():
    return sum(deposit)

def totalWithdrawal():
    return sum(withdrawal)
    
def balance():
    D= totalDeposit()
    W= totalWithdrawal()
    print('**Account Balance**')
    print( initialBalance + D - W)
    
def bal():
    D= totalDeposit()
    W= totalWithdrawal()
    return initialBalance + D - W
    
    

    
    
def depositOperation():
    depositAmount= int (input('Type in Deposit Amount\n'))
    print('Deposit of [ %d ] SUCESSFULL!\n' %depositAmount)
    deposit.append(depositAmount)
    balance()
    endDeposit= int(input('\n(1)Perform Other Operations (2)Exit\n' ))
    if(endDeposit == 1): options()
    elif(endDeposit == 2): close()
    else:options()
              
    
    
    
def withdrawalOperation():
    withdrawalAmount=int(input('withdrawal Amount\n'))
    balance1= bal()
    fundAvailability= balance1 - withdrawalAmount
    if(fundAvailability >= 0):      
        withdrawal.append(withdrawalAmount)
        print('Take your cash== %d ==\n' %withdrawalAmount)
        balance()
        endWithdrawal= int(input('\n (1)Perform Other Operations (2)Exit\n'))
        if(endWithdrawal == 1): options()
        elif(endWithdrawal == 2): close()
        else:options()
    else:
        balance()
        print('--Insuffisient Funds!--!\n')
        
    


def ComplaintOperation():
    input ('in One sentence,type in your complain\n')
    print('Thans for the Feedback , We Will get back to you Shortly')
    endComplaint= int(input('\n (1)Perform Other Operations (2)Exit\n'))
    if(endComplaint == 1): options()
    elif(endComplaint == 2): close()
    else:options()
    

          

def generateAccountNum():
    return random.randrange(1111111111,9999999999)

def close():
    print('>> Thanks For Banking With Us, Do have a Lovely Day! <<\n\n\n')
    endclose=int(input('REOPEN App? (1).YES (2). NO\n'))
    if(endclose==1):start() 


init()
