var = input().rstrip()

if var[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' or var[len(var)-1] == '_' or '__' in var:
    newvar = 'Error!'
elif var.find('_') == -1: # java형이면 (_가 없으면)
    newvar = ''
    for i in var:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            newvar += '_'
            newvar += i.lower()
        else:
            newvar += i
else:
    newvar = var.split('_')
    newvar = ' '.join(newvar)
    newvar = newvar.title()
    newvar = newvar.split()
    newvar = ''.join(newvar)
    newvar = newvar[0].lower() + newvar[1:]
    for i in var: #c++형인데 대문자가 존재하면
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            newvar = 'Error!'
            break

print(newvar)