from math import cos, e

def bissecao(f, a, b, tol=1e-6, max_iter=100, verbose=True, return_history=False):
    """
    Método da Bisseção para resolver f(x) = 0 em [a, b].

    Parâmetros:
      f              -> função contínua
      a, b           -> extremos do intervalo inicial
      tol            -> tolerância (critério de parada)
      max_iter       -> número máximo de iterações
      verbose        -> se True, imprime o andamento
      return_history -> se True, devolve também uma lista com o histórico

    Retorna:
      raiz           -> aproximação da raiz
      (raiz, hist)   -> se return_history=True
    """

    # Histórico de iterações
    history = []

    # Casos de borda
    fa = f(a)
    fb = f(b)
    if abs(fa) < tol:
        return (a, history) if return_history else a
    if abs(fb) < tol:
        return (b, history) if return_history else b

    if fa * fb > 0:
        raise ValueError("Não há garantia de raiz: f(a) e f(b) têm o mesmo sinal.")

    # Loop principal
    for k in range(1, max_iter + 1):
        x = (a + b) / 2.0
        fx = f(x)

        # Salva no histórico
        history.append((k, a, b, x, fx))

        if verbose:
            print(f"Iter {k:>3}: a={a:.6f}, b={b:.6f}, x={x:.6f}, f(x)={fx:.6e}")

        # Critérios de parada
        if abs(fx) < tol or (b - a) / 2.0 < tol:
            return (x, history) if return_history else x

        # Atualiza intervalo
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    # Retorna último valor se atingir max_iter
    return ((a + b) / 2.0, history) if return_history else (a + b) / 2.0


# ===================== EXEMPLOS =====================

# Exemplo 1: f(x) = x^2 - x - 1  (a famosa equação do número áureo)
def f1(x): 
    return x*x - x - 1

raiz1, hist1 = bissecao(f1, 1, 2, tol=1e-6, max_iter=30, verbose=False, return_history=True)
print("\n")
print("="*50)
print("Raiz (x^2 - x - 1):", raiz1)
print("-"*50)
print("Histórico (primeiras 5 iterações):")
for h1 in hist1[:5]:
    print(h1)
print("="*50)    


# Exemplo 2: Resolver cos(x) = x  ->  f(x) = cos(x) - x
def f2(x):
    return cos(x) - x

raiz2, hist2 = bissecao(f2, a=0.0, b=1.0, tol=1e-8, max_iter=80, verbose=False, return_history=True)
print("\n")
print("="*50)
print("Raiz (cos x = x) ≈", raiz2)
print("-"*50)
print("Histórico (primeiras 5 iterações):")
for h2 in hist2[:5]:
    print(h2)
print("="*50)    


# Exemplo 3: Resolver e^x = 5  ->  f(x) = e**x - 5
def f3(x):
    return (e**x) - 5.0

raiz3, hist3 = bissecao(f3, a=1.0, b=2.0, tol=1e-8, max_iter=80, verbose=False, return_history=True)
print("\n")
print("="*50)
print("Raiz (e^x = 5) ≈", raiz3)  
print("-"*50)   
print("Histórico (primeiras 5 iterações):")
for h3 in hist3[:5]:
    print(h3)
print("="*50)    
