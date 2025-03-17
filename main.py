class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone, email):
        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "favorito": False
        }
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso!\n")
    
    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.\n")
            return
        for i, contato in enumerate(self.contatos, start=1):
            favorito = "⭐" if contato["favorito"] else ""
            print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']} {favorito}")
        print()
    
    def editar_contato(self, indice, nome, telefone, email):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice] = {
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "favorito": self.contatos[indice]["favorito"]
            }
            print(f"Contato {nome} editado com sucesso!\n")
        else:
            print("Índice inválido!\n")
    
    def marcar_favorito(self, indice):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice]["favorito"] = not self.contatos[indice]["favorito"]
            status = "favorito" if self.contatos[indice]["favorito"] else "não favorito"
            print(f"Contato {self.contatos[indice]['nome']} marcado como {status}.\n")
        else:
            print("Índice inválido!\n")
    
    def listar_favoritos(self):
        favoritos = [c for c in self.contatos if c["favorito"]]
        if not favoritos:
            print("Nenhum contato favorito.\n")
            return
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']} ⭐")
        print()
    
    def excluir_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos.pop(indice)
            print(f"Contato {contato['nome']} excluído com sucesso!\n")
        else:
            print("Índice inválido!\n")
    

def menu():
    agenda = Agenda()
    while True:
        print("\nAGENDA DE CONTATOS")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar favorito")
        print("5. Listar favoritos")
        print("6. Excluir contato")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == "2":
            agenda.listar_contatos()
        elif opcao == "3":
            agenda.listar_contatos()
            indice = int(input("Digite o número do contato para editar: ")) - 1
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo Email: ")
            agenda.editar_contato(indice, nome, telefone, email)
        elif opcao == "4":
            agenda.listar_contatos()
            indice = int(input("Digite o número do contato para marcar/desmarcar como favorito: ")) - 1
            agenda.marcar_favorito(indice)
        elif opcao == "5":
            agenda.listar_favoritos()
        elif opcao == "6":
            agenda.listar_contatos()
            indice = int(input("Digite o número do contato para excluir: ")) - 1
            agenda.excluir_contato(indice)
        elif opcao == "7":
            print("Saindo da agenda...\n")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
