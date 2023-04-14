
from tabulate import tabulate 
print("https://drive.google.com/file/d/1CjrWBNfdt3YSPp2ti1AZo7fV5yO1EUs4/view")
print("https://pypi.org/project/pip/")
def out_red(text):
    print("\033[34m{}".format(text))
out_red("«Game Over»")

def out_red(text):
    print("\033[35m{}".format(text))
out_red("Введите свое Имя:")
im = input()
out_red("Введите свое Фамилию:")
fam = input()
out_red("Введите свое Отчество:")
otch = input()
print ("Введите дату рождения:")
date = input()
print ("Введите город:")
gorod = input() 
print(tabulate([[im, fam, otch, 18,gorod,]], headers=['Name','surname','patronymic ', 'Age','City',], tablefmt='orgtbl'))

def out_red(text):
    print("\033[38m{}".format(text))
out_red("Введите слова-рифмы через энтер:")
one = input()
two = input()
print ('Висит плакат в мышиной', one)
print("«Страшнее кошки зверя нет».")
print("Но, не боясь, за хлебной", two)
print("Спешит мышонок на паркет")
