#!/bin/python3

def corrige_emails(emails):
	n_emails = []		# E-mails corrigidos

	# Itera sobre e-mails embaralhados
	for email in emails:
		l = len(email)

		# Divide as metades, inverte os pedaços e monta novo e-mail
		partes = email[0:l//2][::-1], email[l//2:][::-1]
		n_email = ''.join(partes)

		n_emails.append(n_email)

		# Detecta erro no domínio
		if n_email[::-1][0:7][::-1] != '@usp.br': n_emails[-1] = 'ERRO'

	return n_emails