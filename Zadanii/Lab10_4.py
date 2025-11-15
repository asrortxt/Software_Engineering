class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('[Unwa force 10 cummons]')
    else:
        print('Yenemuan регистрация')

if __name__ == '__main__':
    name = '12345678910'
    check_name(name)