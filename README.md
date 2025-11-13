# 📚 Classes de Problemas NP


### 📘Definição:
A **Classe NP (Tempo Polinomial não Determinístico)** é um dos conceitos centrais da Teoria da Complexidade Computacional e pode ser definida como o conjunto de problemas de decisão cuja solução é difícil de resolver, mas fáceis de verificar. Se alguém te der a resposta, você consegue confirmar que ela é correta em **tempo polinomial**.

### 💡 Problema da Soma de Subconjuntos:
Imagine que você quer saber se existe uma combinação de números que some exatamente 10. Em uma lista de 100 números pode ser difícil achar a combinação, mas se alguém achou a combinação, é fácil verificar que ela soma e da o resultado.

### 💻 Código em Python - Subset Sum Problem (versão simples)

```bash
def existe_subconjunto(numeros, n, alvo):
    """
    Verifica se existe um subconjunto dos 'n' primeiros elementos de 'numeros'
    cuja soma seja igual a 'alvo'. 
    Implementação recursiva (sem otimizações).
    """

    # Caso base: se o alvo for 0, existe subconjunto válido (soma vazia)
    if alvo == 0:
        return True

    # Caso base: se não há elementos e o alvo ainda não foi atingido
    if n == 0 and alvo != 0:
        return False

    # Se o último número for maior que o alvo, ignora-o
    if numeros[n - 1] > alvo:
        return existe_subconjunto(numeros, n - 1, alvo)

    # Testa duas possibilidades:
    # 1️⃣ Não incluir o último número
    # 2️⃣ Incluir o último número e reduzir o alvo
    return (existe_subconjunto(numeros, n - 1, alvo) or
            existe_subconjunto(numeros, n - 1, alvo - numeros[n - 1]))


# Lista de números e valor alvo
numeros = [3, 2, 7, 1]
alvo = 6
n = len(numeros)

# Executa a função e exibe o resultado
if existe_subconjunto(numeros, n, alvo):
    print(f"Existe um subconjunto com soma igual a {alvo}")
else:
    print(f"Não existe subconjunto com soma igual a {alvo}")

```

### 📈 Código com 5 melhorias de desempenho
```bash
# Contador de chamadas recursivas (para medir desempenho)
cont = {"chamadas": 0}


def existe_subconjunto(numeros, n, alvo, memo=None):
    """Verifica se há um subconjunto com soma igual a 'alvo'."""

    # (1) Conta chamadas recursivas
    cont["chamadas"] += 1

    # (2) Usa memoization para evitar repetir cálculos
    if memo is None:
        memo = {}
    if (n, alvo) in memo:
        return memo[(n, alvo)]

    # Casos base
    if alvo == 0:
        return True
    if n == 0:
        return False

    # (3) Poda: se a soma total for menor que o alvo, não há solução
    if sum(numeros[:n]) < alvo:
        memo[(n, alvo)] = False
        return False

    # (4) Testa incluir ou não o último número
    if numeros[n - 1] > alvo:
        resultado = existe_subconjunto(numeros, n - 1, alvo, memo)
    else:
        sem_ultimo = existe_subconjunto(numeros, n - 1, alvo, memo)
        com_ultimo = existe_subconjunto(numeros, n - 1, alvo - numeros[n - 1], memo)
        resultado = sem_ultimo or com_ultimo

    # Salva resultado no cache
    memo[(n, alvo)] = resultado
    return resultado


# Lista e alvo
numeros = [3, 2, 7, 1]
alvo = 6

# (5) Ordena a lista para melhorar as podas
numeros.sort()

n = len(numeros)

# Executa e mostra resultado
if existe_subconjunto(numeros, n, alvo):
    print(f"✅ Existe um subconjunto com soma igual a {alvo}")
else:
    print(f"❌ Não existe subconjunto com soma igual a {alvo}")

# Mostra total de chamadas (análise de desempenho)
print(f"📊 Chamadas recursivas: {cont['chamadas']}")


```

### ⚙️ Análise de Complexidade
Tempo de complexidade: O(2ⁿ). Esse crescimento exponencial torna o problema ineficiente para grandes conjuntos - por isso ele pertence à **classe NP**
