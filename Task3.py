print("введите длину массива: ")
x=int(input())
mas = []
min=1
max=0
for i in range(x):
   print("Введите элемент массива: ")
   mas.append(float(input()))
for i in range(x):
   if mas[i]%1<min:
      min=mas[i]%1
   elif mas[i]%1>max:
      max=mas[i]%1
print(round(max-min,1))
