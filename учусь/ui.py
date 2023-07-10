from logger import input_data, print_data, del_data, rebuild_data

def interface():
    print('Добрый день! Это бот-помошник.\n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные\n'
          '3 - Удалить данные\n'
          '4 - Изменить данные')

    command = int(input('Ваш выбор: '))
    while command < 1 or command >4:
        command = int(input('Ошибка! Попробуйте еще раз! Ваш выбор: '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        del_data()
    else:
        rebuild_data()