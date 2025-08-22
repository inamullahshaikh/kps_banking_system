from people.user import User
import threading
from .data_access import DataAccess
class Bank:
    def __init__(self):
        self._data_access = DataAccess()
        users_dict = self._data_access.load_users()
        self._users = {}
        for IBAN,u in users_dict.items():
            self._users[IBAN] = User(u["name"],u["email"],u["ph_num"],IBAN,u["PIN"], u["Balance"])
            print(self._users[IBAN])
        self._iban_counter = self._data_access.get_current_account()
        print(self._users)
        self._lock = threading.Lock()
        
    def generate_iban(self):
        iban = f"PKABCC{self._iban_counter}"
        self._iban_counter += 1
        return iban
    
    def addUser(self, name, email, ph_num, PIN):
        with self._lock:
            IBAN = self.generate_iban()
            self._users[IBAN] = User(name, email, ph_num, IBAN, PIN)
            self._data_access.add_user(self._users[IBAN])
            print(f"Account Added sucessfully. IBAN: {IBAN}")

    def delete_user(self, IBAN):
        with self._lock:
            if IBAN in self._users:
                del self._users[IBAN]
                print("Account Removed sucessfully")
                self._data_access.delete_user(IBAN)
            else:
                print("Account not found")
    
    def login_user(self, IBAN, pin):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].login(IBAN,pin)
                print(res["message"])
    def logout_user(self, IBAN):
        with self._lock:
            res = self._users[IBAN].logout()
            print(res["message"])
    def withdraw(self, IBAN, val):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].withdraw(val)
                if res["status"] == 200:
                    self._data_access.update_user(self._users[IBAN])
                print(res["message"])

    def deposit(self, IBAN, val):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].deposit(val)
                if res["status"] == 200:
                    self._data_access.update_user(self._users[IBAN])
                print(res["message"])
    
    def get_user_detail(self, IBAN):
        if IBAN in self._users:
            print(self._users[IBAN])
        else:
            print("User not found")
    def transfer(self, IBAN_1, IBAN_2, amount, pin):
        with self._lock:
            if IBAN_1 in self._users:
                res = self._users[IBAN_1].match_pin(pin)
                if res["status"] == 200:
                    if IBAN_2 in self._users:
                        res = self._users[IBAN_1].withdraw(amount)
                        if res["status"] == 200:
                            res1 = self._users[IBAN_2].forced_deposit(amount)
                            if res1["status"] == 200:
                                self._data_access.update_user(self._users[IBAN_1])
                                self._data_access.update_user(self._users[IBAN_2])
                                print(f"Amount: {amount} sucessfully transfered from {IBAN_1} to {IBAN_2}")
                        else:
                            print(res["message"])
                    else:
                        print(f"user: {IBAN_2} doesnt exist")
                else:
                   print(res["message"])
            else:
                print(f"user: {IBAN_1} doesnt exist")
    from people.user import User
import threading
from .data_access import DataAccess
class Bank:
    def __init__(self):
        self._data_access = DataAccess()
        users_dict = self._data_access.load_users()
        self._users = {}
        for IBAN,u in users_dict.items():
            self._users[IBAN] = User(u["name"],u["email"],u["ph_num"],IBAN,u["PIN"], u["Balance"])
            print(self._users[IBAN])
        self._iban_counter = self._data_access.get_current_account()
        print(self._users)
        self._lock = threading.Lock()
        
    def generate_iban(self):
        iban = f"PKABCC{self._iban_counter}"
        self._iban_counter += 1
        return iban
    
    def addUser(self, name, email, ph_num, PIN):
        with self._lock:
            IBAN = self.generate_iban()
            self._users[IBAN] = User(name, email, ph_num, IBAN, PIN)
            self._data_access.add_user(self._users[IBAN])
            print(f"Account Added sucessfully. IBAN: {IBAN}")

    def delete_user(self, IBAN):
        with self._lock:
            if IBAN in self._users:
                del self._users[IBAN]
                print("Account Removed sucessfully")
                self._data_access.delete_user(IBAN)
            else:
                print("Account not found")
    
    def login_user(self, IBAN, pin):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].login(IBAN,pin)
                print(res["message"])
    def logout_user(self, IBAN):
        with self._lock:
            res = self._users[IBAN].logout()
            print(res["message"])
    def withdraw(self, IBAN, val):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].withdraw(val)
                if res["status"] == 200:
                    self._data_access.update_user(self._users[IBAN])
                print(res["message"])

    def deposit(self, IBAN, val):
        with self._lock:
            if IBAN in self._users:
                res = self._users[IBAN].deposit(val)
                if res["status"] == 200:
                    self._data_access.update_user(self._users[IBAN])
                print(res["message"])
    
    def get_user_detail(self, IBAN):
        if IBAN in self._users:
            print(self._users[IBAN])
        else:
            print("User not found")

    def transfer(self, IBAN_1, IBAN_2, amount, pin):
        with self._lock:
            if IBAN_1 in self._users:
                res = self._users[IBAN_1].match_pin(pin)
                if res["status"] == 200:
                    if IBAN_2 in self._users:
                        res = self._users[IBAN_1].withdraw(amount)
                        if res["status"] == 200:
                            res1 = self._users[IBAN_2].forced_deposit(amount)
                            if res1["status"] == 200:
                                self._data_access.update_user(self._users[IBAN_1])
                                self._data_access.update_user(self._users[IBAN_2])
                                print(f"Amount: {amount} sucessfully transfered from {IBAN_1} to {IBAN_2}")
                        else:
                            print(res["message"])
                    else:
                        print(f"user: {IBAN_2} doesnt exist")
                else:
                   print(res["message"])
            else:
                print(f"user: {IBAN_1} doesnt exist")
    def update_user_info(self, IBAN, name=None, email=None, ph_num=None, old_pin=None, new_pin=None):
        with self._lock:
            if IBAN not in self._users:
                print(f"User with IBAN {IBAN} does not exist")
                return
            
            res = self._users[IBAN].update_info(name=name, email=email, ph_num=ph_num, old_pin=old_pin, new_pin=new_pin)
            
            print(res["message"])
            
            if res["status"] == 200:
                self._data_access.update_user(self._users[IBAN])

    def get_user_count(self):
        return len(self._users)
    
    def user_exists(self, IBAN):
        if IBAN in self._users:
            return True
        return False
    
    