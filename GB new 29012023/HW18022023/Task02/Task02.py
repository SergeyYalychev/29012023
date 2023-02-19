print("Введите количество монет")
n = int(input())
k = 0
print('Введите расположение монет где 1 это орёл 0 решка')
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
f = k if k<n/2 else n-k
print(F'Итого необходимо перевернуть {f} монеты')