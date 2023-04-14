def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def vivod(n):
    for i in range(1,n):
        print(fibonacci(i),end = " ")
def chast(n):
    i=1
    while (fibonacci(i)<n):
        print(fibonacci(i),end = " ")
        i=i+1
print('Введите требуемую операцию: 1-вывод конкретного элемента 2-вывод всех элементов до заданного')
print('3-вывод части последовательности,значение последнего элемента которой не превосходит заданного')
a=int(input())
print('Введите номер элемента')
n=int(input())
if (a==1):
    print(fibonacci(n))
if (a==2):
    vivod(n)
if (a==3):
    chast(n)