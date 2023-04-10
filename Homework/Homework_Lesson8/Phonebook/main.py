"""Задача №49.
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Использование функций. Ваша программа
не должна быть линейной"""

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])

def changing_an_entry(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    print()
    show_all_items(filename)
    print()
    id_number = input('Выберите ID записи, которую хотите изменить: ')

    data_array = read_file(filename) 
    
    int_num = int(id_number)
    for i in range(1,len(data_array)):
        if i == int(data_array[int_num][0]): 
            for j in range(4):
                if j == 0: name = 'новую фамилию'
                if j == 1: name = 'новое имя'
                if j == 2: name = 'новое отчество'
                if j == 3: name = 'новый телефон'
                data_array[i][j+1] = input(f'Введите {name}: ')

    write_file(filename, data_array)

def deleting_an_entry(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    print()
    show_all_items(filename)
    print()
    id_number = input('Выберите ID записи, которую хотите удалить: ')

    data_array = read_file(filename) 
    
    int_num = int(id_number)
    for i in range(1,len(data_array)):
        if i == int(data_array[int_num][0]): 
            data_array.pop(i)

    write_file(filename, data_array)
    print('Запись удаленна.')

def search(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename)
    searchWord = input('Введите слово по которому произвести поиск: ')

    for i in range(1,len(data_array)):
        for j in range(4):
            if data_array[i][j+1].replace(' ', '') == searchWord:
                print(*data_array[i])
            
def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    print('5 - Поиск')

    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        changing_an_entry(filename)
    elif user_operation == 4:
        deleting_an_entry(filename)
    elif user_operation == 5:
        search(filename)

filename = 'file.txt'
menu()