from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')


def main():
    casa = []

    casa.append(Tarefa('limpar a casa'))
    casa.append(Tarefa('lavar a roupa'))
    casa.append(Tarefa('lavar os pratos'))

    # desafio
    [tarefa.concluir() for tarefa in casa if
     tarefa.descricao == 'lavar os pratos']
    for tarefa in casa:
        print(f'-{tarefa}')


if __name__ == '__main__':
    # se o programa esta sendo executado por si só
    main()
