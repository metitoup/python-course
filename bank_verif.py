#!/usr/bin/python
#input a belgian bank account to check if it's a correct one
def verif_bank_account(account):
    #print (len(account))
    if len(account)==12:
        accountnm=int(account[0:10])
        checknm=int(account[10:])
        verif_code= accountnm % 97
        if checknm == accountnm % 97:
            print ("Its'OK  : " + account + " is a valid account number")
        else :
            print ("Not OK : " + account + " is not a valid account number")
    else:
        print ("Account length not valid")

if __name__ == '__main__':

    bank_account=input("Bank_account : ")
    verif_bank_account(bank_account)