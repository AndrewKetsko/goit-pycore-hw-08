from collections import UserDict
from datetime import datetime
from record_class import Record
from dater_class import Dater
from typing import TypeVar

T=TypeVar('T',bound='Record')

class AddressBook(UserDict[str,T]):

    def __str__(self):
        list=''
        for record in self.data.values():
            list+=f'{record.name}: {[record.value for record in record.phones]}\n'
        return list
    
    def add_record(self,record:Record)->None:
        self.data[record.name.value]=record

    def find(self,name:str)->Record|None:
       return self.data.get(name)
    
    def delete(self,name:str)->None|str:
        try:
            del self.data[name]
        except KeyError:
            return f'Name {name} is not in your phonebook'
        
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today()

        for user in self.data.values():
            if not user.birthday:
                continue
            birthday_this_year = datetime.strptime(user.birthday.value,'%d.%m.%Y').replace(year=today.year)

            if birthday_this_year<today:
                birthday_this_year=birthday_this_year.replace(year=today.year+1)
            
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year=Dater.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = Dater.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": user.name.value, "birthday": congratulation_date_str})

        return f'upcoming birthdays: {upcoming_birthdays}'
