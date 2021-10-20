from lib.interface import cabecalho

def arquivoExtiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('ERRO: não foi possível criar o arquivo.')
    else:
        print(f'O arquivo {nome} foi criado com sucesso')

def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('ERRO: não foi possível abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:.<21}{dado[1]:.>3} anos;')
    finally:
        arq.close()

def cadastrar(nomeArq, nomePessoa='<Desconhecido>', idade=0):
    try:
        arq = open(nomeArq, 'at')
    except:
        print('ERRO: não foi possível abrir o arquivo.')
    else:
        try:
            arq.write(f'{nomePessoa};{idade}\n')
        except:
            print('ERRO: não foi possível escrever os dados no arquivo.')
        else:
            print(f'{nomePessoa} foi adicionada com sucesso.')
        finally:
            arq.close()
