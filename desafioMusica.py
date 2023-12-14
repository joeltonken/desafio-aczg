class Musica:
    def __init__(self):
        self.letra = [] # Inicializa a classe com uma lista vazia para armazenar as linhas da letra.

    """
    As funções que receberão estrofes terão seus nomes de acordo com sua posição na música original
    https://www.letras.mus.br/padre-marcelo-rossi/47896/
    """
    
    def estrofe_um(self):
        """Adiciona as linhas correspondentes à primeira estrofe da música."""
        for _ in range(2): # Eliminar repetição da frase, exibindo duas vezes.
            self.letra.append("Erguei as mãos e dai glória a Deus")
        self.letra.extend([
            "Erguei as mãos",
            "E cantai como os filhos do Senhor\n"
        ])

    def estrofe_cinco(self):
        """Adiciona as linhas correspondentes à quinta estrofe da música."""
        for _ in range(2):
            self.letra.append("Deus disse a Noé: Constrói uma arca")
        self.letra.append("Que seja feita")
        self.letra.append("De madeira para os filhos do Senhor\n")

    def estrofe_nove(self, *args):
        """Adiciona linhas à letra com base na lista_corpo."""
        for item in args:
            if isinstance(item, list): # Se o argumento for uma lista, junta seus elementos em uma string.
                self.letra.append(", ".join(item))
            else:
                self.letra.append(item)
        self.letra.extend([
            "O senhor tem muitos filhos",
            "Muitos filhos ele tem",
            "Eu sou um deles, você também",
            "Louvemos ao senhor\n"
        ])

    def estrofe_ultima(self):
        self.letra.extend([
            "Braço direito e braço esquerdo",
            "Perna direita e perna esquerda",
            "Balança a cabeça e dá uma voltinha",
            "Dá um pulinho e abraça o irmão"
        ])

    def repeticao_animais(self, animal1, animal2):
        """Adiciona linhas à letra com base nos animais e na repetição fornecida."""
        for _ in range(2):
            self.letra.append(f"Os animaizinhos subiram de dois em dois")
        self.letra.append(f"{animal1}")
        self.letra.append(f"E os {animal2}, como os filhos do Senhor\n")

    def adicionar_linha(self, texto):
        """Adiciona uma linha à letra com base no texto fornecido."""
        self.letra.append(f"{texto}")

    def opcional(self, texto):
        """Adiciona uma linha à letra com base no texto opcional, os que possuem () na letra original."""
        self.letra.append(f"({texto})")

    def imprimir_letra(self): 
        """Imprime cada linha da letra."""
        for linha in self.letra:
            print(linha)

    @staticmethod
    def letra_parte_um():
        """Cria e retorna a letra da primeira parte da música."""
        musica = Musica()
        musica.estrofe_um()
        musica.repeticao_animais("O elefante", "passarinhos")
        musica.opcional("Para não!")
        musica.repeticao_animais("A minhoquinha", "pinguins")
        musica.repeticao_animais("O canguru", "sapinhos")

        musica.estrofe_cinco()
        musica.adicionar_linha("Por isso...!")
        musica.estrofe_um()
        musica.estrofe_um()
        musica.opcional("de novo!")
        musica.estrofe_um()

        return "\n".join(musica.letra)

    @staticmethod
    def letra_parte_dois():
        """Cria e retorna a letra da segunda parte da música."""
        musica = Musica()
        musica.adicionar_linha("E atenção agora, porque\n")

        musica.estrofe_nove()
        musica.estrofe_nove()

        lista_corpo = [
            "Braço direito", "Braço esquerdo", "\nPerna direita", "Perna esquerda",
            "\nBalança a cabeça", "Dá uma voltinha", "\nDá um pulinho",
        ]

        # Adiciona as partes do corpo com base em subconjuntos da lista_corpo.
        for i in range(2, 8):
            itens_corpo = lista_corpo[0:i]
            musica.estrofe_nove(itens_corpo)

        musica.estrofe_ultima()

        return "\n".join(musica.letra)


if __name__ == "__main__": # Bloco principal do programa.
    print("\n-------------------------------------------\n"
          "\nPadre Marcelo Rossi - Erguei as Mãos\n"
          "\n-------------------------------------------\n\n")

    opcoes_menu = 0
    while opcoes_menu != '4':
        # Menu interativo para escolher opções de exibição da letra.
        opcoes_menu = input("\nEscolha uma das opções abaixo: \n\n"
                                "1 - Exibir apenas a primeira parte da música.\n"
                                "2 - Exibir apenas a segunda parte da música.\n"
                                "3 - Exibir a letra da música completa.\n"
                                "4 - Sair do programa.\n\n"
                                "Informe a opção desejada: ")
        print("\n")

        if opcoes_menu == '1':
            print(Musica.letra_parte_um())
        elif opcoes_menu == '2':
            print(Musica.letra_parte_dois())
        elif opcoes_menu == '3':
            print(Musica.letra_parte_um())
            print(Musica.letra_parte_dois())
        elif opcoes_menu == '4':
            print("Muito obrigado pela oportunidade! \n")
        else:
            print("Opção Inválida! Por favor, escolha uma opção válida.\n")