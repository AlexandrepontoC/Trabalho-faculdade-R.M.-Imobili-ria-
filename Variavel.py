print ("Olá Mundo")


# - Variaveis e tipo de dados -

# 1 - O que é uma variavél?
# É um espaço reservado na memória, que serve para
# armazenar qualquer tipo de dado.

# 2 - O que é tipagem dinâmica?
# Significa que não é necessário especificar, 
# na declaração o tipo  de variavél.

# Exemplo de nome de variavéç (snake case):

nome_aluno = "Fernando"
nota_aluno = 8

print (nome_aluno)
print (nota_aluno)

# 3 - Quais os tipos de dados em Python?
# Inteiro (int), Decimal (flooat), Complexo (comples),
# Strimg (str), Boolean (bool), list, tuple, sets e dictionary
# Exemplos: 
ano_atual = 2023
desconto = 15.59
cidade = "Jandira"
filhos = False
#list
cores = ["branco", "azul", "vermelho"]
#tuple
frutas = ("banana", "uva")
#sets
notas = {5, 10, 30}
#dictionary
clientes = {
    "nome": "Maria",
    "altura": 1.95,
    "peso":  60.00

}

# 4 - O que é tipagem forte?
# linguagem tem que ser mais consistente,
# trabalhando com os mesmos dados, 

numero1 = 23
numero02 = 100
print (numero1 + numero02)


# 5 Como trocar o tipo de variável?
preco_produto = 1.90
preco_produto = str(preco_produto)
preco_produto = float(preco_produto)
print (type(preco_produto))