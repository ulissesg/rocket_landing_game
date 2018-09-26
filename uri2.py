nome= input("digite o nome do funcionario:\n")
sal = float (input("insira o salario fixo:\n"))
vendas= float(input("insira o valor total de vendas:\n"))

total= sal + (vendas*0.15)
print("\nnome: ", nome)
print("salario total: ", total)
