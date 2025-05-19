def validar_luhn(numero_cartao):
    """Verifica se um número de cartão de crédito é válido pelo algoritmo de Luhn."""
    numero = [int(digito) for digito in str(numero_cartao)]
    soma = 0
    alternar = False

    for i in range(len(numero) - 1, -1, -1):
        digito = numero[i]
        if alternar:
            digito *= 2
            if digito > 9:
                digito -= 9
        soma += digito
        alternar = not alternar

    return soma % 10 == 0  # Apenas retorna True se a soma for múltiplo de 10
