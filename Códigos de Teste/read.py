#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = list()
#arq = open("file.bin", "rb")
with open("file.bin", "rb") as arq:
	lista.append(arq.read(1))

print(lista)

arq.close()