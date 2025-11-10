# 📚 Classes de Problemas NP


### 📘Definição:
A **Classe NP (Tempo Polinomial não Determinístico)** é um dos conceitos centrais da Teoria da Complexidade Computacional e pode ser definida como o conjunto de problemas de decisão cuja solução é difícil de resolver, mas fáceis de verificar. Se alguém te der a resposta, você consegue confirmar que ela é correta em **tempo polinomial**.

### 💡 Problema da Soma de Subconjuntos:
Imagine que você quer saber se existe uma combinação de números que some exatamente 10. Em uma lista de 100 números pode ser difícil achar a combinação, mas se alguém achou a combinação, é fácil verificar que ela soma e da o resultado.

### 💻 Código em Python - Subset Sum Problem (versão recursiva)

```bash
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
```

### ⚙️ Análise de Complexidade
Tempo de complexidade: O(2^n). Esse crescimento exponencial torna o problema ineficiente para grandes conjuntos - por isso ele pertence à **classe NP**
