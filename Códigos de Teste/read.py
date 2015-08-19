#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = list()
#arq = open("file.bin", "rb")
#with open("file.bin", "rb") as arq:
  #lista.append(arq.read(1))

#print(lista)
#cont = 0
nome = raw_input("Digite o nome do arquivo q deseja abrir\n")
with open(nome, "rb") as f:
    byte = f.read()
    #print(len(byte))
    print(byte)
info = [byte[i:i+1] for i in range(0, len(byte), 1)]



print(info)
