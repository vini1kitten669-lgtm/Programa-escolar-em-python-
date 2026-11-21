class Aluno:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = float(media)
        self.situacao = self.calcular_situacao()
    def calcular_situacao(self):
        if self.media >= 7.0:
            return "Aprovado"
        elif self.media >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"
    def atualizar_dados(self, novo_nome, nova_media):
        self.nome = novo_nome
        self.media = float(nova_media)
        self.situacao = self.calcular_situacao()
class Escola:
    def __init__(self):
        self.alunos = []
    def inscrever_aluno(self):
        nome = input("Informe o nome do aluno: ").strip()
        media = float(input("Informe a média final do aluno: "))
        novo_aluno = Aluno(nome, media)
        self.alunos.append(novo_aluno)
        print(f"Aluno '{nome}' inscrito com sucesso!")
    def _buscar_aluno_por_nome(self, nome_busca):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome_busca.lower():
                return aluno
        return None
    def editar_aluno(self):
        nome_atual = input("Informe o nome atual do aluno que deseja atualizar: ").strip()
        aluno = self._buscar_aluno_por_nome(nome_atual)
        if aluno:
            novo_nome = input("Informe o novo nome do aluno: ").strip()
            nova_media = float(input("Informe a nova média do aluno: "))
            aluno.atualizar_dados(novo_nome, nova_media)
            print("Dados do aluno atualizados com sucesso!")
        else:
            print("Aluno não encontrado.")
    def excluir_aluno(self):
        nome_busca = input("Informe o nome do aluno que deseja remover: ").strip()
        aluno = self._buscar_aluno_por_nome(nome_busca)
        if aluno:
            confirmacao = input(f"Tem certeza que deseja remover '{aluno.nome}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                self.alunos.remove(aluno)
                print("Aluno removido com sucesso!")
            else:
                print("Ação cancelada.")
        else:
            print("Aluno não encontrado.")
    def _exibir_tabela(self, lista_alunos):
        if not lista_alunos:
            print("Nenhum aluno encontrado para exibição.")
            return
        print("\nnome | média | situação")
        print("-" * 30)
        for aluno in lista_alunos:
            media_formatada = int(aluno.media) if aluno.media.is_integer() else aluno.media
            print(f"{aluno.nome} | {media_formatada} | {aluno.situacao}")
        print()
    def visualizar_alunos(self):
        self._exibir_tabela(self.alunos)
    def filtrar_alunos(self):
        print("\nSelecione o filtro desejado:")
        print("1 - Mostrar todos os alunos")
        print("2 - Mostrar alunos aprovados")
        print("3 - Mostrar alunos de recuperação")
        print("4 - Mostrar alunos reprovados")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            filtrados = self.alunos
        elif opcao == "2":
            filtrados = [a for a in self.alunos if a.situacao == "Aprovado"]
        elif opcao == "3":
            filtrados = [a for a in self.alunos if a.situacao == "Recuperação"]
        elif opcao == "4":
            filtrados = [a for a in self.alunos if a.situacao == "Reprovado"]
        else:
            print("Opção de filtro inválida.")
            return
        self._exibir_tabela(filtrados)
    def salvar_arquivo(self):
        nome_arquivo = input("Informe o nome do arquivo onde os alunos serão salvos (ex: alunos.txt): ").strip()
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for aluno in self.alunos:
                media_formatada = int(aluno.media) if aluno.media.is_integer() else aluno.media
                arquivo.write(f"{aluno.nome}, {media_formatada}, {aluno.situacao}\n")
        print(f"Alunos salvos com sucesso em '{nome_arquivo}'!")
    def carregar_arquivo(self):
        nome_arquivo = input("Informe o nome do arquivo de onde os alunos serão carregados: ").strip()
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                carregados = 0
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        partes = linha.split(",")
                        nome = partes[0].strip()
                        media = float(partes[1].strip())
                        self.alunos.append(Aluno(nome, media))
                        carregados += 1
            print(f"{carregados} aluno(s) carregado(s) com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique o nome e tente novamente.")
def menu():
    escola = Escola()
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE ALUNOS ===")
        print("1. Inscrever novo aluno")
        print("2. Editar dados de um aluno")
        print("3. Excluir aluno")
        print("4. Visualizar lista de alunos")
        print("5. Filtrar alunos por situação")
        print("6. Salvar alunos em arquivo")
        print("7. Carregar alunos de arquivo")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            escola.inscrever_aluno()
        elif opcao == "2":
            escola.editar_aluno()
        elif opcao == "3":
            escola.excluir_aluno()
        elif opcao == "4":
            escola.visualizar_alunos()
        elif opcao == "5":
            escola.filtrar_alunos()
        elif opcao == "6":
            escola.salvar_arquivo()
        elif opcao == "7":
            escola.carregar_arquivo()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    menu()