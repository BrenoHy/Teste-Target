# Teste Técnico 5   

# Função para inverter a string
def inverter_string(s):
    string_invertida = ""
    # Percorrendo a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Entrada do usuário
entrada = input("Digite uma string para inverter: ")

# Inversão de string
resultado = inverter_string(entrada)

# Exibição do resultado
print("String invertida: ", resultado)
