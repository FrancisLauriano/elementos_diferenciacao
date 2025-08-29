def raiz_metodo_bissecao(f, a, b, tol=0.01):
    
    if f(a) * f(b) >= 0:
        raise ValueError(f"f(a) e f(b) devem ter sinais opostos!")

    k = 0

    while True:
        xk = (a + b) / 2
        fx = f(xk)

        print(f"Interaração {k}: a={a:.4f}, b={b:.4f}, xk={xk:.4f}, f(xk)={fx:.4f}")
