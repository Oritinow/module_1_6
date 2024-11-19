my_dict = {'Anton': 1999, 'Egor': 1998, 'Nikita': 2000}
print(my_dict)
print(my_dict['Anton'])
#print(my_dict['Artur'])
my_dict['Igor'] = 2001
my_dict['Irina'] = 2002
print(my_dict)
del my_dict['Irina']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, (1, 2, 3), 'Apple'}
print(my_set)
my_set.add('Pineapple')
my_set.add(447)
print(my_set)
my_set.remove(447)
print(my_set)
