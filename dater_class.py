from datetime import timedelta


class Dater:
    @staticmethod
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)
    

    @classmethod    
    def adjust_for_weekend(cls, birthday):
        if birthday.weekday() >= 5:
            return cls.find_next_weekday(birthday, 0)
        return birthday
    
    @staticmethod
    def date_to_string(date):
        return date.strftime("%d.%m.%Y")