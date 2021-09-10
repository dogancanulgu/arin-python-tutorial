# dersler = ['matematik', 'fizik', 'kimya', 'ingilizce', 'türkçe']
# print(dersler[1].upper())
# print(dersler[4].upper())
# print(dersler[-1].upper())

# print(dersler[1:3])
# print(dersler[:2])

# dersler = ['matematik', ['fizik', 'kimya'], 'ingilizce', 'türkçe']
# print(dersler[1])
# print(dersler[1][0])
# print(dersler[1][1])
# print(dersler[-1])
# print(dersler[len(dersler)-1])
# print(len(dersler))

# dersler.append('tarih')
# print(dersler)

# dersler[len(dersler):] = ['coğrafya']
# print(dersler)

# dersler.insert(0, 'tarih')
# print(dersler)

# dersler.insert(len(dersler), 'coğrafya')
# print(dersler)

# del dersler[1]
# print(dersler)

# dersler.remove('türkçe')
# print(dersler)

# numbers = [8, 4, 5, 1, 6, 9, 2, 7, 3, 10]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

# dersler = [['matematik', 'fizik'], ['kimya', 'ingilizce'], ['türkçe', 'tarih']]
# dersler2 = []
# # dersler2.append(dersler[0][-1])
# # dersler2.append(dersler[1][-1])
# # dersler2.append(dersler[2][-1])
# # print(dersler2)

# for ders in dersler:
#     dersler2.append(ders[-1])

# print(dersler2)

# squares = []
# for num in range(1,11):
#     squares.append(num**2)
# print(squares)

squares = [num**2 for num in range(1,11)]
print(squares)





