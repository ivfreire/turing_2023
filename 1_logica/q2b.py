#!/bin/python3

def estado_atual(K, entradas, T):
	estado = [ 0 ] * K

	for t in range(1, T + 1):

		# Avança estado
		for i in range(1, K): estado[-i] = estado[-i-1]
		estado[0] = 0

		# Verifica se um carro novo entrou no estacionamento
		for carro, entrada in enumerate(entradas):
			if entrada - t == 0:
				estado[0] = carro + 1
				break

	return estado
