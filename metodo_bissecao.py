"""
ALGORITMO  MÉTODO DA BISSEÇÃO 
Disciplica: ELEMENTOS DA DIFERENCIAÇÃO COMPUTACIONAL
Alunos(as):
- Franciscleide Lauriano da Silva
- Anderson Rodrigues Silva de Barros
- Jeanne Espíndola Pereira
- Allan Lucas Lages dos Santos
"""

"""
===================== IDEIA DO MÉTODO DA BISSEÇÃO =====================

1) Hipótese-chave (garantia de existência de raiz)
----------------------------------------------------------------------------
Se f é contínua no intervalo fechado [a,b] e f(a)*f(b) < 0, então existe
pelo menos um ponto x* em (a,b) tal que f(x*) = 0. Essa é uma consequência
direta do Teorema do Valor Intermediário (TVI): a função contínua não pode
“pular” de um valor negativo para um positivo sem cruzar o zero no caminho.

2) Ideia central do algoritmo
----------------------------------------------------------------------------
A bisseção explora apenas o sinal de f nos extremos do intervalo:
  - Calcula o ponto médio x = (a + b) / 2.
  - Avalia f(x).
  - Se f(a) e f(x) têm sinais opostos (f(a)*f(x) < 0), então a raiz está
    no subintervalo [a, x], e podemos descartar a metade direita: b ← x.
  - Caso contrário, a raiz está no subintervalo [x, b], e descartamos a
    metade esquerda: a ← x.
Fazendo isso repetidamente, o comprimento do intervalo cai pela metade a
cada passo; logo, “apertamos” a raiz.

3) Critérios de parada (quando interromper)
----------------------------------------------------------------------------
Usaremos dois critérios simultâneos:
  (i) |f(x)| < tol → o valor da função está “suficientemente perto de 0”.
 (ii) (b - a)/2 < tol → o intervalo já é tão pequeno que o erro absoluto
      no ponto médio é menor que tol. (O ponto retornado é o meio do
      intervalo; assim, o erro é no máximo a metade do comprimento atual.)

4) Erro e taxa de convergência
----------------------------------------------------------------------------
Se o intervalo inicial tem comprimento L0 = b0 - a0, após k iterações
o comprimento vale Lk = L0 / 2^k.
Como retornamos o ponto médio, o erro absoluto em relação à raiz x* obedece:
    |x_k - x*| ≤ Lk / 2 = L0 / 2^(k+1).
Portanto, para garantir (b - a)/2 ≤ tol, basta escolher k tal que
    k ≥ ceil( log2( L0 / tol ) ).
Essa é uma convergência linear: a cada passo, o erro “cai pela metade”.

5) Observações práticas
----------------------------------------------------------------------------
- Se f(a) ≈ 0 ou f(b) ≈ 0 já no início (|f| < tol), podemos retornar a/b
  imediatamente: isso evita iterações desnecessárias.
- Se f(a)*f(b) > 0, não há garantia de raiz (pode até haver um número PAR de
  raízes, mas seus sinais se “cancelam” nos extremos), então o método não
  deve prosseguir.
- Usar ‘verbose’ para imprimir as iterações ajuda a estudar a convergência.
- ‘return_history’ armazena as tuplas (k, a, b, x, f(x)), úteis para tabelas
  e gráficos.

===============================================================================================
"""


# Código em python:
from math import cos, e

def bissecao(f, a, b, tol=1e-6, max_iter=100, verbose=True, return_history=False):
    """
    Método da Bisseção para resolver f(x) = 0 em [a, b].

    Parâmetros:
        f                       -> função contínua
        a, b                    -> extremos do intervalo inicial
        tol                     -> tolerância (critério de parada)
        max_iter                -> número máximo de iterações para evitar alto custo computacional (sobrecarga da memória)
        verbose                 -> se True, imprime o andamento
        return_history          -> se True, devolve também uma lista com o histórico

    Retorna:
        raiz                    -> aproximação da raiz
        (raiz, hist)            -> se return_history=True
    """

    # Histórico para estudo/depuração
    history = []

    # Casos de borda: já começamos “em cima” da raiz em a ou b?
    fa = f(a)
    fb = f(b)
    if abs(fa) < tol:
        return (a, history) if return_history else a
    if abs(fb) < tol:
        return (b, history) if return_history else b

    # Pré-condição do método: sinais opostos nos extremos
    if fa * fb > 0:
        raise ValueError("Não há garantia de raiz: f(a) e f(b) têm o mesmo sinal.")

    # Loop principal: a cada passo reduzimos o intervalo pela metade
    for k in range(1, max_iter + 1):
        x = (a + b) / 2.0       # ponto médio
        fx = f(x)

        # Guarda a iteração (k, a, b, x, f(x)) para análise posterior
        history.append((k, a, b, x, fx))

        # Mostra o andamento, se desejado
        if verbose:
            print(f"Iter {k:>3}: a={a:.6f}, b={b:.6f}, x={x:.6f}, f(x)={fx:.6e}")

        # Critérios de parada: valor pequeno da função OU intervalo pequeno
        if abs(fx) < tol or (b - a) / 2.0 < tol:
            return (x, history) if return_history else x

        # Escolha do subintervalo que contém a raiz (pelo sinal)
        if fa * fx < 0:
            # raiz em [a, x] → encurta pela direita
            b = x
            fb = fx
        else:
            # raiz em [x, b] → encurta pela esquerda
            a = x
            fa = fx

    # Se atingiu max_iter sem satisfazer os critérios de parada,
    # devolve o meio do último intervalo como melhor aproximação.
    return ((a + b) / 2.0, history) if return_history else (a + b) / 2.0


# --------------------- EXEMPLOS DE APLICAÇÃO ---------------------

# f(x) = x^2 - x - 1  (número áureo)
def f1(x): 
    return x*x - x - 1
print("Raiz (x^2 - x - 1) ≈", bissecao(f1, 1, 2, tol=1e-6, verbose=False))

# cos(x) = x  → f(x) = cos(x) - x
def f2(x):
    return cos(x) - x
print("Raiz (cos x = x)  ≈", bissecao(f2, 0.0, 1.0, tol=1e-8, verbose=False))

# e^x = 5  → f(x) = e**x - 5
def f3(x):
    return (e**x) - 5.0
print("Raiz (e^x = 5)    ≈", bissecao(f3, 1.0, 2.0, tol=1e-8, verbose=False))



