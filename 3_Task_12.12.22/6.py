#Сложность - O(n)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    stock=head #статичное значение, которое идет по каждому элементу
    speed=head #значение через один элемент
    while stock!=None and speed.next!=None: #Есть ли вообще какая-либо последовательность чисел
        stock=speed.next #перезаписываем следущий элемент последовательности в эту переменную
        speed=speed.next.next #перезаписываем в эту переменную элемент через один
        if stock==speed: #если элеметы стали равны, то цикл есть и выводим True
            return True
    return False