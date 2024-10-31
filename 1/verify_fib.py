


def gerar_fib(n):
    fib = [0,1,1]
    numero_fib = 0
    if n == 0 or n == 1:
            return print("Número pertence a sequência de fibonnaci!!")
            
    else:
            while True:
                numero_fib = fib[-1] + fib[-2]
                if numero_fib > n:
                    return print("Número não pertence a sequência de fibonnaci!!")
                    break;
                elif numero_fib == n:
                    return print("Número pertence a sequência de fibonnaci!!")
                else:
                    fib.append(numero_fib)
                    continue;
    
        
    




