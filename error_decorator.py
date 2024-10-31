def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'Give me actual name please.'
        except IndexError:
            return 'Give me name please.'
    return inner   