def existe_subconjunto(numeros, n, alvo):
    # Caso base: se o alvo for 0, encontramos um subconjunto
    if alvo == 0:
        return True
    # Se não há mais elementos e o alvo não foi atingido
    if n == 0 and alvo != 0:
        return False

    # Se o último número for maior que o alvo, ignora ele
    if numeros[n - 1] > alvo:
        return existe_subconjunto(numeros, n - 1, alvo)

    # Duas possibilidades:
    # 1️⃣ Inclui o número atual
    # 2️⃣ Não inclui o número atual
    return (existe_subconjunto(numeros, n - 1, alvo) or
            existe_subconjunto(numeros, n - 1, alvo - numeros[n - 1]))


# Programa principal
numeros = [3, 2, 7, 1]
alvo = 6
n = len(numeros)

if existe_subconjunto(numeros, n, alvo):
    print(f"Existe um subconjunto com soma igual a {alvo}")
else:
    print(f"Não existe subconjunto com soma igual a {alvo}")