   # Bank Account With Withdrawal, Deposits, Minimum Balanced and Etc..

class BankAcc():                                                                                # Class ' BankAcc '
    ''' Base_Class '''
    
    Balance = 0                                                                                 # Class Variable or Static Variable.
    
    @classmethod
    def deposits(cls,amount):                                                                   # Deposits Class Function Definition... 
        
        BankAcc.Balance += amount                                                               # Adding Cash in Bank Account.
        print("Cash Deposited in Your Bank Account = {}".format(amount))
        return BankAcc.Balance
    
    @classmethod
    def Withdraw(cls,amount):                                                                   # Withdraw Class Function Definition.
        
        BankAcc.Balance -= amount                                                               # Deduction Of Cash in Bank Account.
        return BankAcc.Balance
        

class MiniBalAcc(BankAcc):
    ''' Child_Class '''
    ope = 0
    
    def __init__(self):                                                                         # Constructor
        
        self.mini_balance=500
    
    def Withdraw(self, amount):                                                                 # Withdraw Function to Implement Method Overriding. 

        if BankAcc.Balance - amount <= self.mini_balance:                                       # Checking if the Balance Amount is Smaller than MiniMum Balance...
            
            print('Sorry, {} Should be Maintained in your Bank Account.'.format(self.mini_balance))                               # Formatting
            MiniBalAcc.ope = ['None',BankAcc.Balance,amount,False]  
            
            return MiniBalAcc.ope                                                               # Passing List.

        else:
            WithAmt = BankAcc.Withdraw(amount)                                                  # WithDraw of Class ' BankAcc '
            MiniBalAcc.ope = [WithAmt,BankAcc.Balance,amount,True]
            
            return MiniBalAcc.ope                                                               # Passing List

            
# ---------------------------------- Main Program Flow begins Here ----------------------------
            
Cash = MiniBalAcc()                                                                             # Objects Of Bank Account...

# Running in While Loop For Infinite Loop...
while True:
                                                                                                 # Operations perform on I Else Statements.
    try:
        print("\n\t\t\tOmi Bank\n\n")
        Operation = int(input("1: Add Money or Deposit Money\n2: Withdraw Money\n3: Exit\n"))

    except:
        print('Invalid Input....')

    else:

        if Operation == 1:
            print('****** Add Money ******\n')
            try:
                cash = int(input('Enter Cash you want to Add\n'))

            except:
                print('Invalid Input from User,Try Again With Integers Values.')

            else:
                print('Total Cash in your Bank Account = {}'.format(BankAcc.deposits(cash)))            # It Will Call Parent Class Deposit Class_Function.

            finally:
                print('Operations Successful.')

        elif Operation == 2:

            try:
                withCash = int(input('Type Cash, you want to Withdraw from Your Account.\n'))

            except:
                print('Type Valid Cash Details, Try Again With Integers...')

            else:
                    Operate = Cash.Withdraw(withCash)                                                  # Withdraw of Child Class return either Cash is Withdraw or Not in List Manner.
                    
                    if Operate[3] == True:
                        print('Cash has Been WithDraw = {}\nRemaining Balance = {}'.format(Operate[2],Operate[1]))          # result if Success.
                    else:
                        print('Cash has Been WithDraw = {}\nRemaining Balance = {}'.format(Operate[0],Operate[1]))          # result if Unsuccess.
                        
        elif Operation == 3:
            
            break

        else:
            print('Invalid Input')
    finally:
        print('All Operations Perform Sucessfully.')
