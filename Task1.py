print("введите длину массива: ")
x=int(input())
mas = []
sum=0
for i in range(x):
   print("Введите элемент массива: ")
   mas.append(int(input()))
for i in range(1,x,2):
   sum=sum+mas[i]
print(mas)
print(sum)