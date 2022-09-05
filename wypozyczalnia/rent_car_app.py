PATH_TO_CARS = 'files/'
ALL = 'files/all.txt'
RENTED = 'files/rented.txt'
NOT_RENTED = 'files/not_rented.txt'
from car import *

def load_file(file):
    #otworzenie plików w folderze files
    with open(file) as f:
        return f.read()


def create_menu():
    main_db = {}
    cars = load_file(ALL)
    cars_list = list(cars.replace('\n', ''))
    for car_num in cars_list:
        if car_num:
            car = {}
            car_content = load_file(PATH_TO_CARS + car_num + '.txt')
            rows = list(car_content.split('\n'))
            inner_dict_key = ''

            for record in rows:
                if record:
                    key, value = record.split('=')
                    if not value:
                        inner_dict_key = key
                        car[key] = {}
                    elif key[0] == ' ' and inner_dict_key:
                        key = key.strip()
                        car.get(inner_dict_key).update({key: value})
                    else:
                        car[key] = value
                        inner_dict_key = ''

        main_db[car_num] = car
    return main_db


def print_head():
    #Głowne menu
    print('*'*75)
    print()
    print('Witamy w katalogu sportowych samochodów!'.upper())
    print()
    print('*'*75)


def print_menu(menu):
    #Wyświetla menu
    print()
    for item in menu:
        print(item, end='   ')
    print()
    print()
    print('*'*75)


def print_selected_cars(main_db, cars_list):
    #Wyświetla katalog samochodów
    template = '''{}
| {:^12} | {:^12} | {:^12} | {:^12} | {:^12} |
| {:^12} | {:^12} | {:^12} | {:^12} | {:^12} |'''
    input_for_print = create_selection_for_print(main_db, cars_list)
    star_row = '*'*75
    for row in input_for_print:
        print(template.format(star_row, *row))
    print(star_row)


def create_selection_for_print(main_db, cars_list):
    '''
    Tworzy tabele dostępnych samochodów
    '''
    input_for_print = []
    row_key = ['ID']
    for car in cars_list:
        row = [car]
        for key, value in main_db[car].items():
            if isinstance(value, dict):
                for key_inner, value_inner in value.items():
                    if not input_for_print:
                        row_key.append(key_inner)
                    row.append(value_inner)
            else:
                if not input_for_print:
                    row_key.append(key)
                row.append(value)
        input_for_print.append(row)
    input_for_print = [row_key] + input_for_print
    return input_for_print


main_db = create_menu()
cars_list = list(main_db)
create_selection_for_print(main_db, cars_list)


def choose_car():
    #Użytkownik wybiera ID samochodu, który chcę wypożyczyc
    while True:
        ID = input('Wybierz numer samochodu, który chcesz wypożyczyć: ')
        print()
        if ID.lower() == 'q':
            return
        elif ID in load_file(NOT_RENTED):
            return ID
        else:
            if ID in load_file(RENTED):
                print('Samochód nie jest dostępny')
            else:
                print('Zły wybór, spróbuj ponownie lub wpisz Q aby wyjść.')
            not_rented = load_file(NOT_RENTED).strip().replace('\n', ', ')
            print('Możesz wypożyczyć te samochody: {}\n'.format(not_rented))


def return_car():
    #Użytkownik wybiera ID samochodu, który chce oddać do wypożyczalni
    #Gdy użytkownik wybierze złe ID, program wyrzuca liste wypożyczonych aut

    while True:
        ID = input('Wybierz numer samochodu, który chcesz oddać do wypożyczalni: ')
        print()
        if ID.lower() == 'q':
            return
        elif ID in load_file(RENTED):
            return ID
        else:
            print('Zły wybór, spróbuj ponownie lub wpisz Q aby wyjść.')
            rented = load_file(RENTED).strip().replace('\n', ', ')
            print('Możesz oddać te samochody: {}\n'.format(rented))


def write_car_to_file(ID, file):
   #wpisuje id samochodu do pliku rented
   #po wypozyczeniu auta ID samochodu trafia do pliku tekstowego rented i nie moze byc
   #ponownie wypozyczone
    with open(file) as f:
        content = f.read()
    content = list(content.strip().replace('\n', ''))
    content.append(ID)
    content.sort()
    content = '\n'.join(content)
    with open(file, 'w') as f:
        f.write(content)


def del_car_from_file(ID, file):
   #usuwa id samochodu z pliki rented(jesli oddalismy samochod do wypozyczalni automatycznie ten samochod jest usuwany z pliku rented)
    with open(file) as f:
        content = f.read()
    content = content.replace(ID, '').replace('\n\n', '\n')
    with open(file, 'w') as f:
        f.write(content)


def main():
    print_head()
    main_db = create_menu()
    #glowna klasa po wlaczeniu programu uzytkownik za pomoca cyfr obsluguje menu
    while True:
        menu = ['1 - Pokaż wszystkie', 
                '2 - Wypożycz auto', '3 - Zwróć auto', '4 - Wyjdź']
        print_menu(menu)
        choice = input('Wybierz: '.upper())
        print()

        # pokazuje tabele wszystkich aut
        if choice == '1':
            print('Zestawienie wszystkich samochodów:'.upper())
            cars_list = list(main_db)
            print_selected_cars(main_db, cars_list)
            print()


        # wypozycz auto
        elif choice == '2':
            ID = choose_car()
            if ID:
                write_car_to_file(ID, RENTED)
                del_car_from_file(ID, NOT_RENTED)
                print('Gratulacje wybrałeś auto: {}'.upper().format(ID))
            print()

        # zwroc samochod
        elif choice == '3':
            ID = return_car()
            if ID:
                write_car_to_file(ID, NOT_RENTED)
                del_car_from_file(ID, RENTED)
                print('Dziękuje ci za oddanie auta {}'.upper().format(ID))
            print()

        # wyjscie z programu
        elif choice == '4':
            print('Dziękujemy za skorzystanie z naszych usług Do zobaczenia!'.upper())
            break
            print()

        # zły wybor
        else:
            print('Twój wybór jest błędny'.upper())
            print()


main()


