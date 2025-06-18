#1)
#a)
for i in range(1, 101):
    print(i)
print("\n")

#b)
for i in range(100, -1, -1):
    print(i)
print("\n")

#c)
for i in range(2, 101, 2):
    print(i)
print("\n")

#d)
for i in range(1, 101, 2):
    print(i)
print("\n")

#e)
soma = 0
for i in range(1, 101):
    soma += i

print(soma)
print("\n")

#g)
X = int(input("Informe um valor inicial(X): "))
Y = int(input("Informe um valor final(Y) maior do que o inicial(X): "))
if(X > Y):
    print("O valor inicial não pode ser maior que o valor final!")
soma = 0 
for i in range (X, Y+1):
    soma += i
print(soma)