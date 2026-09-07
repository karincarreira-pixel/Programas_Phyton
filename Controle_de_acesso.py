nome_do_funcionario = input("Digite o nome do funcionário:")
numero_da_matricula = input("Digite o nuemro da matrícula:")
autorizacao = True

funcionario = {"nome": nome_do_funcionario,
               "matricula": numero_da_matricula,
               "autorizado": autorizacao
               }

print("Funcionário:", funcionario["nome"])
print("Matrícula:", funcionario["matricula"])
print("Autorização:", funcionario["autorizado"])


