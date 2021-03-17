import re


def email_parse(email_ad):
    dict1 = {}
    mail1 = re.compile(r'[a-z0-9]+@')
    mail2 = re.compile(r'([@][a-z]+[.]ru)')
    value1 = mail1.findall(email_ad)
    value2 = mail2.findall(email_ad)
    if value1 == [] or value2 == []:
        raise ValueError(f'неверное значение {email_ad}')
    else:
        dict1['username'] = value1[0][:-1]
        dict1['domain'] = value2[0][1:]
        print(dict1)


email_parse(input('Введите адрес электронной почты: '))
