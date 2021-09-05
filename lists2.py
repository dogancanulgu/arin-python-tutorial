# cities = ['tokyo', 'madrid', 'londra', 'kiev']

# # print(cities.index('madrid'))
# # print('ankara' in cities)

# for city in cities:
#     print(f'Gezilen şehir: {city}')
# print('Gezilecek şehir kalmadı')

# str_cities = 'tokyo, madrid, kiev'
# my_list = str_cities.split(', ')
# print(my_list)

# str_email = 'arinyazilim@gmail.com'
# my_list2 = str_email.split('@')
# print(my_list2)

# for number in range(2,21,2):
#     print(number)

# numbers = list(range(1,11))
# print(numbers)

# numbers = [number for number in range(1,11)]
# print(numbers)

cities = ['izmir', 'ankara', 'istanbul']
print(cities)
# cities2 = cities
cities2 = cities[:]
print(cities2)
cities.append('artvin')
print(cities)
print(cities2)
