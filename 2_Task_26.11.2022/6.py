#Сложность программы - O(n)
#Код под первое условие
nums=[2, 3, 2] #список подаваемый на вход по условию
s=[] #список, куда заносятся валидные значения
if len(nums) <= 3: #сразу можно сделать проверку на последовательность из трех домов, т.к дома стоят по кругу и мы в любом случае не сможем ограбить более 1 дома, следовательно если грабим дом, то только с максимальным значением.
    print(max(nums)) #выводим значение максимального дома
for i in range(0, len(nums)): #проходимся по индексам списка от нуля до длины списка
    if i==nums[-1]: #если текущее значение равно последнему элементу списка, то добавляем текущий элемент и элемент через него
        s.append(i)
        s.append(nums[i+1])
print(sum(s))


#Код для второго условия
nums=[1, 2, 3, 1]
s=[]
if len(nums) <= 3:
    print(max(nums))
for i in range(0, len(nums)):
    if i==nums[-1]:
        s.append(i)
        s.append(nums[i+1])
print(sum(s))
