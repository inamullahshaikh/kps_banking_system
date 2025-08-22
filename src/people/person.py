from abc import ABC,abstractmethod
import re

def is_name(text):
    pattern = r"^[A-Za-z ]+$"
    return bool(re.search(pattern, text))

def is_email(text):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.search(pattern, text))

def is_phuonenum(text):
    pattern = r"^\+923\d{9}$"
    return bool(re.search(pattern, text))


class Person(ABC):
    def __init__(self,name,email,ph_num):
        self._name = name
        self._email = email
        self._phone_number = ph_num
    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
    @property
    def phone_number(self):
        return self._phone_number
    
    @name.setter
    def name(self, val):
        if val and isinstance(str, val):
            if(is_name(val)):
                self._name = val
            else:
                print("Enter correct name(no digits or special characters allowed)")
    @email.setter
    def email(self, val):
        if val and isinstance(str, val):
            if(is_email(val)):
                self._email = val
            else:
                print("Enter correct email(Format: abc@abc.com)")
    @phone_number.setter
    def phone_number(self, val):
        if val and isinstance(str, val):
            if(is_phuonenum(val)):
                self._phone_number = val
            else:
                print("Enter correct phone number(Format: +923XXXXXXXXX")

    @abstractmethod
    def __str__(self):
        pass
    

