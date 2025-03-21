class Usuarios:
    def __init__(self):
        self.usuarios = {}

    def cad_usu(self):
        
        nome = input('Insira seu nome: ')
        idade = int(input('Sua idade: '))
        email = input('Seu email: ')
        self.usuarios[nome] = {'idade': idade, 'email': email}
        print(f'Usuário {nome} cadastrado com sucesso!')

    def listar_usu(self):
        if not self.usuarios:
            print('Nenhum usuário cadastrado.')
        else:
            print('Lista de usuários cadastrados:')
            for nome, dados in self.usuarios.items():
                print(f"Nome: {nome}, Idade: {dados['idade']}, Email: {dados['email']}")

    def rem(self, nome):
       
        if nome in self.usuarios:
            del self.usuarios[nome]
            print(f'Usuário {nome} removido com sucesso!')
        else:
            print('Usuário não encontrado.')

    def menu(self):
        while True:
            print("""
[ 1 ] Cadastrar novo usuário
[ 2 ] Listar usuários cadastrados
[ 3 ] Remover usuário
[ 4 ] Sair
            """)
            op = int(input('Qual operação deseja fazer? '))
            
            if op == 1:
                self.cad_usu()
            elif op == 2:
                self.listar_usu()
            elif op == 3:
                nome = input('Nome do usuário a ser removido: ')
                self.rem(nome)
            elif op == 4:
                print("Saindo...")
                break
            else:
                print('Opção inválida! Tente novamente.')


usuarios = Usuarios()


usuarios.menu()	