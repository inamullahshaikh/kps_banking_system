from server.bank import Bank
import threading

def menu():
    bank = Bank()
    while(True):
        print("=====MENU=====")
        print("1. Add users")
        print("2. Delete users")
        print("3. Login users")
        print("4. Withdraw")
        print("5. Deposit")
        print("6. Get user detail")
        print("7. Transfer")
        print("8. Logout users")
        print("9. Update users")
        print("10. Exit")
        print("==============")
        opt = int(input("Enter option: "))
        while opt < 1 or opt > 10:
            opt = int(input("Invalid option selected: "))

        if opt == 1:
            size = int(input("Enter the number of users you wish to add: "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                name = input("Enter name: ")
                email = input("Enter email (Format: abc@xyz.com): ")
                phnum = input("Enter phone number (Format: +923XXXXXXXXX): ")
                PIN = input("Enter PIN (Format; XXXX): ")
                T.append(threading.Thread(target=bank.addUser, args=(name,email,phnum,PIN,)))
                print('\n')
            for t in T:
                t.start()
            for t in T:
                t.join()
        if opt == 2:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of users you wish to delete (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                IBAN = (input(f"Enter IBAN {i}: "))
                if bank.user_exists(IBAN):
                    T.append(threading.Thread(target=bank.delete_user, args=(IBAN,)))
            for t in T:
                t.start()
            for t in T:
                t.join()
        
        if opt == 3:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of users you wish to Log-in (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                IBAN = (input(f"Enter IBAN: "))
                PIN = input("enter PIN: ")
                T.append(threading.Thread(target=bank.login_user, args=(IBAN,PIN,)))
            for t in T:
                t.start()
            for t in T:
                t.join()
        if opt == 4:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of Accounts from which you would like to withdraw (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                IBAN = (input(f"Enter IBAN: "))
                amount = float(input("Enter Amount: "))
                T.append(threading.Thread(target=bank.withdraw, args=(IBAN,amount,)))
            for t in T:
                t.start()
            for t in T:
                t.join()

        if opt == 5:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of Accounts in which you would like to deposit (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                IBAN = (input(f"Enter IBAN: "))
                amount = float(input("Enter Amount: "))
                T.append(threading.Thread(target=bank.deposit, args=(IBAN,amount,)))
            for t in T:
                t.start()
            for t in T:
                t.join()

        if opt == 6:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of Accounts you would like to view (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                IBAN = (input(f"Enter IBAN: "))
                T.append(threading.Thread(target=bank.get_user_detail, args=(IBAN,)))
            for t in T:
                t.start()
            for t in T:
                t.join()
                
        if opt == 7:
            size = int(input(f"Enter the number of Accounts that you would like perform: "))
            while size < 0:
                size = int(input(f"Invalid number ( >= 0 ): "))
            T = []
            for i in range(size):
                print(f"==TRANSFER DETAILS {i}==")
                IBAN_1 = (input(f"Enter IBAN of Sender: "))
                IBAN_2 = (input(f"Enter IBAN of Reciever: "))
                amount = float(input(f"Enter Amount to transfer: "))
                PIN = int(input(f"Enter PIN of Sender: "))
                T.append(threading.Thread(target=bank.transfer, args=(IBAN_1,IBAN_2,amount,PIN,)))
            for t in T:
                t.start()
            for t in T:
                t.join()
        if opt == 8:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of users you wish to Log-out (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==USER DETAIL {i}==")
                IBAN = (input(f"Enter IBAN: "))
                T.append(threading.Thread(target=bank.logout_user, args=(IBAN,)))
            for t in T:
                t.start()
            for t in T:
                t.join()

        if opt == 9:
            t_size = bank.get_user_count()
            size = int(input(f"Enter the number of users you wish to Update (Total users: {t_size}): "))
            while size > t_size:
                size = int(input(f"Invalid number (Total users: {t_size}): "))
            T = []
            for i in range(size):
                print(f"==UPDATE USER {i}==")
                IBAN = input("Enter IBAN: ")

                print("Leave a field blank if you don't want to update it.")
                name = input("Enter new name: ").strip() or None
                email = input("Enter new email: ").strip() or None
                phnum = input("Enter new phone number: ").strip() or None

                old_pin = None
                new_pin = None
                change_pin = input("Do you want to change PIN? (yes/no): ").strip().lower()
                if change_pin == "yes":
                    old_pin = input("Enter old PIN: ").strip()
                    new_pin = input("Enter new PIN: ").strip()

                T.append(threading.Thread(target=bank.update_user_info, args=(IBAN, name, email, phnum, old_pin, new_pin)))
            for t in T:
                t.start()
            for t in T:
                t.join()

        
        if opt == 10:
            print("Exiting")
            break
if __name__ == "__main__":
    menu()