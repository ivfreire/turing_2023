#!/bin/python3

def conta_economia(emails):
	economia = 0

	# Itera sobre lista de emails
	for i in range(1, len(emails)):
		# Pega último e penútimo email e descarta o "@usp.br"
		mails = emails[i-1][0:len(emails[i-1])-7], emails[i][0:len(emails[i])-7]

		# Tamanho do menor email
		l = min(len(mails[0]), len(mails[1]))

		# Itera letra a letra do nome do email
		for j in range(0,l):
			if mails[0][len(mails[0])-l+j] != mails[1][len(mails[1])-l+j]: break	# Se caracteres forem diferentes encerra o loop
			economia += 1

	return economia