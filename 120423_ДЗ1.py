def print_all(*args, sep= ' ', end = '\n',**kwargs):
    args = args + (end, )
    all = sep.join(args)
    return all

p = print_all('1','2','3','4', sep= 'a', end = '!')
print(p)
p = print_all('1','2','3','4', end = '##')
print(p)
p = print_all('1','2','3','4', '5')
print(p)
