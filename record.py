from phone import Phone
from name import Name

class Record:


    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

    def add_phone(self, number):
        self.phones.append(Phone(number))


    def remove_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                self.phones.remove(phone)


    def edit_phone(self, previous_number, new_number):
        for phone in self.phones:
            if phone.number == previous_number:
                phone.number = new_number


    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone