# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


file_path = "C:/Users/User/Documents/example.txt"
import os


# def get_file_info(file_path):
#     path, filename = os.path.split(file_path)
#     name, extension = os.path.splitext(filename)
#     return path, name, extension


def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return path, file_name[:-len(file_extension) - 1], "." + file_extension




print(get_file_info(file_path))