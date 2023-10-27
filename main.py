import os
import sys
from sys import stdin, stdout
from file_spellchecker import FileSpellchecker
from interactive_spellchecker import InteractiveSpellchecker
from pathlib import Path


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_options(options):
    if options:
        stdout.write(f'Найдено ошибок: {len(options)} ' + '\n')
        for word in options:
            stdout.write(f'Ошибка в слове "{word}".'
                         f'Возможно Вы имели в виду:' + '\n')
            for option in options[word]:
                stdout.write(f'    {option}' + '\n')
    stdout.write("Ошибок нет. Все корректно." + '\n')
    return



def print_mode_selection():
    stdout.write('Нажмите 1, а затем Enter, '
                 'если хотите проверить слова в файле' + '\n')
    stdout.write('Нажмите 2, а затем Enter, '
                 'если хотите просто вводить слова' + '\n')
    stdout.write('Введите exit, а затем нажмите Enter, '
                 'если хотите завершить работу программы' + '\n')


def execute_command(command):
    while command != '1' and command != '2' and command != 'exit':
        stdout.write('\r'
                     + 'Неизвестная команда, попробуйте еще раз'
                     + '\n')
        command = input().rstrip('\n')
    if command == '1':
        stdout.write('Введите название файла:' + '\n')
        file = input().rstrip('\n')
        path = Path(file)
        stdout.write('\r' + "Идет проверка...")
        spellchecker = FileSpellchecker(path)
        options = spellchecker.get_options()
        stdout.write('\r')
        print_options(options)
    elif command == '2':
        stdout.write('Введите текст:' + '\n')
        text = input().rstrip('\n').lower()
        stdout.write('\r' + "Идет проверка...")
        spellchecker = InteractiveSpellchecker(text)
        options = spellchecker.get_options()
        stdout.write('\r')
        print_options(options)
    elif command == 'exit':
        exit(0)


def execute_menu_command(menu_command):
    while menu_command != 'да' and menu_command != 'нет':
        sys.stdout.write('\r'
                         + 'Неизвестная команда, попробуйте еще раз'
                         + '\n')
        menu_command = input().rstrip('\n')
    if menu_command == 'да':
        clear()
        print_mode_selection()
    elif menu_command == 'нет':
        exit(0)


def main():
    stdout.write('Добро пожаловать в SpellChecker!' + '\n')
    print_mode_selection()
    for command in stdin:
        execute_command(command.rstrip('\n'))
        sys.stdout.write('Выйти в главное меню?'
                         + '\n'
                         + 'Введите "да",'
                           'если хотите'
                         + '\n'
                         + 'Введите "нет",'
                           'если хотите завершить работу программы'
                         + '\n')
        menu_command = input().rstrip('\n')
        execute_menu_command(menu_command)


if __name__ == "__main__":
    main()
