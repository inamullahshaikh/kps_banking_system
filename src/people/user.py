from .person import Person
import re

def is_IBAN(text):
    pattern = r"^PKABCC\d{16}$"
    return bool(re.search(pattern, text))

def is_PIN(text):
    pattern = r"^\d{4}$"
    return bool(re.search(pattern, text))

class User(Person):
    def __init__(self, name, email, ph_num, IBAN, PIN, Balance=0):
        super().__init__(name, email, ph_num)
        self._IBAN = IBAN
        self._PIN = PIN
        self._Balance = Balance
        self._logged_in = False

    @property
    def IBAN(self):
        return self._IBAN

    @property
    def PIN(self):
        return self._PIN

    @property
    def Balance(self):
        return self._Balance

    @property
    def Logged_IN(self):
        return self._logged_in

    @IBAN.setter
    def IBAN(self, val):
        if not self._logged_in:
            return {"status": 403, "message": f"User with IBAN {self._IBAN} is not logged in"}
        if is_IBAN(val):
            self._IBAN = val
            return {"status": 200, "message": "IBAN updated successfully"}
        return {"status": 400, "message": "Invalid IBAN format"}

    @PIN.setter
    def PIN(self, old_pin, val):
        if not self._logged_in:
            return {"status": 403, "message": f"User with IBAN {self._IBAN} is not logged in"}
        if old_pin == self._PIN:
            if is_PIN(val):
                self._PIN = val
                return {"status": 200, "message": "PIN updated successfully"}
            return {"status": 400, "message": "Invalid new PIN"}
        return {"status": 403, "message": "Old PIN does not match"}

    @Balance.setter
    def Balance(self, val):
        if not self._logged_in:
            return {"status": 403, "message": f"User with IBAN {self._IBAN} is not logged in"}
        if isinstance(val, (int, float)):
            self._Balance = val
            return {"status": 200, "message": "Balance updated successfully"}
        return {"status": 400, "message": "Invalid balance amount"}

    @Logged_IN.setter
    def Logged_IN(self, val):
        if isinstance(val, bool):
            self._logged_in = val
            return {"status": 200, "message": "Login status updated"}
        return {"status": 400, "message": "Invalid login status"}

    def login(self, iban, pin):
        if self._IBAN == iban:
            if self._PIN == pin:
                self._logged_in = True
                return {"status": 200, "message": f"Login successful for IBAN {self._IBAN}"}
            return {"status": 401, "message": f"Invalid PIN for IBAN {self._IBAN}"}
        return {"status": 404, "message": f"IBAN {iban} not found"}
    def match_pin(self, PIN):
        print(self.PIN)
        print(PIN)
        if str(self.PIN).strip() == str(PIN).strip():
            return {"status": 200, "message": f"PIN matched for IBAN {self._IBAN}"}
        else:
            return {"status": 401, "message": f"Invalid PIN for IBAN {self._IBAN}"}

    def logout(self):
        if self._logged_in:
            self._logged_in = False
            return {"status": 200, "message": f"Logged out successfully for IBAN {self._IBAN}"}
        return {"status": 400, "message": f"User with IBAN {self._IBAN} is not logged in"}


    def deposit(self, val):
        if not self._logged_in:
            return {"status": 403, "message": f"User with IBAN {self._IBAN} is not logged in"}
        if isinstance(val, (int, float)) and val > 0:
            self._Balance += val
            return {"status": 200, "message": f"Deposited {val}. Balance: {self._Balance}"}
        return {"status": 400, "message": "Invalid deposit amount"}
    
    def forced_deposit(self, val):
        if isinstance(val, (int, float)) and val > 0:
            self._Balance += val
            return {"status": 200, "message": f"Deposited {val}. Balance: {self._Balance}"}
        return {"status": 400, "message": "Invalid deposit amount"}

    def withdraw(self, val):
        if not self._logged_in:
            return {"status": 403, "message": f"User with IBAN {self._IBAN} is not logged in"}
        if isinstance(val, (int, float)) and val > 0:
            if val <= self._Balance:
                self._Balance -= val
                return {"status": 200, "message": f"Withdrew {val}. Balance: {self._Balance}"}
            return {"status": 402, "message": "Insufficient funds"}
        return {"status": 400, "message": "Invalid withdrawal amount"}
    def __str__(self):
        return f"IBAN: {self._IBAN}\nName: {self.name}\nEmail: {self.email}\nContact number: {self.phone_number}\nBalance: {self._Balance}\n" if self.Logged_IN else f"User with IBAN {self._IBAN} is not logged in"
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "ph_num": self.phone_number,
            "IBAN": self._IBAN,
            "PIN": self._PIN,
            "Balance": self._Balance
        }

