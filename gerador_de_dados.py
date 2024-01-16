import random


# Lista de 5 nomes
nomes = ['Douglas', 'Mauricio', 'Regina', 'Zaya', 'Matheus']
# Lista de 5 e-mails
emails = ['douglas@gmail.com', 'mauricio@gmail.com',
          'regina@gmail.com', 'zaya@gmail.com', 'matheus@gmail.com']
# Lista com 5 telefones
telefones = ['(31) 9 9555-4455', '(31) 9 8877-6655',
             '(31) 9 3322-1144', '(31) 9 6655-2233', '(31) 9 4477-8855']
# Lista com 5 cidades
cidades = ['João Monlevade', 'São Paulo',
           'Belo Horizonte', 'Rio de Janeiro', 'Itabira']
# Lista com 5 estados
estados = ['Minas Gerais', 'São Paulo', 'Rio de Janeiro', 'Ceara', 'Para']

print(f'--------------- Bem vindo ao gerador de dados ---------------')
print(f'Caso queira finalizar a sessão digite "PARAR"')
print('-'*60)
print(
    f'Escolha uma ou mais opções abaixo para gerar aleatóriamente\n[1] - Nome\n[2] - E-mail\n[3] - Telefone\n[4] - Cidade\n[5] - Estado')
print(f'Digite uma ou mais opção separadas por virgulas. ex:1,2,3...')


# Dados aleatórios

def gerar_dados(dados):
    gerador = []
    for dado in dados:
        if dado == 1:
            gerador.append(random.choice(nomes))
        if dado == 2:
            gerador.append(random.choice(emails))
        if dado == 3:
            gerador.append(random.choice(telefones))
        if dado == 4:
            gerador.append(random.choice(cidades))
        if dado == 5:
            gerador.append(random.choice(estados))
    return gerador


def salvar(resultado):
    with open('resultado.txt', 'a') as arquivo:
        for item in resultado:
            arquivo.write(str(item)+'\n')


if __name__ == "__main__":
    while True:
        entrada = str(input('Digite as opções: '))

        if entrada.upper() == 'PARAR':
            print("Encerrando o programa.")
            break

        try:
            aleatorios = [int(gerador) for gerador in entrada.split(',')]
            dados_aleatorios = gerar_dados(aleatorios)

            opcao_salvar = input(
                "Deseja que as informações sejam salvas em um arquivo? (s/n)").lower()
            if opcao_salvar == 's':
                salvar(dados_aleatorios)

            print(dados_aleatorios)

        except ValueError:
            print("Entrada inválida. Por favor, digite um comando válido!")
