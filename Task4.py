n=int(input())
string = ''
while n > 0:
    string+=str(n%2)
    n//= 2
print(string[::-1])
