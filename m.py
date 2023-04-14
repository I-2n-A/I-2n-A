def fibonaci(n): 
    if n in (1, 2): 
        return 1 
    return fibonaci(n - 1) + fibonaci(n - 2) 
def vivod(n): 
    for i in range(1,n): 
        print(fibonaci(i),end = " ") 
def chast(n): 
    i=1 
    while (fibonaci(i)<n): 
        print(fibonaci(i),end = " ") 
        i=i+1 
print('Введите требуемую операцию:') 
print('1-вывод конкретного элемента') 
print('2-вывод всех элементов до заданного') 
print('3-вывод части последовательности,значение последнего элемента которой не превосходит заданного') 
a=int(input()) 
print('Введите номер элемента') 
n=int(input()) 
slovar={1:print(fibonaci(n)),2:vivod(n),3:chast(n)}
slovar.get(a)