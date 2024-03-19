from time import time, sleep


tempoInicial = time()

for i in range(10):
    sleep(1)

tempoFinal = time()

print("Tempo de execução: ", tempoFinal - tempoInicial)