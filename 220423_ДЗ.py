ip = input('Введите IP-адрес для проверки  ').split('.')
print(all(map(lambda n: n.isdigit() and int(n) <= 255, ip)))
