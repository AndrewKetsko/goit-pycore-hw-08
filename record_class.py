from name_class import Name
from phone_class import Phone
from birthday_class import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones=[]
        self.birthday=None

    # реалізація класу
    def __phonelist_from_instancelist(self):
        return [phone.value for phone in self.phones]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone_str:str)->None:
        phone=Phone(phone_str)
        if phone_str not in self.__phonelist_from_instancelist():
            self.phones.append(phone)

    def remove_phone(self, phone_str:str)->None:
        try:
            index=self.__phonelist_from_instancelist().index(phone_str) #raise ValueError if not found
            self.phones.pop(index)
        except ValueError:
            pass

    def find_phone(self,phone_str:str)->Phone|None:
        try:
            index=self.__phonelist_from_instancelist().index(phone_str) #raise ValueError if not found
            return self.phones[index] 
        except ValueError:
            return None

    def edit_phone(self, old_phone_str:str, new_phone_str:str)->None:
        new_phone=Phone(new_phone_str)
        if new_phone_str in [phone.value for phone in self.phones]:
            self.remove_phone(old_phone_str)
            return
        index=self.__phonelist_from_instancelist().index(old_phone_str) #raise ValueError if not found
        self.phones[index]=new_phone

    def add_birthday(self, value):
        self.birthday=Birthday(value)

    def show_birthday(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday.value}"
