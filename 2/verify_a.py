

def verify_a(text):
    cont = 0
    for i in range(len(text)):
        
        if text[i].lower() == 'a' or text[i].lower() == 'ã':
            cont += 1
    if cont > 0:
        return f'A letra a existe no texto, e aparece {cont} vezes'
    return 'A letra a não aparece no texto'


print(verify_a('ana banana comeu banana'))
