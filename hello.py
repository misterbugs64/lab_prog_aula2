dia_da_semana = int(input("Digite um número da semana que são representados pelos números de 1 a 7: "))
mês = int(input("informe o número do mês: "))

match dia_da_semana:
    case 1|2|3|4|5 if mês == 5:
        print("é um dia da semana")
    case 6|7 if mês == 4:
        print("é um final de semana")
    case _:
        print("dia invalido ou mês invalido")