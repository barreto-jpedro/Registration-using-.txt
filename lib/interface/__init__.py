def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return inteiro

def linha(n=30):
    print('-'*n)

def cabecalho(titulo = 'MENU PRINCIPAL', tamanho=30):
    linha()
    print(titulo.center(tamanho))
    linha()
    
def menu(opcoes):    
    cabecalho()
    for n in opcoes:
        print(f'{opcoes.index(n)+1} - {n}')
    linha()
    escolha = leiaInt()
    return escolha
