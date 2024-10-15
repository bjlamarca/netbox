

def format_phone(number):
    if len(number)==10:
        return '({}) {}-{}'.format(number[:3],number[3:6], number[6:])
    elif len(number)==7:
        return '{}-{}'.format(number[:3],number[3:])
    else:
        return number

if __name__ == '__main__':
    print(format_phone('7075'))