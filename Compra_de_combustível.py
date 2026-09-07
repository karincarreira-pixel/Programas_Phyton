qtd_litros = float(input("Quantidade de litros de combustível:"))
valor_litro = float(input("Valor do litro do combustível:"))
tipo_combustivel = input("Tipo de combustível:")

valor_total = round(qtd_litros * valor_litro, 2)

print("O valor total do abastecimento é de", valor_total)


