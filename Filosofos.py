import threading as thr
import time


class Filosofo(thr.Thread):

    acoes = []

    def __init__(self, nome, garfoEsquerda, garfoDireita, comida, id):
        thr.Thread.__init__(self)
        self.nome = nome
        self.garfoEsquerda = garfoEsquerda
        self.garfoDireita = garfoDireita
        self.comida = comida
        self.id = id

    def run(self):

        while True:

            if self.comida == 0:
                self.acoes.append("{}-finalizou-{}-{}".format(self.id, self.comida, self.nome))
                break

            self.pensa()
            self.acoes.append("{}-fome-{}-{}".format(self.id, self.comida, self.nome))
            print("\n{} está com fome".format(self.nome))

            self.tentaComer()

    def pensa(self):
        self.acoes.append("{}-pensando-{}-{}".format(self.id, self.comida, self.nome))
        print("{} esta pensando".format(self.nome))
        time.sleep(1)
        return

    def tentaComer(self):

        self.garfoEsquerda.acquire()    # Pega ESQUERDO bloqueando ESQUERDO
        garfoLivre = self.garfoDireita.acquire()

        if not garfoLivre: #Se o GARFO DIREITA NÃO está livre
            self.garfoEsquerda.release()    # Solta o Garfo
            return

        # Caso o contrário o FILÓSOFO come e LIBERA OS GARFOS
        self.come()

        self.garfoEsquerda.release()
        self.garfoDireita.release()

    def come(self):
        print("{} começou a comer".format(self.nome))

        self.acoes.append("\n{}-come-{}-{}".format(self.id, self.comida, self.nome))
        time.sleep(4)
        self.comida -= 1

        self.acoes.append("\n{}-come-{}-{}".format(self.id, self.comida, self.nome))

        print("{} terminou de comer, prato tem {} comida\n".format(self.nome, self.comida))

