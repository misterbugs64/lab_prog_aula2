dia_da_semana = int(input("Digite um número da semana\nque são representados pelos números de 1 a 7:"))


match dia_da_semana:
    case 1|2|3|4|5:
        print("é um dia da semana")
    case 6|7:
        print("é um final de semana")
    case _:
        print("dia invalido")