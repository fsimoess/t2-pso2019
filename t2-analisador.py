#!/usr/bin/env python3

import sys
import csv
import collections

def tarefa1():
	packages=0
	with open(sys.argv[1]) as file:
		leitorcsv = csv.reader(file)
		for linha in leitorcsv:
			packages+=1
	print(packages)

def tarefa2():
	src = []
	file = open(sys.argv[1], 'r')
	for linha in file:
		aux = linha[linha.find("SRC=")+4:]
		src.append(aux[:aux.find(" ")])
	src = collections.Counter(src)

	for (ip, num) in src.most_common(10):
		print ("IP:", ip, "| Numero de Pacotes enviados:", num)

def tarefa3():
	dst = []
	file = open(sys.argv[1], 'r')
	for linha in file:
		aux = linha[linha.find("DST=")+4:]
		dst.append(aux[:aux.find(" ")])
	dst = collections.Counter(dst)

	for (ip, num) in dst.most_common(10):
		print ("IP:", ip, "| Numero de Pacotes recebidos:", num)

def tarefa4():
	src = []
	file = open(sys.argv[1], 'r')
	for linha in file:
		aux = linha[linha.find("PROTO=")+6:]
		src.append(aux[:aux.find(" ")])
	src = collections.Counter(src)

	for (proc, num) in src.most_common(3):
		print("Protocolo: ", proc, "| Contagem:", num)

def tarefa5():
	src = []
	file = open(sys.argv[1], 'r')
	for linha in file:
		aux = linha[linha.find("DPT=")+4:]
		src.append(aux[:aux.find(" ")])
	src = collections.Counter(src)

	lista = []

	for (port, num) in src.most_common(11):
		if port != "":
			print("Porta: ", port, "| Quantidade:", num)

print("1: Número total de pacotes")
tarefa1()
print("--------------------------------------")
print("2: Top 10 IPs fonte e quantos pacotes cada um enviou")
tarefa2()
print("--------------------------------------")
print("3: Top 10 IPs destino e quantos pacotes cada um recebeu")
tarefa3()
print("--------------------------------------")
print("4: Contagem de pacotes por protocolo (TCP, UDP, ICMP)")
tarefa4()
print("--------------------------------------")
print("5: Top 10 portas usadas informando o nome, número da porta, e quantidade")
tarefa5()