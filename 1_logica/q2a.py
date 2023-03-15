#!/bin/python3

def estacionamento_ok(K, instantes):
	pilha = []

	for c in instantes:
		if c > 0: pilha.append(c)
		else:
			if -c != pilha[-1]: return 'nao'
			pilha.pop()
		print(pilha)
		
	return 'sim'