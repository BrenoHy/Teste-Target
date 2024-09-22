# Teste Técnico 2 

def fibonacci(n):
    fib_1, fib_2 = 0, 1  # Inicializando os dois primeiros números da sequência 

    fibonacci_sequence = [fib_1, fib_2]  # Lista p/ armazenar a sequência gerada

    # Gerando a sequência até que o próximo número seja maior que o número informado
    while fib_2 < n: 
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        fibonacci_sequence.append(fib_2)

    # Verificando se o número informado esta na sequência
    if n in fibonacci_sequence:
        return f"O número {n} pertence a sequência de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."
    

numero = int(input("Informe um número: "))
resultado = fibonacci(numero)
print(resultado)