from lib.interface import *
from lib.file import *

arq = 'dataBase.txt'

if arquivoExtiste(arq) is False:
    criarArquivo(arq)

opcoes = ['Ver pessoas cadastradas',
          'Cadastrar novas pessoas',
          'Sair do programa'
          ]


while True:
    resposta = menu(opcoes)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Até a próxima!')
        break
    else:
        print('Opção inválida. Tente novamente!')

