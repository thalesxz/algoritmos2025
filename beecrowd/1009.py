
linha1 = input().split()
codigo1 = int(linha1[0])
numero1 = int(linha1[1])
valor_unitario1 = float(linha1[2])

linha2 = input().split()
codigo2 = int(linha2[0])
numero2 = int(linha2[1])
valor_unitario2 = float(linha2[2])

total = (numero1 * valor_unitario1) + (numero2 * valor_unitario2)

print(f"VALOR A PAGAR: R$ {total:.2f}")