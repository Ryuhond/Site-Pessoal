lista_livro = [] # Lista que armazena os livros cadastrados
id_global= 1 # Variável global que armazena o ID dos livro
#Mensagem de boas vindas
print ('Bem Vindo a Livraria do Flávio Ryuji Okamoto Honda')


# Cadastrar livro
def cadastrar_livro (id):
                print ('-'*50)
                print ('-'*15 + 'Menu Cadastrar Livro' + '-'*15)
                print (f'ID do livro: {id}')
                nome = input('Por favor entre com o nome do livro: ')
                autor = input('Por favor entre com o autor do livro: ')
                editora = input('Por favor entre com a editora do livro: ')
                livro = {
                    'id': id,
                    'nome': nome,
                    'autor': autor,
                    'editora': editora
                }
                lista_livro.append(livro)
                print ('-'*50)

#Consultar livros cadastrados
def consultar_livro():
    while True:
        print('-'*50)
        print('-'*15 + 'Menu Consultar Livro' + '-'*15)
        print('Escolha a opção desejada:')
        print('1 - Consultar todos os livros')
        print('2 - Consultar livro por ID')
        print('3 - Consultar livro(s) por autor')
        print('4 - Retornar')
        try:
            opcao_consul = int(input('>>'))
        except ValueError:
            print('Por favor insira uma opção válida') #Caso o usuário insira uma opção inválida
            continue
        
#Opcão de consulta de todos os livros
        if opcao_consul == 1:
            print('-'*16)
            for livro in lista_livro:
                print('Id: ', livro['id'])
                print('Nome: ', livro['nome'])
                print('Autor: ', livro['autor'])
                print('Editora: ', livro['editora'])
                print('-'*16)
            print('-'*50)

#Opcão de consulta por ID
        elif opcao_consul == 2:
            try:
                id = int(input('Digite o id do livro: '))
            except ValueError:
                print('Por favor, insira um ID existente')
                continue
            existe_ID = False
            print('-'*16)
            for livro in lista_livro:
                if livro['id'] == id:
                    print('Id: ', livro['id'])
                    print('Nome: ', livro['nome'])
                    print('Autor: ', livro['autor'])
                    print('Editora: ', livro['editora'])
                    print('-'*16)
                    print('-'*50)
                    existe_ID = True
                    break
            if not existe_ID:
                print('Por favor, insira um ID existente') #Caso o ID não exista

#Opcão de consulta por autor
        elif opcao_consul == 3:
            autor = input('Digite o nome do autor: ').lower()
            print('-'*16)
            for livro in lista_livro:
                if livro['autor'].lower() == autor:
                    print('Id: ', livro['id'])
                    print('Nome: ', livro['nome'])
                    print('Autor: ', livro['autor'])
                    print('Editora: ', livro['editora'])
                    print('-'*16)
            print('-'*50)

#Opcão de retornar ao menu 
        elif opcao_consul == 4:
            break

#Caso o usuário insira uma opção inválida
        else:
            print('Por favor insira uma opção válida')
            print('-'*50)
            continue

#Remover livros cadastrados
def remover_livro():
    print('-'*50)
    print('-'*15 + 'Menu Remover Livro' + '-'*15)
    while True:
        try:
            Id_remover = int(input('Digite o id do livro a ser removido: '))
        except ValueError:
            print('Por favor, insira um ID existente') #Caso o usuário insira um id inválido
            continue
        for livro in lista_livro:
            if livro['id'] == Id_remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                return
        print('ID não encontrado. Tente novamente.') #Caso o ID não exista
         

#Menu principal
while True:
    print ('-'*50)
    print ('-'*15 + '   Menu Principal  ' + '-'*15)
    print ('Escolha a opção desejada:')
    print ('1 - Cadastrar Livro')
    print ('2 - Consultar Livro(s)')
    print ('3 - Remover Livro')
    print ('4 - Sair')
    try:
        opcao = int(input('>>')) 
    except ValueError:
        print ('Por favor insira uma opção válida')#Caso o usuário insira uma opção inválida
        continue
    if opcao < 1 or opcao > 4:
        print ('Por favor insira uma opção válida')#Caso o usuário insira uma opção inválida
        continue
    
#Verifica a opção escolhida pelo usuário
    if opcao == 1:
        cadastrar_livro(id_global) #Cadastrar livro
        id_global += 1
    elif opcao == 2:
        consultar_livro() #Consultar livros cadastrados
    elif opcao == 3:
         remover_livro() #Remover livros cadastrados
    elif opcao == 4: #Sair do programa
        print ('Encerrando o programa...Aguarde alguns instantes...')
        print ('-'*50)
        break