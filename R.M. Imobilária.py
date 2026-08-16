print('******************')
print('R.M. IMOBILIÁRIA')
print('******************')

# Valor do Contrato
valor_contrato = 2000.00
valor_imovel = 0.0
valor_garagem = 0.0

print(f"Valor taxa de contrato: R$ {valor_contrato:.2f}\n")

# opções do imóvel
opcao_pgto = ""
opcoes_validas = ["1", "2", "3", "4", "5"]

while opcao_pgto not in opcoes_validas:
    opcao_pgto = input(
        """Selecione o tipo de locação:
 (1) - Apartamento R$ 700.00 / 1 Quarto
 (2) - Apartamento R$ 900.00 / 2 Quartos
 (3) - Casa R$ 900.00 / 1 Quarto
 (4) - Casa R$ 1150.00 / 2 Quartos
 (5) - Estudio R$ 1200.00
Digite a opção desejada: """
    )

    if opcao_pgto not in opcoes_validas:
        print("\n[Erro] Opção inválida! Escolha um número de 1 a 5.\n")

# Valor do imóvel escolhido
if opcao_pgto == "1":
    valor_imovel = 700.00
elif opcao_pgto == "2":
    valor_imovel = 900.00
elif opcao_pgto == "3":
    valor_imovel = 900.00
elif opcao_pgto == "4":
    valor_imovel = 1150.00
elif opcao_pgto == "5":
    valor_imovel = 1200.00

# sobre a garagem
quer_garagem = input("\nGostaria de vaga de garagem? (S/N): ").upper()

if quer_garagem == "S":
    if opcao_pgto == "5":  # Se for Estúdio
        valor_garagem = 250.00
    else:  # Demais opções
        valor_garagem = 200.00

#  Parcelamento do Contrato caso houver
parcelas_contrato = 1
while True:
    try:
        print("\nA taxa de contrato (R$ 2000.00) pode ser parcelada em até 5x sem juros.")
        parcelas_contrato = int(
            input("Digite a quantidade de parcelas desejada (1 a 5): ")
        )

        if 1 <= parcelas_contrato <= 5:
            break  # Sai do loop se o número for válido
        else:
            print("[Erro] Por favor, escolha um número entre 1 e 5.")
    except ValueError:
        print("[Erro] Digite apenas números inteiros.")

# Cálculos financeiros
valor_parcela_contrato = valor_contrato / parcelas_contrato
mensalidade_total = valor_imovel + valor_garagem

# O primeiro pagamento será a mensalidade + a primeira parcela do contrato
total_primeiro_mes = mensalidade_total + valor_parcela_contrato

# resumo detalhado
print("\n" + "=" * 45)
print("             RESUMO DO CONTRATO              ")
print("=" * 45)
print(f"Aluguel do Imóvel:            R$ {valor_imovel:.2f}")
print(f"Acréscimo de Garagem:         R$ {valor_garagem:.2f}")
print(f"valor fixo:       R$ {mensalidade_total:.2f}")
print("-" * 45)
print(f"Taxa de Contrato (Total):     R$ {valor_contrato:.2f}")
print(f"Parcelamento do Contrato:     {parcelas_contrato}x de R$ {valor_parcela_contrato:.2f}")
print("-" * 45)
print(f"valor a pagar no 1° mes:      R$ {total_primeiro_mes:.2f}")
print(f"valor das demais parcelas ({2} ao {parcelas_contrato}): R$ {total_primeiro_mes:.2f}" if parcelas_contrato > 1 else "")
print(f"total a pagar apos quitação:  R$ {mensalidade_total:.2f}")
print("=" * 45)