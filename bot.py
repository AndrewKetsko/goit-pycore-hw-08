from address_book_class import AddressBook
from record_class import Record
from error_decorator import input_error
import pickle

class Bot:
    def __init__(self,filename="addressbook.pkl"):
        self.filename=filename
        self.book=self.load_data()

    def __parse_input(self,command):
        cmd,*args = command.split()
        cmd=cmd.strip()
        return cmd,args
    
    def save_data(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.book,file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()

    @input_error
    def __add_contact(self,args):
        name,phone=args
        record=self.book.find(name)        
        if record:
            record.add_phone(phone)
            return('contact updated')
        record=Record(name)
        record.add_phone(phone)
        self.book.add_record(record)
        return('contact added')

    @input_error
    def __change_contact(self,args):
        name,old_phone, new_phone=args
        record=self.book.find(name)
        if not record:
            raise KeyError
        record.edit_phone(old_phone, new_phone)
        return('contact changed')

    @input_error
    def __show_phone(self,args):
        name=args[0]
        record=self.book.find(name)
        return(str(record))

    @input_error
    def __add_birthday(self,args):
        name,birthday=args
        record=self.book.find(name)
        record.add_birthday(birthday)
        return('birthday added')


    @input_error
    def __show_birthday(self,args):
        name=args[0]
        record=self.book.find(name)
        return record.show_birthday()

    @input_error
    def __birthdays(self):
        return self.book.get_upcoming_birthdays()

    @input_error
    def __show_all(self):
        return str(self.book)

    def main(self):
        self.book=self.load_data()
        print("Welcome to the assistant bot!")
        while True:
            command = input("Enter a command: ").strip().lower()
            if command:
                command,args=self.__parse_input(command)

            match(command):
                case('close'):
                    print("Good bye!")
                    break  
                case('exit'):
                    print("Good bye!")
                    break 

                case('hello'):
                    print("How can I help you?")

                case('add'):
                    print(self.__add_contact(args))

                case('change'):
                    print(self.__change_contact(args))

                case('phone'):
                    print(self.__show_phone(args))

                case('all'):
                    print(self.__show_all())

                case('add-birthday'):
                    print(self.__add_birthday(args))

                case('show-birthday'):
                    print(self.__show_birthday(args))

                case('birthdays'):
                    print(self.__birthdays())

                case(_):
                    print("Invalid command.")

        self.save_data()
