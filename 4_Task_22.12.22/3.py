#Число трибоначи. Есть последовательность состоящая из 3 жлементов 0 1 1, сумма равна двум. Принцип работы трибоначи заключается в переносе чисел,
#то есть, если будет n=5, то сначала возмем n=4, оно равно 1 1 2, то есть мы перенесли индексы на 1 влево, сумма n=3 стала числом в последовательности.
def tribonacci(self, n: int) -> int:
    mas = [0, 1, 1]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    for i in range(2, n):
        mas.append(mas[-1] + mas[-2] + mas[-3])
    return mas[-1]