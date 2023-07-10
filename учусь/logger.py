from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные? \n\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')

    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')
    
    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 Вариант: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i

        print(''.join(data_list))

    print('2 Вариант: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
                

def del_data():
    var = int(input(f'\nВ каком списке удалить данные? \n'))
    x = int(input(f'Нужно удалить данные по номеру: \n'))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list()
            j = 0
            for i in range(len(data)):
                if data[i] == '\n':
                    data_list.append(''.join(data[j:i]))
                    j = i
                
            for i in range(len(data_list)):
                if i+1 == x:
                    list1  = data_list[0:i] + data_list[i+1:]
                    f = open('data_first_variant.csv', 'w', encoding='utf-8')
                    f.write(''.join(list1))
                    f.close()
                    
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            
            for i in range(len(data)):
                if i+1 == x:
                    list1  = data[0:i] + data[i+2:]
                    f = open('data_second_variant.csv', 'w', encoding='utf-8')
                    f.write(''.join(list1))
                    f.close()
                                                                
def rebuild_data():
    var = int(input(f'\nВ каком списке заменить данные? \n'))
    x = int(input(f'Нужно заменить данные по номеру: \n'))
    name, surname, phone, adress = input_user_data()
    if var == 1:
        list_1 = (f'\n{name}\n'
                  f'{surname}\n'
                  f'{phone}\n'
                  f'{adress}\n')

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            data_list = list()
            j = 0
            for i in range(len(data)):
                if data[i] == '\n':
                    data_list.append(''.join(data[j:i]))
                    j = i
               
            for i in range(len(data_list)):
                if i+1 == x:
                    list1  = data_list[0:i]
                    list1.append(list_1)
                    list1 += data_list[i+1:]
                    f = open('data_first_variant.csv', 'w', encoding='utf-8')
                    f.write(''.join(list1))
                    f.close()
                    
    elif var == 2:
        list_2 = (f'\n{name};{surname};{phone};{adress}\n')
    
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
            
            for i in range(len(data)):
                if i+1 == x:
                    list1  = data[0:i] 
                    list1.append(list_2)
                    list1 += data[i+2:]
                    f = open('data_second_variant.csv', 'w', encoding='utf-8')
                    f.write(''.join(list1))
                    f.close()