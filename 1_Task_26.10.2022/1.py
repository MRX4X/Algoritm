#Общая сложность программы - #O(n**3)
def add(): #создаем функцию add
    a=14 #число, которое изменяем
    c=0 #счетчик
    while a!=0: #пока а не равно нулю, цикл работает #O(n)
        if a%2==0: #проверяем четно ли а #O(n)
            a=a//2 #если а четно, делим на 2
            c+=1 #наращивем счетчик на единицу
        if a%2!=0: #если а не четно #O(n)
            a=a-1 #отнимаем единицу
            c+=1 #наращиваем счетчик
    return c #возвращаем счетчик
print(add()) #выводим значение