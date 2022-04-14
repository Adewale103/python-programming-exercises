#
# list_ = list('abcde')
# print(list_)
#
# name = ['w', 'a', 'l', 'e']
# print(''.join(name))
#
alphabet = list('abcdefghijkl')
# print(alphabet)
# print(alphabet[:])  #slicing
# print(alphabet[::-5]) #reading from the back
# print(alphabet*2)
# alphabet += [1, 2, 3, 4, 5]
# print(alphabet)
# print('j' in alphabet)
# print('q' not in alphabet)

# list_of_lists = [1, 2, [3, 4, 5], 6]
# print(list_of_lists[2])
#
# my_dict = {
#     'name': "Segun",
#     'age': 12,
#     'sex': 'Male',
#     'hobby': ['Python', 'Java'],
#     'is_wife_beater': False
# }
#
# print(len(my_dict))
# for key in my_dict:
#     print(key, '-->', my_dict[key])


new_list = ['segun', 'sege', 'Bayo', "wale"]
#new_list.extend(['paul', 'henry'])    #same thing extend will do (new_list.exend)
#new_list = new_list + ['paul', 'henry']     #same thing extend will do (new_list.exend)
#new_list.append(['Kai', 'jojo'])


new_list.insert(2, 'Tolani')


new_list.insert(len(new_list), 'Ernest')
print(new_list)

print(new_list.pop(3))
print(new_list)

print(new_list.remove('sege'))
print(new_list)      #clear will remove everything

print(new_list.index("wale"))

new_list.reverse()
print(new_list)

new_list.sort(key = len)
print(new_list)




