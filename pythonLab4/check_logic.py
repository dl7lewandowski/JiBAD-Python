import string

def check_expresion(exp):
    legal_symbol = ['(', '~',]  # lepszy do tego byłby zbiór + liczba mnoga by się przydała
    values = list(string.ascii_lowercase) + ['1', '0']
    legal_symbol += values
    operators = ['|', '&']
    count = 0
    for i in range(len(exp)):
        if count == 0 and ')' in legal_symbol:
            legal_symbol.remove(')')
        if exp[i] not in legal_symbol and exp[i] != ' ':    # a gdyby dodać spację do legal_symbol?
            return False
        if exp[i] == '(':
            legal_symbol = ['~', '('] + values
            count += 1
        elif exp[i] == ['~']:
            legal_symbol = ['~', '('] + values
        elif exp[i] in values:
            legal_symbol = operators + [')']
        elif exp[i] in operators:
            legal_symbol = values + ['~']   # a nawias?
        elif exp[i] == ')':
            legal_symbol = operators
            count -= 1
        elif exp[i] == ' ':
            pass
    if count == 0 and exp[-1] not in ['~', '|', '&', '(']:
        return True
    return False

# sprawdzenie poprawnosci wyrazenia
print(check_expresion('a'))
print(check_expresion('a|b'))
print(check_expresion('a & b | a'))
print(check_expresion('~~a'))
print(check_expresion('~(a|c)'))
print(check_expresion('(a)'))
print('----------------------------------')
# niepoprawne wyrazenie
print(check_expresion('~'))
print(check_expresion('a|'))
print(check_expresion('A|B'))
print(check_expresion('a|&b'))
print(check_expresion('b~'))
print(check_expresion('(a|b'))
print(check_expresion('a|b)'))


print(check_expresion('a|(b|c)'))
print(check_expresion('((a))'))
