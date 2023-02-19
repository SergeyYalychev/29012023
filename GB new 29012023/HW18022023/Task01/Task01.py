print('Введие количество арбузов')
n = int(input())
print('Введие вес арбузов через пробел')
if n < 2 :
    print('Ooops!')
else:
    list = list(map(int,input().split()))
    list.sort()
    print(list[0],list[-1])