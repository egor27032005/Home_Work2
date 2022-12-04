print("введите длину массива: ")
x=int(input())
if x%2==0:
  t=x//2
else:
   t=x//2+1
mas = []
mas2=[]
sum=0
for i in range(x):
   print("Введите элемент массива: ")
   mas.append(int(input()))
for i in range(t):
   mas2.append(mas[i]*mas[-i-1])
print(mas)   
print(mas2)