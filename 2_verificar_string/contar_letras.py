def contar_letras_a(s):
    s_lower = s.lower()
    
    count_a = s_lower.count('a')
    
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

string = "A programação é uma arte incrível!"  # aqui você pode alterar o valor da string

resultado = contar_letras_a(string)
print(resultado)
