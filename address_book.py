from collections import UserDict

class AddressBook(UserDict):

    def __init__ (self, name):
        pass


    def add_record(self, record):
        if record.name.value in self.data:
            raise KeyError(f"This name '{record.name.value}' is already taken by another user. Please choose another name.")
        self.data[record.name.value] = record


    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"No record found with the name '{name}'.")
            return None


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Record with the name '{name}' successfully deleted.")
        else:
            print(f"No record found with the name '{name}'. Deletion not performed.")