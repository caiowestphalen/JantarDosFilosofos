# Estudo de caso - Sistemas operacionais 
# Uni Dom Bosco - Curitiba 
# Aluno: Caio Westphalen


import threading as thr
import time
from Filosofos import Filosofo

def jantarFilosofos():
    nomeFilosofos = ('DomBosco1', 'DomBosco2', 'DomBosco3', 'DomBosco4', 'DomBosco5')

    garfo = [thr.Semaphore() for i in range(5)]     # Informa a quantidade de itens

    filosofos = [Filosofo(nomeFilosofos[i], garfo[i], garfo[(i + 1) % 5], 2, i)     # % - modulus
                    for i in range(5)]

    for f in filosofos:
        f.start()

    time.sleep(30)

    return Filosofo.acoes


def main():
    acoes = jantarFilosofos()
    return acoes


if __name__ == '__main__':

    main()
