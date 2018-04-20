#Callum_Steedman
#Project

from sys import exit

#Opening menu
def openingMessage():
    print("1. Open an account\n2. Close an account\n3. Withdraw money\n"
          "4. Deposit money\n5. Generate a report for management\n6. Quit")

#Reading the file
def readFile():
    f = open("Bank.txt")  # opens the text file
    lines = f.readlines()
    return lines

#Putting information from files into lists
def intoList(lines):
    Account_Number = []
    Balance = []
    Fnames = []
    Lnames = []
    for i in lines:
        item = i.split(" ")
        Account_Number.append(str(item[0]))
        Balance.append(float(item[1]))
        Fnames.append(item[2])
        Lnames.append(item[3].strip('\n'))
    return Account_Number,Balance,Fnames,Lnames

#Option1
def makeAccount(Account_Number,Balance,Fnames,Lnames):
    Fname = input("Please enter your first name")
    Lname = input("Please enter your last name")
    Opening_Balance = input("How much would you like to deposit for your opening balance")
    from random import randint
    Random_account_number = randint(10000, 99999)
    Account_Number.append(str(Random_account_number))
    Balance.append(float(Opening_Balance))
    Fnames.append(Fname)
    Lnames.append(Lname)
    print(Account_Number)
    print(Balance)
    print(Fnames)
    print(Lnames)
    with open("Bank.txt", "a") as f:
        # f.write(str(Random_account_number) +"  " + Opening_Balance +" " + str(Fname) + " " + str(Lname))
        f.close()
    print("Congratulations", Fname, Lname, "Your account number is", Random_account_number)


#Option2
def closeAccount(Account_Number,Balance,Fnames,Lnames):
    Number_Delete = input(str("Please enter the account number you would like to delete"))
    if Number_Delete in Account_Number:
        Account_to_delete = Account_Number.index(Number_Delete)
        del Account_Number[Account_to_delete]
        del Balance[Account_to_delete]
        del Fnames[Account_to_delete]
        del Lnames[Account_to_delete]
        print(Number_Delete, "Has been deleted")
    else:
        print("Sorry but that account does not exist")

#Option3
def withDraw(Account_Number,Balance):
    Account_Number_minus = input("Please enter the account you would like to withdraw from")
    if Account_Number_minus in Account_Number:
        Amount_To_Subtract = input("How much woud you like to withdraw")
        Account_to_subtract = Account_Number.index(Account_Number_minus)
        Balance[Account_to_subtract] = Balance[Account_to_subtract] - float(Amount_To_Subtract)
        New_withdraw = Balance[Account_to_subtract]
        print("Your new balance is", New_withdraw, "Euro")
    else:
        print("Sorry but that account does not exist")

#Option4
def depOsit(Account_Number,Balance):
    Account_Number_add = input("Please enter the account you would like to deposit to")
    if Account_Number_add in Account_Number:
        Amount_To_Add = input("How much would you like to deposit")
        Account_to_add = Account_Number.index(Account_Number_add)
        Balance[Account_to_add] = Balance[Account_to_add] + float(Amount_To_Add)
        New_deposit = Balance[Account_to_add]
        print("Your new balance is", New_deposit, "Euro")
    else:
        print("Sorry but that account does not exist")

#Option5
def Report(Account_Number,Balance,Fnames,Lnames):
    Total = sum(Balance)
    Largest_Account = max(Balance)
    Owner = Balance.index(Largest_Account)
    Name = Fnames[Owner],Lnames[Owner]
    print(Account_Number,"\n", Balance,"\n" ,Fnames,"\n" ,Lnames)
    print("The total amount on deposit is", Total, "Euro")
    print("The largest deposit is" , Largest_Account , "Euro" , "Which belongs to" , Name)

#Option6
def Exit(Account_Number,Balance,Fnames,Lnames):
    with open("Bank.txt", "w") as f:
        for (Account_Number, Balance, Fnames, Lnames) in zip(Account_Number, Balance, Fnames, Lnames):
            f.write("{0} {1} {2} {3} \n".format(Account_Number, Balance, Fnames, Lnames))
    exit("Goodbye")


def main():
    openingMessage()
    lines_from_file = readFile()
    Account_Number, Balance, Fnames, Lnames  = intoList(lines_from_file)
    try:
        while True:
            Choice = int(input("Type your choice now"))
            if Choice == 1:
                makeAccount(Account_Number, Balance, Fnames, Lnames)
            elif Choice == 2:
                closeAccount(Account_Number, Balance, Fnames, Lnames)
            elif Choice == 3:
                withDraw(Account_Number, Balance)
            elif Choice == 4:
                depOsit(Account_Number, Balance)
            elif Choice ==5:
                Report(Account_Number, Balance, Fnames, Lnames)
            elif Choice ==6:
                Exit(Account_Number, Balance, Fnames, Lnames)
    except ValueError:
        print('Input a number')
main()
