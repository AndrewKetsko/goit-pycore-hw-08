from field_class import Field


class Phone(Field):
    def __init__(self, value:str):
        if len(value)!=10:
            raise ValueError('phone number must be equel to 10 digit')
        if not value.isnumeric():
            raise ValueError('phone must contain numbers only')
        # assert len(value)!=10, f'phone number must be greater than 10 digit'
        super().__init__(value)