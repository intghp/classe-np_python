cont = {"chamadas": 0}

def existe_subconjunto(numeros, n, alvo, memo=None):

    cont["chamadas"] += 1

    if memo is None:
        memo = {}

    if (n, alvo) in memo:
        return memo[(n, alvo)]

    if alvo == 0:
        return True
    if n == 0:
        return False

    if sum(numeros[:n]) < alvo:
        memo[(n, alvo)] = False
        return False

    if numeros[n - 1] > alvo:
        resultado = existe_subconjunto(numeros, n - 1, alvo, memo)
    else:
        sem_ultimo = existe_subconjunto(numeros, n - 1, alvo, memo)
        com_ultimo = existe_subconjunto(numeros, n - 1, alvo - numeros[n - 1], memo)
        resultado = sem_ultimo or com_ultimo

    memo[(n, alvo)] = resultado
    return resultado


numeros = [3, 2, 7, 1]
alvo = 6

numeros.sort()

n = len(numeros)

if existe_subconjunto(numeros, n, alvo):
    print(f"✅ Existe um subconjunto com soma igual a {alvo}")
else:
    print(f"❌ Não existe subconjunto com soma igual a {alvo}")

print(f"📊 Chamadas recursivas realizadas: {cont['chamadas']}")
