def fibonacci(n):
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def is_fibonacci_number(n):
    fib_sequence = fibonacci(n)
    
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

numero = 21  # aqui você pode alterar o valor para qualquer número que queira testar

resultado = is_fibonacci_number(numero)
print(resultado)