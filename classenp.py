def existe_subconjunto(numeros, n, alvo):
    
    if alvo == 0:
        return True

    if n == 0 and alvo != 0:
        return False

    if numeros[n - 1] > alvo:
        return existe_subconjunto(numeros, n - 1, alvo)

    return (existe_subconjunto(numeros, n - 1, alvo) or
            existe_subconjunto(numeros, n - 1, alvo - numeros[n - 1]))


numeros = [3, 2, 7, 1]
alvo = 6
n = len(numeros)

if existe_subconjunto(numeros, n, alvo):
    print(f"Existe um subconjunto com soma igual a {alvo}")
else:
    print(f"Não existe subconjunto com soma igual a {alvo}")