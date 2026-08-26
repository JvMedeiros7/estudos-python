import lib.interface as interface  # CORRIGIDO: "from lib.interface import *" não cria a variável "interface", só importa os nomes de dentro do módulo. Com "import ... as interface" o nome do módulo passa a existir e "interface.funcao()" funciona.
import lib.arquivos as arquivos    # CORRIGIDO: mesmo problema do import acima, agora "arquivos" existe como objeto de módulo.
from time import sleep
import os

arq = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cursoemvideo.txt')

if arquivos.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado! Criando arquivo...')
    arquivos.criarArquivo(arq)  # CORRIGIDO: antes chamava "criarArquivo(arq)" sem prefixo, que só funcionava por acidente com "import *"; agora precisa do prefixo "arquivos." pois o import mudou para namespace.

while True:
    resposta = interface.menu([' Ver pessoas cadastradas', 'Cadastrar nova pessoa', ' Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo do arquivo
        arquivos.lerArquivo(arq)
        
    elif resposta == 2:
        interface.cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = interface.leiaInt('Idade: ')
        arquivos.cadastrar(arq, nome, idade)  # CORRIGIDO: antes chamava "cadastrar(arq, nome, idade)" sem prefixo, que só funcionava por acidente com "import *"; agora precisa do prefixo "arquivos." pois o import mudou para namespace.
    elif resposta == 3:
        interface.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida!')
    sleep(2)
