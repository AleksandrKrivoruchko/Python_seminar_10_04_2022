from read_contact import read_contact


def enter_data():
    print('Выберите необходимую операцию:', '1 - ввод данных в формате "Фамилия, Имя, телефон, описание',
          '2 - вывод данных в требуемом формате', '3 - экспорт данных в файл', '4 - завершение работы с модулем',
          sep='\n')

    operation_select = int(input())
    if operation_select == 1:
        soname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        description = input('Введите описание: ')
        new_list = [soname, name, phone_number, description]
        return (new_list)
    elif operation_select == 2:
        print('Выберите формат отображения данных:', '1 - построчно', '2 - в одну строку', sep='\n')
        read_contact()


# print(enter_data())
