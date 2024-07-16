def leiadinheiro(valor):
    válido = False
    while not válido:
        entrada = str(input(valor)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO!!! "{entrada}" não é um número, digite novamente.\033[m')
        else:
            válido = True
            return float(entrada)
