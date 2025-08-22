import json
import os

class DataAccess:
    def __init__(self):
        self._FILE_PATH = "D:/Task 2/src/server/data/user_data.json"
        self._FILE_PATH_1 = "D:/Task 2/src/server/data/bank_data.json"

    def get_current_account(self):
        with open(self._FILE_PATH_1, "r") as f:
            data = json.load(f)
        return data["last_account_number"]

    def increment_account(self):
        with open(self._FILE_PATH_1, "r+") as f:
            data = json.load(f)
            data["last_account_number"] += 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        return data["last_account_number"]

    def load_users_helper(self):
        if not os.path.exists(self._FILE_PATH):
            return []
        with open(self._FILE_PATH, "r") as file:
            return json.load(file)

    def load_users(self):
        users_list = self.load_users_helper()
        return {user["IBAN"]: user for user in users_list}

    def save_users(self, users_list):
        with open(self._FILE_PATH, "w") as file:
            json.dump(users_list, file, indent=4)

    def update_user(self, updated_user, old_IBAN=None):
        users_list = self.load_users_helper()
        for user in users_list:
            if old_IBAN is not None and old_IBAN == user.get("IBAN"):
                user["IBAN"] = updated_user.IBAN
            if user.get("IBAN") == updated_user.IBAN:
                user["name"] = updated_user.name
                user["email"] = updated_user.email
                user["ph_num"] = updated_user.phone_number
                user["PIN"] = updated_user.PIN
                user["Balance"] = updated_user.Balance
                self.save_users(users_list)
                print("User updated successfully!")
                return
        print("User not found!")

    def delete_user(self, IBAN):
        users_list = self.load_users_helper()
        updated_users = [user for user in users_list if user.get("IBAN") != IBAN]
        if len(users_list) == len(updated_users):
            print("User not found!")
            return
        self.save_users(updated_users)
        print("User deleted successfully!")

    def add_user(self, new_user):
        users_list = self.load_users_helper()
        for user in users_list:
            if user["IBAN"] == new_user.IBAN:
                print("User with this IBAN already exists!")
                return
        # Append as dict
        users_list.append({
            "name": new_user.name,
            "email": new_user.email,
            "ph_num": new_user.phone_number,
            "IBAN": new_user.IBAN,
            "PIN": new_user.PIN,
            "Balance": new_user.Balance
        })
        self.save_users(users_list)
        self.increment_account()
        print("User added successfully!")
