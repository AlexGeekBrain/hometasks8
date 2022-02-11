import re


def email_parse(email_address):
    r_email = re.findall(r'(^\w+)@((\w+)\.(\w+))$', email_address)
    if not r_email:
        raise ValueError(f'wrong email: {email_address}')
    return dict(zip(['username', 'domain'], r_email[0]))


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
