from file_functions import *
from dir_functions import *


def main():
    folder = "folder"
    if not os.path.isdir(folder):
        os.mkdir(folder)

    while True:
        print("1) Создание папки (с указанием имени)")
        print("2) Удаление папки по имени")
        print("3) Перемещение между папками (в пределах рабочей папки)")
        print("4) Создание пустых файлов с указанием имени")
        print("5) Запись текста в файл")
        print("6) Просмотр содержимого текстового файла")
        print("7) Удаление файлов по имени")
        print("8) Копирование файлов из одной папки в другую")
        print("9) Перемещение файлов")
        print("10) Переименование файлов")
        print("0) Завершение работы\n")
        print(f"Вы находитесь в папке {folder}\n")

        integer = int(input("Введите число от 0 до 10: "))
        while integer > 10 or integer < 0:
            integer = int(input("Введите число от 0 до 10: "))

        if integer == 0:
            break

        if integer == 1:
            dir_name = input("Введите название папки для создания: ")
            make_dir(os.path.join(folder, dir_name))

        if integer == 2:
            dir_name = input("Введите название папки для удаления: ")
            remove_dir(os.path.join(folder, dir_name))

        if integer == 3:
            dir_name = input("Введите название папки для перемещения: ")
            if dir_name == "":
                folder = "folder"
            elif dir_name == ".." and folder != "folder":
                folder = os.path.dirname(folder)
            else:
                folder = os.path.join(folder, dir_name)

        if integer == 4:
            file_name = input("Введите название файла для создания: ")
            make_file(os.path.join(folder, file_name))

        if integer == 5:
            file_name = input("Введите название файла для добавления текста: ")
            text = input("Введите текст: ")
            add_text(os.path.join(folder, file_name), text)

        if integer == 6:
            file_name = input("Введите название файла для просмотра: ")
            read_file(os.path.join(folder, file_name))

        if integer == 7:
            file_name = input("Введите название файла для удаления: ")
            remove_file(os.path.join(folder, file_name))

        if integer == 8:
            file_name = input("Введите название файла для копирования: ")
            dir1 = input("Введите исходную папку: ")
            dir2 = input("Введите конечную папку: ")
            copy_file(file_name, os.path.join(folder, dir1), os.path.join(folder, dir2))

        if integer == 9:
            file_name = input("Введите название файла для перемещения: ")
            dir1 = input("Введите исходную папку: ")
            dir2 = input("Введите конечную папку: ")
            move_file(file_name, os.path.join(folder, dir1), os.path.join(folder, dir2))

        if integer == 10:
            file_name = input("Введите исходное название файла: ")
            file_name2 = input("Введите новое название файла: ")
            rename_file(os.path.join(folder, file_name), os.path.join(folder, file_name2))


if __name__ == "__main__":
    main()